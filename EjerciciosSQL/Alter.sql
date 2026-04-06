ALTER TABLE Facturas 
ADD COLUMN TelefonoComprador TEXT CHECK(length(TelefonoComprador) >= 8);

ALTER TABLE Facturas 
ADD COLUMN CodigoEmpleado INTEGER NOT NULL DEFAULT 0;