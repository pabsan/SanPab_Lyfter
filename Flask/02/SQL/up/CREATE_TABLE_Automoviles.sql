CREATE TABLE IF NOT EXISTS Cars (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    brand VARCHAR(100) NOT NULL,
    model VARCHAR(100) NOT NULL,
    model_year INT NOT NULL,
    status VARCHAR(50) NOT NULL,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DO $$
DECLARE
    row_count INT;
BEGIN
    SELECT COUNT(*) INTO row_count FROM Cars;

    IF row_count = 0 THEN
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Maserati', 'Spyder', 2003, 'Eliminado');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Honda', 'Insight', 2000, 'Nuevo');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Mercedes-Benz', 'M-Class', 2004, 'Disponible');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Toyota', 'Land Cruiser', 2013, 'Eliminado');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Dodge', 'Durango', 2001, 'Reparación');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Mercedes-Benz', 'SL-Class', 2002, 'Ocupado');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Mercedes-Benz', 'SLK-Class', 2012, 'Reparación');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Mazda', 'Miata MX-5', 1995, 'Desuso');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Chevrolet', 'Suburban 1500', 2009, 'Disponible');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Lincoln', 'Continental Mark VII', 1990, 'Ocupado');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Mercedes-Benz', 'CLK-Class', 2001, 'Desuso');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Jaguar', 'XK', 2006, 'Reparación');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Honda', 'Odyssey', 2008, 'Dañado');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Mitsubishi', 'Montero', 2004, 'Reparación');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Toyota', 'Sequoia', 2011, 'Reparación');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Chevrolet', 'Express 3500', 1998, 'Disponible');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Chevrolet', 'Suburban 1500', 2008, 'Ocupado');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Acura', 'TL', 2011, 'Desuso');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Chevrolet', 'Camaro', 1973, 'Dañado');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Toyota', '4Runner', 1994, 'Reparación');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Jaguar', 'XF', 2010, 'Reparación');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Ford', 'Explorer', 2005, 'Dañado');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Pontiac', 'Grand Prix', 2002, 'Ocupado');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Volvo', 'V40', 2001, 'Nuevo');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Toyota', 'Highlander', 2012, 'Dañado');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Mercury', 'Villager', 1997, 'Desuso');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Volkswagen', 'riolet', 1992, 'Disponible');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Mazda', 'B-Series Plus', 1995, 'Dañado');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('BMW', '745', 2002, 'Eliminado');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Toyota', 'Tercel', 1995, 'Dañado');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Mitsubishi', 'Chariot', 1986, 'Desuso');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Toyota', 'Matrix', 2008, 'Disponible');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Porsche', '911', 2004, 'Reparación');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Ford', 'Explorer', 2000, 'Eliminado');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Ford', 'Club Wagon', 1996, 'Reparación');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Chevrolet', 'Sonic', 2012, 'Nuevo');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Chevrolet', 'Impala', 2008, 'Desuso');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Mitsubishi', 'Challenger', 1998, 'Nuevo');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Pontiac', 'Tempest', 1961, 'Nuevo');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Buick', 'LeSabre', 1986, 'Disponible');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Hyundai', 'Equus', 2011, 'Reparación');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Cadillac', 'CTS', 2011, 'Disponible');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Oldsmobile', 'Toronado', 1992, 'Eliminado');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Jaguar', 'S-Type', 2004, 'Dañado');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Subaru', 'Legacy', 2012, 'Eliminado');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Mercedes-Benz', 'CLS-Class', 2007, 'Desuso');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Lexus', 'LS', 1998, 'Nuevo');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Dodge', 'Avenger', 1999, 'Desuso');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Lotus', 'Esprit', 2004, 'Ocupado');
        INSERT INTO Cars (brand, model, model_year, status) VALUES ('Mercedes-Benz', 'GL-Class', 2008, 'Eliminado');
END IF;
END $$;
