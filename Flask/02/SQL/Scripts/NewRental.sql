CREATE OR REPLACE PROCEDURE lyfter_car_rental.NewRental(
    p_user_id INT,
    p_car_id INT,
    p_end_date TIMESTAMP
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM lyfter_car_rental.Cars
        WHERE id = p_car_id AND lower(status) = 'disponible'
    ) THEN
        UPDATE lyfter_car_rental.Cars
        SET status = 'Ocupado'
        WHERE id = p_car_id;
    
        INSERT INTO lyfter_car_rental.Rents (user_id, car_id, status, rental_end_date)
        VALUES (p_user_id, p_car_id, 'Activo', p_end_date);
    END IF;
    COMMIT;
END;
$$;


