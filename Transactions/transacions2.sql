-- 1. Verificar que la factura existe
DO $$
DECLARE
    v_bill_id INT := 1; 
	v_exists INT;
BEGIN
    SELECT COUNT(*) INTO v_exists
    FROM bills
    WHERE bill_id = v_bill_id;

    IF v_exists = 0 THEN
        RAISE EXCEPTION 'La factura % no existe', v_bill_id;
    END IF;
	
	-- 2. Aumentar el stock de productos
	UPDATE products p
	SET stock = p.stock + bi.quantity
	FROM bill_items bi
	WHERE p.product_id = bi.product_id
	  AND bi.bill_id = v_bill_id; 
	
	-- 3. Marcar la factura como retornada
	UPDATE bills
	SET status = 'Retornada'
	WHERE bill_id = v_bill_id;

	RAISE NOTICE 'Factura actualizada exitosamente';

END $$;