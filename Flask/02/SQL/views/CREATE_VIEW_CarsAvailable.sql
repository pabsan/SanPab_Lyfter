CREATE OR REPLACE VIEW lyfter_car_rental.CarsAvailable AS
SELECT Model,
	   Brand,
	   Model_Year,
	   Status
FROM lyfter_car_rental.Cars
WHERE Status IN ('Disponible','Nuevo')