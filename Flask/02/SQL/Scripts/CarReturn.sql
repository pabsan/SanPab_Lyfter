CREATE OR REPLACE PROCEDURE lyfter_car_rental.CarReturn(
    p_id INT,
    p_return_date TIMESTAMP DEFAULT NOW()
)
LANGUAGE plpgsql
AS $$
DECLARE 
    moroso_flag BOOLEAN;

BEGIN
    IF EXISTS (
        SELECT 1
        FROM lyfter_car_rental.Rents
        WHERE id = p_id
     ) THEN
        SELECT rental_end_date < p_return_date INTO moroso_flag
        FROM lyfter_car_rental.Rents
        WHERE id = p_id;

        IF (moroso_flag) THEN
            UPDATE lyfter_car_rental.Rents
            SET return_date = p_return_date
                ,status = 'Moroso'
            WHERE id = p_id;
        ELSE
            UPDATE lyfter_car_rental.Rents
            SET return_date = p_return_date
                ,status = 'Devuelto'
            WHERE id = p_id;
        END IF;
        
        UPDATE lyfter_car_rental.Cars
        SET status = 'Disponible'
        WHERE id = (SELECT car_id FROM lyfter_car_rental.Rents WHERE id = p_id);
    END IF;
    COMMIT;
END;
$$;


