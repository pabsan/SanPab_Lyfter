-- =========================
-- Tabla: Usuarios
-- =========================

CREATE TABLE Usuarios (
    IdUsuarios INTEGER PRIMARY KEY AUTOINCREMENT,
    Email VARCHAR(250) UNIQUE NOT NULL CHECK(LENGTH(Email) <=250),
    Nombre VARCHAR(100) NOT NULL CHECK(LENGTH(Nombre) <=100),
    Apellidos VARCHAR(100) NOT NULL CHECK(LENGTH(Apellidos) <100)
);
-- =========================
-- Tabla: Estados_Carrito
-- =========================
CREATE TABLE Estados_Carrito (
    IdEstadoCarrito INTEGER PRIMARY KEY AUTOINCREMENT,
    Descripcion TEXT NOT NULL
);

-- =========================
-- Tabla: Carrito_Compras
-- =========================
CREATE TABLE Carrito_Compras (
    IdCarrito INTEGER PRIMARY KEY AUTOINCREMENT,
    IdUsuario INTEGER NOT NULL,
    FechaCreacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FechaCierre DATETIME,
    IdEstadoCarrito INTEGER NOT NULL,

    FOREIGN KEY (IdUsuario) REFERENCES Usuarios(IdUsuario),
    FOREIGN KEY (IdEstadoCarrito) REFERENCES Estados_Carrito(IdEstadoCarrito)
);

-- =========================
-- Tabla: Detalle_Carrito_Compras
-- =========================
CREATE TABLE Detalle_Carrito_Compras (
    IdCarrito INTEGER,
    CodigoProducto TEXT,
    Cantidad INTEGER NOT NULL CHECK (Cantidad > 0),
    MontoTotal REAL NOT NULL CHECK (MontoTotal >= 0),

    PRIMARY KEY (IdCarrito, CodigoProducto),

    FOREIGN KEY (IdCarrito) REFERENCES Carrito_Compras(IdCarrito),
    FOREIGN KEY (CodigoProducto) REFERENCES Productos(CodigoProducto)
);

-- =========================
-- Tabla: Facturas
-- =========================
CREATE TABLE Facturas (
    NumeroFactura INTEGER PRIMARY KEY AUTOINCREMENT,
    FechaFactura DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CorreoComprador TEXT NOT NULL,
    MontoTotal REAL NOT NULL CHECK (MontoTotal >= 0)
);

-- =========================
-- Tabla: Detalle_Facturas
-- =========================
CREATE TABLE Detalle_Facturas (
    NumeroFactura INTEGER,
    CodigoProducto TEXT,
    Cantidad INTEGER NOT NULL CHECK (Cantidad > 0),
    MontoTotal REAL NOT NULL CHECK (MontoTotal >= 0),

    PRIMARY KEY (NumeroFactura, CodigoProducto),

    FOREIGN KEY (NumeroFactura) REFERENCES Facturas(NumeroFactura),
    FOREIGN KEY (CodigoProducto) REFERENCES Productos(CodigoProducto)
);