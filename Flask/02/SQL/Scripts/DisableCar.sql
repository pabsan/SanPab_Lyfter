CREATE OR REPLACE PROCEDURE lyfter_car_rental.DisableCar(
    p_id INT
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
        SET status = 'No Disponible'
        WHERE id = p_id;

    END IF;
    COMMIT;
END;
$$;


