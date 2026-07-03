CREATE OR REPLACE PROCEDURE NewRental(
    p_user_id INT,
    p_car_id INT,
    p_start_date DATE,
    p_end_date DATE
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM cars
        WHERE id = p_car_id AND lower(status) = 'disponible'
    ) THEN
        UPDATE cars
        SET status = 'Rentado'
        WHERE id = p_car_id;
    
        INSERT INTO Rents (user_id, car_id, rental_date, rental_end_date)
        VALUES (p_user_id, p_car_id, p_start_date, p_end_date);
    END IF;
    COMMIT;
END;
$$;


