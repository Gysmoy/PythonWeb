USE MANAGE_IT
GO
/* INICIO PROCEDIMINETO ALMACENADO USUARIOS*/
/* =============================================== */

-- USUARIOS -> CREATE = EXEC == USUARIOS_CREATE ''
CREATE PROCEDURE USUARIOS_CREATE
(
    @usuario VARCHAR(16),
    @correo VARCHAR(320),
    @clave CHAR(64),
    @dni CHAR(8),
    @apePater VARCHAR(15),
    @apeMater VARCHAR(15),
    @nombres VARCHAR(45),
    @sexo CHAR(1),
    @fec_nac DATE,
    @id_idioma CHAR(8)
)
AS BEGIN 
    DECLARE @id CHAR(8)
    SELECT @id = 'USR' + RIGHT('00000' + LTRIM(STR(COUNT(*) + 1)), 5) FROM USUARIOS
    INSERT INTO USUARIOS VALUES (@id, @usuario, @correo, @clave, @dni, @apePater, @apeMater, @nombre, @sexo, @fec_nac,@id_idioma, '1')
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
    SELECT * FROM USUARIOS WHERE estado = '1'
GO

-- USUARIOS -> READ INACTIVES == EXEC USUARIO_READ_INACTIVES
CREATE PROCEDURE USUARIOS_READ_INACTIVES
AS
    SELECT * FROM USUARIOS WHERE estado = '0'
GO

-- USUARIOS -> READ ONE == EXEC USUARIOS_READ_ONE
CREATE PROCEDURE USUARIOS_READ_ONE
@id CHAR(8)
AS
    SELECT * FROM USUARIOS WHERE id = @id
GO

-- USUARIOS -> SEARCH = EXEC USUARIOS_SEARCH
CREATE PROCEDURE USUARIOS_SEARCH
@search VARCHAR(50)
AS
    SELECT * FROM USUARIOS WHERE
        usuario LIKE(CONCAT('%', @search, '%')) OR
        correo LIKE (CONCAT('%', @search, '%')) OR
        clave LIKE (CONCAT('%', @search, '%')) OR
        dni LIKE (CONCAT('%', @search, '%')) OR
        apePater LIKE (CONCAT('%', @search, '%')) OR
        apeMater LIKE (CONCAT('%', @search, '%')) OR
        nombre LIKE (CONCAT('%', @search, '%'))
GO

-- USUARIOS -> UPDATE == EXEC USUARIOS_UPDATE
CREATE PROCEDURE USUARIOS_UPDATE

@id CHAR(8),
@usuario VARCHAR(16),
@correo VARCHAR(320),
@clave CHAR(64),
@dni CHAR(8),
@apePater VARCHAR(15),
@apeMater VARCHAR(15),
@nombres VARCHAR(45),
@sexo CHAR(1),
@fec_nac DATE,
@id_idioma CHAR(8),
@estado BIT
AS
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
    id_idioma = @is_idioma,
    estado = @estado
    WHERE id = @id
GO 

--USUARIOS -> CHANGE STATUS == EXEC USUARIOS_CHANGE_STATUS
CREATE PROCEDURE USUARIOS_CHANGE_STATUS
@id CHAR(8)
AS
    DECLARE @estado BIT
    SELECT @estado = estado from USUARIOS WHERE id=@id
    IF @estado = 1
        UPDATE USUARIOS SET estado = '0' WHERE id = @id
    ELSE 
        UPDATE USUARIOS SET estado = '1' WHERE id = @id
GO
/* FIN PROCEDIMIENTOS ALMACENADOS USUARIOS */
/* ====================================== */
