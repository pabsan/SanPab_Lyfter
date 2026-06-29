CREATE TABLE IF NOT EXISTS Usuarios (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    password VARCHAR(255) NOT NULL,
    estado_cuenta BOOLEAN DEFAULT TRUE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DO $$
DECLARE
    row_count INT;
BEGIN
    -- 1. Store the count in a variable
    SELECT COUNT(*) INTO row_count FROM Usuarios WHERE;

    IF row_count = 0 THEN
        INSERT INTO usuarios
(nombre, correo, username, fecha_nacimiento, password, estado_cuenta)
VALUES
('Cathryn Milson', 'cmilson6@disqus.com', 'cmilson6', '1993-11-26', 'jQ9''%KfG', FALSE),
('Ardelia Blevin', 'ablevin7@amazon.de', 'ablevin7', '1990-12-28', 'nQ7@_be''PJ0}', TRUE),
('Chicky Dorton', 'cdorton8@ucoz.com', 'cdorton8', '1991-02-28', 'pN0''r#<8=ui', FALSE),
('Joye Draysey', 'jdrayseyb@huffingtonpost.com', 'jdrayseyb', '1998-01-26', 'cC9\y''&dcU(w$X', TRUE),
('Moishe Messingham', 'mmessinghamh@aboutads.info', 'mmessinghamh', '1993-12-14', 'bO5@,*79LG''/&<,N', TRUE),
('Illa Corbett', 'icorbetti@hibu.com', 'icorbetti', '1997-07-17', 'uH2\</x?B@2va''2', TRUE),
('Sherline Foulser', 'sfoulserj@admin.ch', 'sfoulserj', '1994-05-26', 'xU3''LH/2DuoJCD', FALSE),
('Cari Overill', 'coverilll@tinyurl.com', 'coverilll', '1997-07-28', 'nP1''aqKq(', TRUE),
('Deanna Cowey', 'dcoweyn@amazonaws.com', 'dcoweyn', '1998-03-11', 'zS5=V5|1D3i''#M8', FALSE),
('Korella Izchaki', 'kizchakix@icq.com', 'kizchakix', '1994-05-16', 'wT2~qfh''OTZ~t', FALSE),
('Roda Joska', 'rjoska1c@hexun.com', 'rjoska1c', '1994-12-09', 'aW0?rtSvY|6''1', TRUE);
    END IF;
END $$;