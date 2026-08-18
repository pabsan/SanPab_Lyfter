CREATE OR REPLACE PROCEDURE lyfter_car_rental.UpdateCar(
    p_id INT,
    p_status VARCHAR(50)
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE lyfter_car_rental.Cars
    SET status = p_status
    WHERE id = p_id;
    COMMIT;
END;
$$;
