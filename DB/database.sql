USE MASTER
GO

IF DB_ID('MANAGE_IT') IS NOT NULL
	DROP DATABASE MANAGE_IT
GO

CREATE DATABASE MANAGE_IT
GO

USE MANAGE_IT
GO

CREATE TABLE SERVICIOS
(
    id CHAR(8),
    servicio VARCHAR(45),
    estado BIT,
    CONSTRAINT pk_servicio PRIMARY KEY (id)
);
GO

CREATE TABLE PERSONA_NATURAL
(
    id CHAR(8),
    apePater VARCHAR(15),
    apeMater VARCHAR(15),
    nombres VARCHAR(45),
    dni CHAR(8),
    id_servicio CHAR(8),
    tel1 VARCHAR(15),
    tel2 VARCHAR(15),
    correo VARCHAR(320),
    direccion VARCHAR(250),
    estado BIT,
    CONSTRAINT pk_persona_natural PRIMARY KEY (id),
    CONSTRAINT fk_persona_natural_servicio FOREIGN KEY (id_servicio) REFERENCES SERVICIOS (id),
    CONSTRAINT ck_persona_natural_dni CHECK(dni LIKE('[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')),
);
GO

CREATE TABLE PERSONA_JURIDICA
(
    id CHAR(8),
    razonSocial VARCHAR(250),
    ruc CHAR(11),
    id_servicio CHAR(8),
    tel1 VARCHAR(15),
    tel2 VARCHAR(15),
    correo VARCHAR(320),
    direccion VARCHAR(320),
    estado BIT,
    CONSTRAINT pk_persona_juridica PRIMARY KEY (id),
    CONSTRAINT fk_persona_juridica_servicio FOREIGN KEY (id_servicio) REFERENCES SERVICIOS (id),
    CONSTRAINT ck_persona_juridica_ruc CHECK(ruc LIKE('[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')),
);
GO

CREATE TABLE PROVEEDORES
(
    id CHAR(8),
    tipo CHAR(1),
    id_per_nat CHAR(8),
    id_per_jur CHAR(8),
    estado BIT,
    CONSTRAINT pk_proveedor PRIMARY KEY (id),
    CONSTRAINT fk_proveedor_persona_juridica FOREIGN KEY (id_per_jur) REFERENCES PERSONA_JURIDICA (id),
    CONSTRAINT fk_proveedor_persona_natural FOREIGN KEY (id_per_nat) REFERENCES PERSONA_NATURAL (id),
    CONSTRAINT ck_proveedor_tipo CHECK(tipo IN('N','J')),
);
GO

CREATE TABLE IDIOMAS
(
    id CHAR(8),
    idioma VARCHAR(12),
    estado BIT,
    CONSTRAINT pk_idioma PRIMARY KEY (id)
);
GO

CREATE TABLE USUARIOS
(
    id CHAR(8),
    usuario VARCHAR(16),
    correo VARCHAR(320),
    clave CHAR(64),
    dni CHAR(8),
    apePater VARCHAR(15),
    apeMater VARCHAR(15),
    nombres VARCHAR(45),
    sexo CHAR(1),
    fec_nac DATE,
    id_idioma CHAR(8),
    estado BIT,
    CONSTRAINT pk_usuario PRIMARY KEY (id),
    CONSTRAINT fk_usuario_idioma FOREIGN KEY (id_idioma) REFERENCES  IDIOMAS(id),
    CONSTRAINT ck_usuario_dni CHECK(dni LIKE('[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')),
    CONSTRAINT ck_usuario_sexo CHECK(sexo IN('M','F')),
    CONSTRAINT ck_usuario_fec_nac CHECK (fec_nac < GETDATE()),
    CONSTRAINT uk_usuario_correo UNIQUE(correo),

);
GO

CREATE TABLE MONEDAS
(
    id CHAR(8),
    modeda VARCHAR(12),
    estado BIT,
    CONSTRAINT pk_monedas PRIMARY KEY (id),
);
GO

CREATE TABLE CICLOS
(
    id CHAR(8),
    tipo VARCHAR(15),
    ciclo INT,
    estado BIT,
    CONSTRAINT pk_ciclo PRIMARY KEY (id),
);
GO

CREATE TABLE SUBSCRIPCIONES
(
    id CHAR(8),
    id_usuario CHAR(8),
    id_proveedor CHAR(8),
    id_ciclo CHAR(8),
    id_moneda CHAR(8),
    monto DECIMAL(5,2),
    fec_inicio DATE,
    prorroga INT,
    estado BIT,
    CONSTRAINT pk_subscripcion PRIMARY KEY (id),
    CONSTRAINT fk_subscripcion_usuario FOREIGN KEY (id_usuario) REFERENCES USUARIOS(id),
    CONSTRAINT fk_subscripcion_proveedor FOREIGN KEY (id_proveedor) REFERENCES PROVEEDORES(id),
    CONSTRAINT fk_subscripcion_ciclo FOREIGN KEY (id_ciclo) REFERENCES CICLOS(id),
    CONSTRAINT fk_subscripcion_moneda FOREIGN KEY (id_moneda) REFERENCES CICLOS(id),
);
GO

CREATE TABLE HISTORIALES
(
    id CHAR(11),
    id_usuario CHAR(8),
    id_proveedor CHAR(8),
    monto DECIMAL(5,2),
    fecha DATE,
    CONSTRAINT pk_historial PRIMARY KEY (id),
    CONSTRAINT fk_historial_usuario FOREIGN KEY (id_usuario) REFERENCES USUARIOS(id),
    CONSTRAINT fk_historial_proveedor FOREIGN KEY (id_proveedor) REFERENCES PROVEEDORES(id),
);
GO