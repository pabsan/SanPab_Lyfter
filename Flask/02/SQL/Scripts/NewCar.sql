CREATE OR REPLACE PROCEDURE lyfter_car_rental.NewCar(
    p_brand VARCHAR(100),
    p_model VARCHAR(100),
    p_model_year INT,
    p_status VARCHAR(50),
	OUT p_result VARCHAR(100)
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM lyfter_car_rental.Cars
        WHERE brand = p_brand AND model = p_model AND model_year = p_model_year AND status = p_status
    ) THEN
        INSERT INTO lyfter_car_rental.Cars (brand, model, model_year, status)
        VALUES (p_brand, p_model, p_model_year, p_status);

        p_result := 'Car created successfully';
    ELSE
        p_result := 'Error: Car already exists';
    END IF;
    COMMIT;
END;
$$;


