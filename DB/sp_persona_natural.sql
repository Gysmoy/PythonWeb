/* ================================================= */
/* INICIO PROCEDIMIENTOS ALMACENADOS PERSONA_NATURAL */

-- PERSONA_NATURAL -> CREATE == EXEC PERSONA_NATURAL_CREATE 'English'
CREATE PROCEDURE PERSONA_NATURAL_CREATE
@apePater VARCHAR(25),
@apeMater VARCHAR(25),
@nombres VARCHAR(50),
@dni CHAR(8),
@id_servicio INT,
@tel1 VARCHAR(15),
@tel2 VARCHAR(15),
@correo VARCHAR(320),
@direccion VARCHAR(250),
@usuario_creacion INT
AS BEGIN
	INSERT INTO PERSONA_NATURAL (
		apePater, apeMater, nombres, dni, id_servicio, tel1, tel2, correo, direccion, usuario_creacion
	) VALUES (
		@apePater, @apeMater, @nombres, @dni, @id_servicio, @tel1, @tel2, @correo, @direccion, @usuario_creacion
	)
END
GO

-- PERSONA_NATURAL -> READ ALL == EXEC PERSONA_NATURAL_READ_ALL
CREATE PROCEDURE PERSONA_NATURAL_READ_ALL
@usuario INT
AS
	IF @usuario = 1
		SELECT * FROM PERSONA_NATURAL
	ELSE
		SELECT * FROM PERSONA_NATURAL
		WHERE usuario_creacion = @usuario
GO

-- PERSONA_NATURAL -> READ ACTIVES == EXEC PERSONA_NATURAL_READ_ACTIVES
CREATE PROCEDURE PERSONA_NATURAL_READ_ACTIVES
@usuario INT
AS
	IF @usuario = 1
		SELECT * FROM PERSONA_NATURAL
		WHERE estado = 1
	ELSE
		SELECT * FROM PERSONA_NATURAL
		WHERE 
			usuario_creacion = @usuario AND
			estado = 1
GO

-- PERSONA_NATURAL -> READ INACTIVES == EXEC PERSONA_NATURAL_READ_INACTIVES
CREATE PROCEDURE PERSONA_NATURAL_READ_INACTIVES
@usuario VARCHAR(16)
AS
	IF @usuario = 1
		SELECT * FROM PERSONA_NATURAL
		WHERE estado = 0
	ELSE
		SELECT * FROM PERSONA_NATURAL
		WHERE 
			usuario_creacion = @usuario AND
			estado = 0
GO

-- PERSONA_NATURAL -> UPDATE == EXEC PERSONA_NATURAL_UPDATE
CREATE PROCEDURE PERSONA_NATURAL_UPDATE
@id INT,
@apePater VARCHAR(25),
@apeMater VARCHAR(25),
@nombres VARCHAR(50),
@dni CHAR(8),
@id_servicio INT,
@tel1 VARCHAR(15),
@tel2 VARCHAR(15),
@correo VARCHAR(320),
@direccion VARCHAR(250)
AS BEGIN
	UPDATE PERSONA_NATURAL SET
		apePater = @apePater,
		apeMater = @apeMater,
		nombres = @nombres,
		dni = @dni,
		id_servicio = @id_servicio,
		tel1 = @tel1,
		tel2 = @tel2,
		correo = @correo,
		direccion = @direccion
	WHERE id = @id
END
GO

-- ELEIMAR CERVICIO

CREATE PROCEDURE PERSONA_NATURAL_DELETE
@id INT
AS BEGIN
	UPDATE PERSONA_NATURAL
	SET estado = 0
	WHERE id = @id
END
GO

-- ACTIVAR CERVICIO
CREATE PROCEDURE PERSONA_NATURAL_RESTORE
@id CHAR(8)
AS BEGIN
	UPDATE PERSONA_NATURAL
	SET estado = 1
	WHERE id = @id
END
GO