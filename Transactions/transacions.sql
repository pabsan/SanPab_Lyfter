DO $$
DECLARE
    v_available_stock INT;
    v_products INT[] := ARRAY[1,2,3];
    v_quantities INT[] := ARRAY[3,2,1]; -- 👈 ahora sí incluye producto 3
    v_product INT;
    v_user_id INT;
    v_bill_id INT;
    v_email VARCHAR(150) := 'juan@example.com';
    i INT;
BEGIN

    -- Validación de stock
    FOR i IN 1..array_length(v_products,1)
    LOOP
        SELECT stock INTO v_available_stock
        FROM products
        WHERE product_id = v_products[i];

        IF v_available_stock IS NULL OR v_available_stock < v_quantities[i] THEN
            RAISE EXCEPTION 
            'Stock insuficiente para producto % (stock: %, requerido: %)',
            v_products[i], v_available_stock, v_quantities[i];
        END IF;
    END LOOP;

    -- Validar usuario
    SELECT user_id INTO v_user_id
    FROM users
    WHERE email = v_email;

    IF v_user_id IS NULL THEN
        RAISE EXCEPTION 'Usuario no existe';
    END IF;

    -- Crear factura
    INSERT INTO bills (user_id, total)
    VALUES (v_user_id, 0)
    RETURNING bill_id INTO v_bill_id;

    -- Procesar productos (INSERT + UPDATE en un solo loop)
    FOR i IN 1..array_length(v_products,1)
    LOOP
        -- Insertar item
        INSERT INTO bill_items (bill_id, product_id, quantity, unit_price)
        SELECT v_bill_id, product_id, v_quantities[i], price
        FROM products
        WHERE product_id = v_products[i];

        -- Actualizar stock
        UPDATE products
        SET stock = stock - v_quantities[i]
        WHERE product_id = v_products[i];
    END LOOP;

    -- Actualizar total
    UPDATE bills
    SET total = (
        SELECT SUM(subtotal)
        FROM bill_items
        WHERE bill_id = v_bill_id
    )
    WHERE bill_id = v_bill_id;

    RAISE NOTICE 'Factura creada: %', v_bill_id;

END $$;