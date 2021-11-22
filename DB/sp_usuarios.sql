/* INICIO PROCEDIMINETO ALMACENADO USUARIOS*/
/* =============================================== */
-- USUARIOS -> CREATE = EXEC == USUARIOS_CREATE
CREATE PROCEDURE USUARIOS_CREATE
@usuario VARCHAR(16),
@correo VARCHAR(320),
@clave CHAR(64),
@dni CHAR(8),
@apePater VARCHAR(15),
@apeMater VARCHAR(15),
@nombres VARCHAR(45),
@sexo CHAR(1),
@fec_nac DATE,
@id_idioma INT
AS BEGIN
    INSERT INTO USUARIOS (
        usuario, correo, clave, dni, apePater, apeMater, nombres, sexo, fec_nac, id_idioma
    ) VALUES (
        @usuario, @correo, @clave, @dni, @apePater, @apeMater, @nombres, @sexo, @fec_nac, @id_idioma
    )
END
GO

-- USUARIOS -> READ ALL = EXEC USUARIOS_READ_ALL
CREATE PROCEDURE USUARIOS_READ_ALL
AS
    SELECT * FROM USUARIOS
GO
-- USUARIOS -> READ ACTIVES == EXEC USUARIOS_READ_ACTIVES
CREATE PROCEDURE USUARIOS_READ_ACTIVES
AS
    SELECT * FROM USUARIOS
    WHERE estado = 1
GO

-- USUARIOS -> READ INACTIVES == EXEC USUARIO_READ_INACTIVES
CREATE PROCEDURE USUARIOS_READ_INACTIVES
AS
    SELECT * FROM USUARIOS
    WHERE estado = 0
GO

-- USUARIOS -> READ ONE == EXEC USUARIOS_READ_ONE
CREATE PROCEDURE USUARIOS_READ_ONE
@id INT
AS BEGIN
    SELECT * FROM USUARIOS
    WHERE id = @id
END
GO
    
-- USUARIOS -> READ USERNAME PASSWORD == EXEC USUARIOS_READ_USERNAME_PASSWORD
CREATE PROCEDURE USUARIOS_VALIDATE
@username CHAR(320),
@password CHAR(64)
AS BEGIN
    SELECT * FROM USUARIOS
    WHERE (
        usuario = @username OR
        correo = @username
    ) AND clave = @password
END
GO

-- USUARIOS -> UPDATE == EXEC USUARIOS_UPDATE
CREATE PROCEDURE USUARIOS_UPDATE
@id INT,
@usuario VARCHAR(16),
@correo VARCHAR(320),
@clave CHAR(64),
@dni CHAR(8),
@apePater VARCHAR(15),
@apeMater VARCHAR(15),
@nombres VARCHAR(45),
@sexo CHAR(1),
@fec_nac DATE,
@id_idioma INT
AS BEGIN
    UPDATE USUARIOS SET
        usuario = @usuario,
        correo = @correo,
        clave = @clave,
        dni = @dni,
        apePater = @apePater,
        apeMater = @apeMater,
        nombres = @nombres,
        sexo = @sexo,
        fec_nac = @fec_nac,
        id_idioma = @id_idioma
    WHERE
        id = @id
END
GO

--USUARIOS -> CHANGE STATUS == EXEC USUARIOS_DELETE
CREATE PROCEDURE USUARIOS_DELETE
@id INT
AS BEGIN
    UPDATE USUARIOS SET estado = 0
    WHERE id = @id
END
GO

--USUARIOS -> CHANGE STATUS == EXEC USUARIOS_RESTORE
CREATE PROCEDURE USUARIOS_RESTORE
@id INT
AS BEGIN
    UPDATE USUARIOS SET estado = 1
    WHERE id = @id
END
GO

CREATE PROCEDURE USUARIOS_VERIFY
@usuario VARCHAR(16),
@clave VARCHAR(64)
AS BEGIN
    SELECT COUNT(*) FROM USUARIOS
    WHERE
        usuario = @usuario AND
        clave = @clave AND
		estado = 1
END
GO
/* FIN PROCEDIMIENTOS ALMACENADOS USUARIOS */
/* ====================================== */