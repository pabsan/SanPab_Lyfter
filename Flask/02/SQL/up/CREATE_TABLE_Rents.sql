CREATE TABLE IF NOT EXISTS lyfter_car_rental.Rents (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    user_id INT NOT NULL,
    car_id INT NOT NULL,

    rental_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    rental_end_date TIMESTAMP NOT NULL,
    return_date TIMESTAMP NULL,
    status VARCHAR(50) NOT NULL,

    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_rents_user
        FOREIGN KEY (user_id)
        REFERENCES lyfter_car_rental.Users(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_rents_car
        FOREIGN KEY (car_id)
        REFERENCES lyfter_car_rental.Cars(id)
        ON DELETE CASCADE
);


DO $$
DECLARE
    row_count INT;
BEGIN
    SELECT COUNT(*) INTO row_count FROM lyfter_car_rental.Rents;

    IF row_count = 0 THEN
		INSERT INTO lyfter_car_rental.Rents (user_id, car_id, status, rental_end_date)
		VALUES (2, 6, 'Activo', '2026-07-31');
	
		INSERT INTO lyfter_car_rental.Rents (user_id, car_id, status, rental_end_date)
		VALUES (4, 10, 'Atraso', '2026-07-7');
		
		INSERT INTO lyfter_car_rental.Rents (user_id, car_id, status, rental_end_date)
		VALUES (14, 17, 'Activo', '2026-08-01');
		
		INSERT INTO lyfter_car_rental.Rents (user_id, car_id, status, rental_end_date)
		VALUES (17, 23, 'Activo', '2026-09-15');
		
		INSERT INTO lyfter_car_rental.Rents (user_id, car_id, status, rental_end_date)
		VALUES (26, 49, 'Activo', '2026-12-31');
END IF;
END $$;

