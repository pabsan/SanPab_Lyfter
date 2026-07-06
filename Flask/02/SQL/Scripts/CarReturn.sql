\c lyfter_car_rental;

CREATE OR REPLACE PROCEDURE CarReturn(
    p_id INT,
    p_return_date TIMESTAMP DEFAULT NOW()
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM Rents
        WHERE id = p_id
     ) THEN
        UPDATE Rents
        SET return_date = p_return_date
        WHERE id = p_id;

        UPDATE Cars
        SET status = 'Disponible'
        WHERE id = (SELECT car_id FROM Rents WHERE id = p_id);
    END IF;
    COMMIT;
END;
$$;


