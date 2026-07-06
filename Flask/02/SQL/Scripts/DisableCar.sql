\c lyfter_car_rental;

CREATE OR REPLACE PROCEDURE DisableCar(
    p_id INT,
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM Cars
        WHERE id = p_id
     ) THEN

        UPDATE Cars
        SET status = 'No Disponible'
        WHERE id = p_id;

    END IF;
    COMMIT;
END;
$$;


