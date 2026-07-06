
\c lyfter_car_rental;

CREATE OR REPLACE PROCEDURE NewUser(
    p_name VARCHAR(100),
    p_email VARCHAR(100),
    p_username VARCHAR(50),
    p_born_date DATE,
    p_password VARCHAR(255),
    p_status VARCHAR(50),
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM Users
        WHERE email = p_email OR username = p_username;
    ) THEN
        INSERT INTO Users (name, email, username, born_date, password, status)
        VALUES (p_name, p_email, p_username, p_username, p_born_date, p_password, p_status);
    END IF;
    COMMIT;
END;
$$;
