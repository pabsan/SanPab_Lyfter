CREATE TABLE IF NOT EXISTS Automoviles (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    marca VARCHAR(100) NOT NULL,
    modelo VARCHAR(100) NOT NULL,
    ano_fabricacion INT NOT NULL,
    estado_auto VARCHAR(50) NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DO $$
DECLARE
    row_count INT;
BEGIN
    SELECT COUNT(*) INTO row_count FROM Automoviles;

    IF row_count = 0 THEN
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Maserati', 'Spyder', 2003, 'Eliminado');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Honda', 'Insight', 2000, 'Nuevo');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Mercedes-Benz', 'M-Class', 2004, 'Activo');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Toyota', 'Land Cruiser', 2013, 'Eliminado');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Dodge', 'Durango', 2001, 'Reparación');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Mercedes-Benz', 'SL-Class', 2002, 'Activo');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Mercedes-Benz', 'SLK-Class', 2012, 'Reparación');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Mazda', 'Miata MX-5', 1995, 'Desuso');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Chevrolet', 'Suburban 1500', 2009, 'Activo');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Lincoln', 'Continental Mark VII', 1990, 'Desuso');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Mercedes-Benz', 'CLK-Class', 2001, 'Desuso');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Jaguar', 'XK', 2006, 'Reparación');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Honda', 'Odyssey', 2008, 'Dañado');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Mitsubishi', 'Montero', 2004, 'Reparación');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Toyota', 'Sequoia', 2011, 'Reparación');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Chevrolet', 'Express 3500', 1998, 'Activo');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Chevrolet', 'Suburban 1500', 2008, 'Eliminado');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Acura', 'TL', 2011, 'Desuso');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Chevrolet', 'Camaro', 1973, 'Dañado');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Toyota', '4Runner', 1994, 'Reparación');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Jaguar', 'XF', 2010, 'Reparación');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Ford', 'Explorer', 2005, 'Dañado');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Pontiac', 'Grand Prix', 2002, 'Reparación');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Volvo', 'V40', 2001, 'Nuevo');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Toyota', 'Highlander', 2012, 'Dañado');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Mercury', 'Villager', 1997, 'Desuso');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Volkswagen', 'riolet', 1992, 'Activo');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Mazda', 'B-Series Plus', 1995, 'Dañado');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('BMW', '745', 2002, 'Eliminado');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Toyota', 'Tercel', 1995, 'Dañado');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Mitsubishi', 'Chariot', 1986, 'Desuso');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Toyota', 'Matrix', 2008, 'Activo');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Porsche', '911', 2004, 'Reparación');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Ford', 'Explorer', 2000, 'Eliminado');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Ford', 'Club Wagon', 1996, 'Reparación');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Chevrolet', 'Sonic', 2012, 'Nuevo');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Chevrolet', 'Impala', 2008, 'Desuso');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Mitsubishi', 'Challenger', 1998, 'Nuevo');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Pontiac', 'Tempest', 1961, 'Nuevo');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Buick', 'LeSabre', 1986, 'Activo');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Hyundai', 'Equus', 2011, 'Reparación');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Cadillac', 'CTS', 2011, 'Activo');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Oldsmobile', 'Toronado', 1992, 'Eliminado');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Jaguar', 'S-Type', 2004, 'Dañado');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Subaru', 'Legacy', 2012, 'Eliminado');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Mercedes-Benz', 'CLS-Class', 2007, 'Desuso');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Lexus', 'LS', 1998, 'Nuevo');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Dodge', 'Avenger', 1999, 'Desuso');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Lotus', 'Esprit', 2004, 'Nuevo');
        INSERT INTO vehiculos (marca, modelo, ano, estado) VALUES ('Mercedes-Benz', 'GL-Class', 2008, 'Eliminado');
    END IF;
END $$;
