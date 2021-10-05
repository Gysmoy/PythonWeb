USE MANAGE_IT
GO

/* ========================================= */
/* INICIO PROCEDIMIENTOS ALMACENADOS SUBSCRIPCIONES */

-- SUBSCRIPCIONES -> CREATE == EXEC SUBSCRIPCIONES_CREATE 'English'
CREATE PROCEDURE SUBSCRIPCIONES_CREATE
@id_usuario CHAR(8),
@id_proveedor CHAR(8),
@id_ciclo CHAR(8),
@id_moneda CHAR(8),
@monto DECIMAL(5,2),
@fec_inicio DATE,
@prorroga INT
AS BEGIN
	DECLARE @id CHAR(8)
	SELECT @id = 'SUB' + RIGHT('00000' + LTRIM(STR(COUNT(*) + 1)), 5) FROM SUBSCRIPCIONES
	INSERT INTO SUBSCRIPCIONES VALUES (
        @id, @id_usuario, @id_proveedor,
        @id_ciclo, @id_moneda, @monto,
        @fec_inicio, @prorroga, '1'
    )
END
GO

-- SUBSCRIPCIONES -> READ ALL == EXEC SUBSCRIPCIONES_READ_ALL
CREATE PROCEDURE SUBSCRIPCIONES_READ_ALL
AS
	SELECT * FROM SUBSCRIPCIONES
GO

-- SUBSCRIPCIONES -> READ ACTIVES == EXEC SUBSCRIPCIONES_READ_ACTIVES
CREATE PROCEDURE SUBSCRIPCIONES_READ_ACTIVES
AS
	SELECT * FROM SUBSCRIPCIONES WHERE estado = '1'
GO

-- SUBSCRIPCIONES -> READ INACTIVES == EXEC SUBSCRIPCIONES_READ_INACTIVES
CREATE PROCEDURE SUBSCRIPCIONES_READ_INACTIVES
AS
	SELECT * FROM SUBSCRIPCIONES WHERE estado = '0'
GO

-- SUBSCRIPCIONES -> READ ONE == EXEC SUBSCRIPCIONES_READ_ONE
CREATE PROCEDURE SUBSCRIPCIONES_READ_ONE
@id CHAR(8)
AS
	SELECT * FROM SUBSCRIPCIONES WHERE id = @id
GO

-- SUBSCRIPCIONES -> SEARCH == EXEC SUBSCRIPCIONES_SEARCH
CREATE PROCEDURE SUBSCRIPCIONES_SEARCH
@search VARCHAR(12)
AS
	SELECT * FROM SUBSCRIPCIONES WHERE
        id_usuario LIKE(CONCAT('%', @idioma, '%'))
GO

-- SUBSCRIPCIONES -> UPDATE == EXEC SUBSCRIPCIONES_UPDATE
CREATE PROCEDURE SUBSCRIPCIONES_UPDATE
@id		CHAR(8),
@idioma VARCHAR(12),
@estado BIT
AS
	UPDATE SUBSCRIPCIONES SET
	idioma = @idioma,
	estado = @estado
	WHERE id = @id
GO

-- SUBSCRIPCIONES -> CHANGE STATUS == EXEC SUBSCRIPCIONES_CHANGE_STATUS
CREATE PROCEDURE SUBSCRIPCIONES_CHANGE_STATUS
@id CHAR(8)
AS
	DECLARE @estado BIT
	SELECT @estado = estado FROM SUBSCRIPCIONES WHERE id = @id
	IF @estado = 1
		UPDATE SUBSCRIPCIONES SET estado = '0' WHERE id = @id
	ELSE
		UPDATE SUBSCRIPCIONES SET estado = '1' WHERE id = @id
GO

/* FIN PROCEDIMIENTOS ALMACENADOS SUBSCRIPCIONES */
/* ====================================== */