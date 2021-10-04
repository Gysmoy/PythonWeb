USE MANAGE_IT
GO

/* ================================================= */
/* INICIO PROCEDIMIENTOS ALMACENADOS CICLOS */

-- PERSONA_NATURAL -> CREATE == EXEC CICLOS_CREATE 'MENSUAL'
CREATE PROCEDURE CICLOS_CREATE
@id CHAR(8),
@tipo VARCHAR(15),
@ciclo INT
AS BEGIN
    DECLARE @id CHAR(8)
    SELECT @id = 'CLC' + RIGHT('00000' + LTRIM(STR(COUNT(*) + 1)) FROM CICLOS
    INSERT INTO CICLOS VALUES (
        @id, @tipo, @ciclo, @estado, '1'
    )
END
GO

/* wa hacer algunas cosas ya lo termino al rato */

