\c lyfter_car_rental;

CREATE OR REPLACE PROCEDURE UpdateUser(
    p_id INT,
    p_status VARCHAR(50)
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE Users
    SET status = p_status
    WHERE id = p_id;
    COMMIT;
END;
$$;
