CREATE TABLE IF NOT EXISTS lyfter_car_rental.Users (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    born_date DATE NOT NULL,
    password VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DO $$
DECLARE
    row_count INT;
BEGIN
    SELECT COUNT(*) INTO row_count FROM lyfter_car_rental.Users;

    IF row_count = 0 THEN
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Coriss Withey', 'cwithey0@cbc.ca', 'cwithey0', DATE '2001-02-17', 'iQ3xPVtI1', 'Inactivo');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Federico McCanny', 'fmccanny1@diigo.com', 'fmccanny1', DATE '2007-04-08', 'mF38w#+qC`', 'Activo');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Drake Whight', 'dwhight2@reddit.com', 'dwhight2', DATE '1988-09-15', 'dJ5*%!yg7J7cO', 'Eliminado');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Lin Hakking', 'lhakking3@edublogs.org', 'lhakking3', DATE '2026-02-02', 'jV2J''syW5', 'Activo');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Dulcinea Piken', 'dpiken4@ihg.com', 'dpiken4', DATE '2007-12-21', 'tD9`htS"~+''P', 'Inactivo');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Blondell Trenear', 'btrenear5@netvibes.com', 'btrenear5', DATE '2011-09-25', 'mD1N4?em''l', 'Inactivo');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Josey Bozward', 'jbozward6@umn.edu', 'jbozward6', DATE '2007-08-13', 'oQ5K9DZ+', 'Inactivo');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Rutger Hanby', 'rhanby7@columbia.edu', 'rhanby7', DATE '1994-11-27', 'bB1Jbw?k', 'Inactivo');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Rudolph Gaiter', 'rgaiter8@icio.us', 'rgaiter8', DATE '2005-09-26', 'bL7<>}HiZ', 'Eliminado');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Donn Twycross', 'dtwycross9@github.com', 'dtwycross9', DATE '2019-08-18', 'iJ2{1s>Xco!}\T', 'Eliminado');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Fidela Measor', 'fmeasora@sfgate.com', 'fmeasora', DATE('2002-10-16'), 'pZ0yr3we_@)k%.', 'Eliminado');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Ewart Syphus', 'esyphusb@ustream.tv', 'esyphusb', DATE '2005-02-02', 'dH4/!x*&,Js',('Inactivo'));
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Berk Corps', 'bcorpsc@paginegialle.it',('bcorpsc'), DATE('2005-10-24'),('lP7L7hF(BzS`{w'),('Eliminado'));
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Sergent Bordiss', 'sbordissd@forbes.com', 'sbordissd', DATE '2009-02-28', 'xH3dxV@W"1xf', 'Activo');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Jarvis Vedeneev', 'jvedeneeve@pen.io', 'jvedeneeve', DATE '2014-01-11', 'zO02gLSJ|Mxj!{}M', 'Eliminado');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Mylo Docket', 'mdocketf@51.la', 'mdocketf', DATE '2013-08-21', 'qL0<2~Qz%KC>&u8s', 'Inactivo');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Ingar Liepina', 'iliepinag@webs.com', 'iliepinag', DATE '2005-11-03', 'kG7lt2Je,&TL', 'Activo');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Maggi Klimke', 'mklimkeh@hugedomains.com', 'mklimkeh', DATE '2004-07-29', 'rF0K_''D@OHGP+ec', 'Eliminado');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Ertha Utting', 'euttingi@ca.gov', 'euttingi', DATE '2017-04-28', 'fX6P#G\J1<aD3B', 'Inactivo');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Misty Vinsen', 'mvinsenj@moonfruit.com', 'mvinsenj', DATE '1994-12-29', 'eV1jstfIS', 'Eliminado');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Elene O''Suaird', 'eosuairdk@phoca.cz', 'eosuairdk', DATE '1995-10-31', 'vB0_Z})=Um_)', 'Eliminado');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Torry Hanvey', 'thanveyl@sciencedirect.com', 'thanveyl', DATE '2018-07-10', 'vI0Ld(E|eCJh$1f', 'Eliminado');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Niall Gittis', 'ngittism@howstuffworks.com', 'ngittism', DATE '2021-12-08', 'cY1djg?0', 'Inactivo');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Emmey Sherlock', 'esherlockn@furl.net', 'esherlockn', DATE '2011-05-04', 'gV8Kz`&_sm&', 'Inactivo');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Mohammed Bris', 'mbriso@ted.com', 'mbriso', DATE '1996-02-02', 'xY1sbfq>/?', 'Eliminado');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Velvet Iglesias', 'viglesiasp@posterous.com', 'viglesiasp', DATE '2004-07-13', 'fJ8l.P+,mYh>XF', 'Activo');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Marilyn Mee', 'mmeeq@ca.gov', 'mmeeq', DATE '2025-03-11', 'kX0<~t\<)j0%>TU', 'Activo');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Calli Ranscomb', 'cranscombr@ucla.edu', 'cranscombr', DATE '1993-09-20', 'jN6oW(Qh)DTm', 'Activo');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Tonya Gabbidon', 'tgabbidons@people.com.cn', 'tgabbidons', DATE '2018-07-20', 'kN9bUQ_J', 'Eliminado');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Gabey Neilan', 'gneilant@cnbc.com', 'gneilant', DATE '1988-08-07', 'bU8Y3dqA\>%=', 'Eliminado');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Ulrich Mandrey', 'umandreyu@google.de', 'umandreyu', DATE '2002-10-29', 'iM87EPbeg$Ar6', 'Activo');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Kiersten Eyton', 'keytonv@microsoft.com', 'keytonv', DATE '2024-07-22', 'mS2l7<ims', 'Inactivo');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Raphael Domelaw', 'rdomelaww@goodreads.com', 'rdomelaww', DATE '2018-12-18', 'bB3=?+=b&O9~=', 'Eliminado');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Gerhardine Lawlor', 'glawlorx@reverbnation.com', 'glawlorx', DATE '2026-01-04', 'yN5''C+<%3jxTek', 'Eliminado');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Etty Whitton', 'ewhittony@samsung.com', 'ewhittony', DATE '2000-08-26', 'nW83''UusdXcA', 'Activo');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Scarlet Cauldfield', 'scauldfieldz@networkadvertising.org', 'scauldfieldz', DATE '2015-10-28', 'jU4!HLT`}S=<k3q', 'Inactivo');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Lorrie Revance', 'lrevance10@chronoengine.com', 'lrevance10', DATE '2007-11-23', 'lX7XaF4`mU#d', 'Eliminado');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Trix Daile', 'tdaile11@cyberchimps.com', 'tdaile11', DATE '2015-06-10', 'tL8~2Z>BHC.}jLf', 'Inactivo');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Rahal Stairmand', 'rstairmand12@yellowpages.com', 'rstairmand12', DATE '1993-06-28', 'uR3K+_>wgXgX_YN', 'Inactivo');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Lars Westmerland', 'lwestmerland13@dmoz.org', 'lwestmerland13', DATE '2016-03-02', 'qR1|0~q5', 'Inactivo');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Davide Tregido', 'dtregido14@hud.gov', 'dtregido14', DATE '2008-12-28', 'yF9BjU\*#u=~1K', 'Activo');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Otho Badini', 'obadini15@miibeian.gov.cn', 'obadini15', DATE '2003-04-02', 'kK742,(&x_idt8', 'Eliminado');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Kelbee Dericot', 'kdericot16@mac.com', 'kdericot16', DATE '2003-07-25', 'rG2JtIo/GGk9~=C@', 'Activo');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Thacher Nutten', 'tnutten17@issuu.com', 'tnutten17', DATE '2025-01-11', 'pO3X5_ICE', 'Eliminado');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Robinet Goodoune', 'rgoodoune18@smugmug.com', 'rgoodoune18', DATE '2020-10-29', 'iR6d<N2GWuSn.t{', 'Inactivo');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Kass Done', 'kdone19@ihg.com', 'kdone19', DATE '2024-07-10', 'xC5XZr=''?', 'Eliminado');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Averyl Wilcock', 'awilcock1a@army.mil', 'awilcock1a', DATE '2020-06-04', 'eJ6kh"VlihR', 'Eliminado');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Inga Melmar', 'imelmar1b@google.co.uk', 'imelmar1b', DATE '2013-05-11', 'yO8`03X(Q9', 'Eliminado');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Bail Braidford', 'bbraidford1c@deliciousdays.com', 'bbraidford1c', DATE '2006-01-17', 'dE5wE%8RuI*', 'Eliminado');
        INSERT INTO lyfter_car_rental.Users (name, email, username, born_date, password, status) VALUES ('Adelind Rouch', 'arouch1d@java.com', 'arouch1d', DATE '2022-11-22', 'pW4wCQ.3Z%<bs', 'Eliminado');    
    END IF;
END $$;
