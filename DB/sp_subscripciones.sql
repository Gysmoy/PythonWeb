/* ========================================= */
/* INICIO PROCEDIMIENTOS ALMACENADOS SUBSCRIPCIONES */

-- SUBSCRIPCIONES -> CREATE == EXEC SUBSCRIPCIONES_CREATE 'English'
CREATE PROCEDURE SUBSCRIPCIONES_CREATE
@id_proveedor INT,
@id_ciclo INT,
@id_moneda INT,
@monto DECIMAL(5,2),
@fec_inicio DATE,
@prorroga INT,
@usuario_creacion INT
AS BEGIN
	INSERT INTO SUBSCRIPCIONES (
		id_proveedor, id_ciclo, id_moneda, monto, fec_inicio, prorroga, usuario_creacion
	) VALUES (
        @id_proveedor, @id_ciclo, @id_moneda, @monto, @fec_inicio, @prorroga, @usuario_creacion
    )
END
GO

-- SUBSCRIPCIONES -> READ ALL == EXEC SUBSCRIPCIONES_READ_ALL
CREATE PROCEDURE SUBSCRIPCIONES_READ_ALL
@usuario INT
AS
	IF @usuario = 'admin'
		SELECT * FROM SUBSCRIPCIONES
	ELSE
		SELECT * FROM SUBSCRIPCIONES
		WHERE usuario_creacion = @usuario
GO

-- SUBSCRIPCIONES -> READ ACTIVES == EXEC SUBSCRIPCIONES_READ_ACTIVES
CREATE PROCEDURE SUBSCRIPCIONES_READ_ACTIVES
@usuario INT
AS
	IF @usuario = 'admin'
		SELECT * FROM SUBSCRIPCIONES
		WHERE estado = 1
	ELSE
		SELECT * FROM SUBSCRIPCIONES
		WHERE 
			usuario_creacion = @usuario AND
			estado = 1
GO

-- SUBSCRIPCIONES -> READ INACTIVES == EXEC SUBSCRIPCIONES_READ_INACTIVES
CREATE PROCEDURE SUBSCRIPCIONES_READ_INACTIVES
@usuario VARCHAR(16)
AS
	IF @usuario = 'admin'
		SELECT * FROM SUBSCRIPCIONES
		WHERE estado = 0
	ELSE
		SELECT * FROM SUBSCRIPCIONES
		WHERE 
			usuario_creacion = @usuario AND
			estado = 0
GO

-- SUBSCRIPCIONES -> UPDATE == EXEC SUBSCRIPCIONES_UPDATE
CREATE PROCEDURE SUBSCRIPCIONES_UPDATE
@id INT,
@id_proveedor INT,
@id_ciclo INT,
@id_moneda INT,
@monto DECIMAL(5,2),
@fec_inicio DATE,
@prorroga INT
AS
	UPDATE SUBSCRIPCIONES SET
		id_proveedor = @id_proveedor,
		id_ciclo = @id_ciclo,
		id_moneda = @id_moneda,
		monto = @monto,
		fec_inicio = @fec_inicio,
		prorroga = @prorroga
	WHERE id = @id
GO


-- ELIMINAR SUBSCRIPCION
CREATE PROCEDURE SUBSCRIPCIONES_DELETE
@id INT
AS BEGIN
	UPDATE SUBSCRIPCIONES
	SET estado = 0
	WHERE id = @id
END
GO

-- ACTIVAR SUBSCRIPCION
CREATE PROCEDURE SUBSCRIPCIONES_RESTORE
@id CHAR(8)
AS BEGIN
	UPDATE SUBSCRIPCIONES
	SET estado = 1
	WHERE id = @id
END
GO

/* FIN PROCEDIMIENTOS ALMACENADOS SUBSCRIPCIONES */
/* ====================================== */