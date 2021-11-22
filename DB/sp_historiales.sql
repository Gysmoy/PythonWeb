/* ========================================= */
/* INICIO PROCEDIMIENTOS ALMACENADOS HISTORIALES */

-- HISTORIALES -> CREATE == EXEC HISTORIALES_CREATE 'English'
CREATE PROCEDURE HISTORIALES_CREATE
@id_proveedor INT,
@monto DECIMAL(5,2),
@usuario_creacion INT
AS BEGIN
	INSERT INTO HISTORIALES (
        id_proveedor, monto, fecha, usuario_creacion
	) VALUES (
        @id_proveedor, @monto, GETDATE(), @usuario_creacion
    )
END
GO

-- HISTORIALES -> READ ALL == EXEC HISTORIALES_READ_ALL
CREATE PROCEDURE HISTORIALES_READ_ALL
@usuario INT
AS
	IF @usuario = 'admin'
		SELECT * FROM HISTORIALES
	ELSE
		SELECT * FROM HISTORIALES
		WHERE usuario_creacion = @usuario
GO