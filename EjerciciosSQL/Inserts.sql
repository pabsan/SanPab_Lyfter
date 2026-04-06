-- =========================
-- Estados_Carrito
-- =========================
INSERT INTO Estados_Carrito (Descripcion) VALUES 
('Abierto'),
('Cerrado'),
('Cancelado');

-- =========================
-- Usuarios
-- =========================
INSERT INTO Usuarios (Email, Nombre, Apellidos) VALUES
('juan@email.com', 'Juan', 'Perez'),
('maria@email.com', 'Maria', 'Lopez'),
('carlos@email.com', 'Carlos', 'Sanchez');

-- =========================
-- Productos (CodigoProducto INTEGER)
-- =========================
INSERT INTO Productos (CodigoProducto, Nombre, Precio, Marca) VALUES
(1, 'Laptop', 850.00, 'Dell'),
(2, 'Mouse', 25.50, 'Logitech'),
(3, 'Teclado', 45.00, 'HP'),
(4, 'Monitor', 220.00, 'Samsung');

INSERT INTO Productos (Nombre, Precio, Marca) VALUES
('MacBook',100000.00,'Apple');


-- =========================
-- Carrito_Compras
-- =========================
INSERT INTO Carrito_Compras (IdUsuario, IdEstadoCarrito, FechaCierre) VALUES
(1, 1, NULL),  -- Abierto
(2, 2, '2026-03-25 10:30:00'), -- Cerrado
(3, 3, '2026-03-20 15:00:00'); -- Cancelado

-- =========================
-- Detalle_Carrito_Compras
-- =========================
INSERT INTO Detalle_Carrito_Compras (IdCarrito, CodigoProducto, Cantidad, MontoTotal) VALUES
(1, 1, 1, 850.00),
(1, 2, 2, 51.00),
(2, 3, 1, 45.00),
(2, 4, 2, 440.00),
(3, 2, 1, 25.50);

-- =========================
-- Facturas
-- =========================
INSERT INTO Facturas (CorreoComprador, MontoTotal, TelefonoComprador, CodigoEmpleado) VALUES
('juan@email.com', 901.00, '88887777', 101),
('maria@email.com', 485.00, '89998888', 102);

-- =========================
-- Detalle_Facturas
-- =========================
INSERT INTO Detalle_Facturas (NumeroFactura, CodigoProducto, Cantidad, MontoTotal) VALUES
(1, 1, 1, 850.00),
(1, 2, 2, 51.00),
(2, 3, 1, 45.00),
(2, 4, 2, 440.00);
