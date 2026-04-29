ALTER TABLE bills
ADD COLUMN IF NOT EXISTS status VARCHAR(20) DEFAULT 'Activa';

-- 1. Verificar que la factura existe
DO $$
DECLARE
    v_bill_id INT := 1; 
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
	  AND bi.bill_id = 1; 
	
	-- 3. Marcar la factura como retornada
	UPDATE bills
	SET status = 'Retornada'
	WHERE bill_id = 1;

	COMMIT;

	RAISE NOTICE 'Factura actualizada exitosamente';

END $$;