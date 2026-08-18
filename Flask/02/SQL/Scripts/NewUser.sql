CREATE OR REPLACE PROCEDURE lyfter_car_rental.DisableCar(
    p_id INT,
	OUT p_result VARCHAR(100)
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM lyfter_car_rental.Cars
        WHERE id = p_id
     ) THEN

        UPDATE lyfter_car_rental.Cars
        SET status = 'Desuso'
        WHERE id = p_id;

		p_result := 'Car updated successfully';
	ELSE
		p_result := 'Error: Car does not exists';

    END IF;
    COMMIT;
END;
$$;

