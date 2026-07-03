CREATE OR REPLACE PROCEDURE UpdateCar(
    p_id INT,
    p_status VARCHAR(50)
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE Cars
    SET status = p_status
    WHERE id = p_id;
    COMMIT;
END;
$$;
