CREATE TABLE IF NOT EXISTS Rents (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    user_id INT NOT NULL,
    car_id INT NOT NULL,

    rental_date DATE NOT NULL,
    return_date DATE NULL,
    status VARCHAR(50) NOT NULL,

    created_dated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_rents_user
        FOREIGN KEY (user_id)
        REFERENCES Users(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_rents_car
        FOREIGN KEY (car_id)
        REFERENCES Cars(id)
        ON DELETE CASCADE
);
