CREATE TABLE IF NOT EXISTS Rentas (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    usuario_id INT NOT NULL,
    automovil_id INT NOT NULL,

    fecha_renta DATE NOT NULL,
    fecha_devolucion DATE,
    estado_renta VARCHAR(50) NOT NULL,

    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_rentas_usuario
        FOREIGN KEY (usuario_id)
        REFERENCES Usuarios(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_rentas_automovil
        FOREIGN KEY (automovil_id)
        REFERENCES Automoviles(id)
        ON DELETE CASCADE
);
