CREATE OR REPLACE VIEW lyfter_car_rental.CarsRented AS
SELECT c.Model,
	   c.Brand,
	   c.Model_Year,
	   c.Status,
	   r.Rental_Date,
	   r.Rental_End_Date,
	   COALESCE(CAST(r.Return_Date AS VARCHAR(15)),'') AS Return_Date,
	   r.Status as Rent_Status
FROM lyfter_car_rental.cars AS c
INNER JOIN lyfter_car_rental.rents AS r
	ON c.id = r.car_id
WHERE c.status = 'Ocupado'