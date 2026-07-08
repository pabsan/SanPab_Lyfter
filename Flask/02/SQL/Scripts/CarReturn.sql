CREATE OR REPLACE PROCEDURE lyfter_car_rental.CarReturn(
    p_id INT,
    p_return_date TIMESTAMP DEFAULT NOW()
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM lyfter_car_rental.Rents
        WHERE id = p_id
     ) THEN
        UPDATE lyfter_car_rental.Rents
        SET return_date = p_return_date
        WHERE id = p_id;

        UPDATE lyfter_car_rental.Cars
        SET status = 'Disponible'
        WHERE id = (SELECT car_id FROM lyfter_car_rental.Rents WHERE id = p_id);
    END IF;
    COMMIT;
END;
$$;


