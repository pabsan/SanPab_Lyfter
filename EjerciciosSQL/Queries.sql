--Obtenga todos los productos almacenados
SELECT * 
FROM Productos;
--Obtenga todos los productos que tengan un precio mayor a 50000
SELECT * 
FROM Productos
WHERE Precio > 50000;
--Obtenga todas las compras de un mismo producto por id.
SELECT f.NumeroFactura, p.Nombre, df.Cantidad, df.MontoTotal
FROM Detalle_Facturas df
JOIN Facturas f ON df.NumeroFactura = f.NumeroFactura
JOIN Productos p ON df.CodigoProducto = p.CodigoProducto
WHERE df.CodigoProducto = 2;
--Obtenga todas las compras agrupadas por producto, donde se muestre el total comprado entre todas las compras.
SELECT 
    p.CodigoProducto,
    p.Nombre,
    SUM(df.Cantidad) AS TotalCantidad,
    SUM(df.MontoTotal) AS TotalVendido
FROM Detalle_Facturas df
JOIN Productos p ON df.CodigoProducto = p.CodigoProducto
GROUP BY p.CodigoProducto, p.Nombre;
--Obtenga todas las facturas realizadas por el mismo comprador
SELECT *
FROM Facturas
WHERE CorreoComprador = 'juan@email.com';
--Obtenga todas las facturas ordenadas por monto total de forma descendente
SELECT *
FROM Facturas
ORDER BY MontoTotal DESC;
--Obtenga una sola factura por número de factura.
SELECT f.NumeroFactura, f.CorreoComprador, p.Nombre, df.Cantidad, df.MontoTotal
FROM Facturas f
JOIN Detalle_Facturas df ON f.NumeroFactura = df.NumeroFactura
JOIN Productos p ON df.CodigoProducto = p.CodigoProducto
WHERE f.NumeroFactura = 1;