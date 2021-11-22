/* ================================================= */
/* INICIO PROCEDIMIENTOS ALMACENADOS PERSONA_JURIDICA */

-- PERSONA_JURIDICA -> CREATE == EXEC PERSONA_JURIDICA_CREATE 'English'
CREATE PROCEDURE PERSONA_JURIDICA_CREATE
@razonSocial VARCHAR(250),
@ruc CHAR(11),
@id_servicio INT,
@tel1 VARCHAR(15),
@tel2 VARCHAR(15),
@correo VARCHAR(320),
@direccion VARCHAR(320),
@usuario_creacion VARCHAR(16)
AS BEGIN
	INSERT INTO PERSONA_JURIDICA (
		razonSocial, ruc, id_servicio, tel1, tel2, correo, direccion, usuario_creacion
	) VALUES (
		@razonSocial, @ruc, @id_servicio, @tel1, @tel2, @correo, @direccion, @usuario_creacion
	)
END
GO

-- PERSONA_JURIDICA -> READ ALL == EXEC PERSONA_JURIDICA_READ_ALL
CREATE PROCEDURE PERSONA_JURIDICA_READ_ALL
@usuario VARCHAR(16)
AS
	IF @usuario = 'admin'
		SELECT * FROM PERSONA_JURIDICA
	ELSE
		SELECT * FROM PERSONA_JURIDICA
		WHERE usuario_creacion = @usuario
GO

-- PERSONA_JURIDICA -> READ ACTIVES == EXEC PERSONA_JURIDICA_READ_ACTIVES
CREATE PROCEDURE PERSONA_JURIDICA_READ_ACTIVES
@usuario VARCHAR(16)
AS
	IF @usuario = 'admin'
		SELECT * FROM PERSONA_JURIDICA
		WHERE estado = 1
	ELSE
		SELECT * FROM PERSONA_JURIDICA
		WHERE 
			usuario_creacion = @usuario AND
			estado = 1
GO

-- PERSONA_JURIDICA -> READ INACTIVES == EXEC PERSONA_JURIDICA_READ_INACTIVES
CREATE PROCEDURE PERSONA_JURIDICA_READ_INACTIVES
@usuario VARCHAR(16)
AS
	IF @usuario = 'admin'
		SELECT * FROM PERSONA_JURIDICA
		WHERE estado = 0
	ELSE
		SELECT * FROM PERSONA_JURIDICA
		WHERE 
			usuario_creacion = @usuario AND
			estado = 0
GO

-- PERSONA_JURIDICA -> UPDATE == EXEC PERSONA_JURIDICA_UPDATE
CREATE PROCEDURE PERSONA_JURIDICA_UPDATE
@id INT,
@razonSocial VARCHAR(250),
@ruc CHAR(11),
@id_servicio INT,
@tel1 VARCHAR(15),
@tel2 VARCHAR(15),
@correo VARCHAR(320),
@direccion VARCHAR(320)
AS BEGIN
	UPDATE PERSONA_JURIDICA SET
		razonSocial = @razonSocial,
		ruc = @ruc,
		id_servicio = @id_servicio,
		tel1 = @tel1,
		tel2 = @tel2,
		correo = @correo,
		direccion = @direccion
	WHERE id = @id
END
GO

-- ELEIMAR CERVICIO

CREATE PROCEDURE PERSONA_JURIDICA_DELETE
@id INT
AS BEGIN
	UPDATE PERSONA_JURIDICA
	SET estado = 0
	WHERE id = @id AND usuario_creacion = @usuario 
END
GO

-- ACTIVAR CERVICIO
CREATE PROCEDURE PERSONA_JURIDICA_RESTORE
@id CHAR(8)
AS BEGIN
	UPDATE PERSONA_JURIDICA
	SET estado = 1
	WHERE id = @id
END
GO