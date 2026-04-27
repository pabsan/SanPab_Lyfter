DO $$
DECLARE
	v_availabe_stock INTEGER;
	v_products INT[] := ARRAY[1,2,3];
	v_product INT;
	v_email varchar(150) := 'juan@example.com';
	v_user_id INT;
	v_bill_id INT;
BEGIN
	FOREACH v_product IN ARRAY v_products
	LOOP
		SELECT stock INTO v_availabe_stock
		FROM products
		WHERE product_id = v_product;

		IF v_availabe_stock IS NULL OR v_availabe_stock < 1 THEN
			RAISE EXCEPTION 'Stock insuficiente. Abortando transacción.';
		END IF;
	END LOOP;

	SELECT user_id INTO v_user_id
	FROM users
	WHERE email = v_email;

	IF v_user_id IS NULL THEN
		RAISE EXCEPTION 'Usuario no existe. Abortando transacción.';
	END IF;

	-- insertar factura
	INSERT INTO bills (user_id, total)
	VALUES (v_user_id, 0)
	RETURNING bill_id INTO v_bill_id;

	IF v_bill_id IS NULL THEN
		RAISE EXCEPTION 'Error al crear la factura. Abortando transacción.';
	END IF;

	BEGIN
		-- insertar items de factura
		INSERT INTO bill_items (bill_id, product_id, quantity, unit_price)
		SELECT v_bill_id, product_id, 3, price
		FROM products
		WHERE product_id = 1;

		INSERT INTO bill_items (bill_id, product_id, quantity, unit_price)
		SELECT v_bill_id, product_id, 2, price
		FROM products
		WHERE product_id = 2;

		-- actualizar stock de productos
		UPDATE products
		SET stock = stock - 3
		WHERE product_id = 1;

		UPDATE products
		SET stock = stock - 2
		WHERE product_id = 2;
	
		-- actualizar total de la factura
		UPDATE bills
		SET total = (SELECT SUM(subtotal) FROM bill_items WHERE bill_id = v_bill_id)
		WHERE bill_id = v_bill_id;	
	EXCEPTION
		WHEN OTHERS THEN
			RAISE EXCEPTION 'Error al procesar la factura: %', SQLERRM;
	END;

	RAISE NOTICE 'Factura procesada exitosamente. ID de factura: %', v_bill_id;

END $$;


