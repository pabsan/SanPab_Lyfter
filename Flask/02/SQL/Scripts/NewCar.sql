CREATE OR REPLACE PROCEDURE NewCar(
    p_marca VARCHAR(100),
    p_modelo VARCHAR(100),
    p_ano_fabricacion INT,
    p_estado_auto VARCHAR(50)
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM Automoviles
        WHERE marca = p_marca AND modelo = p_modelo AND ano_fabricacion = p_ano_fabricacion AND estado_auto = p_estado_auto
    ) THEN
        INSERT INTO Automoviles (marca, modelo, ano_fabricacion, estado_auto)
        VALUES (p_marca, p_modelo, p_ano_fabricacion, p_estado_auto);
    END IF;
    COMMIT;
END;
$$;


