\c lyfter_car_rental;

CREATE TABLE IF NOT EXISTS lyfter_car_rental.Rents (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    user_id INT NOT NULL,
    car_id INT NOT NULL,

    rental_date DATE NOT NULL,
    rental_end_date DATE NOT NULL,
    return_date DATE NULL,
    status VARCHAR(50) NOT NULL,

    created_dated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_rents_user
        FOREIGN KEY (user_id)
        REFERENCES lyfter_car_rental.Users(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_rents_car
        FOREIGN KEY (car_id)
        REFERENCES lyfter_car_rental.Cars(id)
        ON DELETE CASCADE
);
