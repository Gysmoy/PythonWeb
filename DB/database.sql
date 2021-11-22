USE MASTER
GO

IF DB_ID('MANAGEIT-DB') IS NOT NULL
	DROP DATABASE 'MANAGEIT-DB'
GO

CREATE DATABASE 'MANAGEIT-DB'
GO

USE 'MANAGEIT-DB'
GO

CREATE TABLE SERVICIOS
(
    id INT IDENTITY NOT NULL,
    servicio VARCHAR(250),
    estado BIT DEFAULT '1',
    CONSTRAINT pk_servicio PRIMARY KEY (id)
);
GO

CREATE TABLE IDIOMAS
(
    id INT IDENTITY NOT NULL,
    idioma VARCHAR(12),
    estado BIT DEFAULT '1',
    CONSTRAINT pk_idioma PRIMARY KEY (id)
);
GO

CREATE TABLE USUARIOS
(
    id INT IDENTITY NOT NULL,
    usuario VARCHAR(16),
    correo VARCHAR(320),
    clave CHAR(64),
    dni CHAR(8),
    apePater VARCHAR(15),
    apeMater VARCHAR(15),
    nombres VARCHAR(45),
    sexo CHAR(1),
    fec_nac DATE,
    id_idioma INT NOT NULL,
    estado BIT DEFAULT '1',
    CONSTRAINT pk_usuario PRIMARY KEY (id),
    CONSTRAINT fk_usuario_idioma FOREIGN KEY (id_idioma) REFERENCES  IDIOMAS(id),
    CONSTRAINT ck_usuario_dni CHECK(dni LIKE('[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')),
    CONSTRAINT ck_usuario_sexo CHECK(sexo IN('M','F')),
    CONSTRAINT ck_usuario_fec_nac CHECK (fec_nac < GETDATE()),
    CONSTRAINT uk_usuario_correo UNIQUE(correo)
);
GO

CREATE TABLE PERSONA_NATURAL
(
    id INT IDENTITY NOT NULL,
    apePater VARCHAR(25),
    apeMater VARCHAR(25),
    nombres VARCHAR(50),
    dni CHAR(8),
    id_servicio INT,
    tel1 VARCHAR(15),
    tel2 VARCHAR(15),
    correo VARCHAR(320),
    direccion VARCHAR(250),
    usuario_creacion INT NOT NULL,
    estado BIT DEFAULT '1',
    CONSTRAINT pk_persona_natural PRIMARY KEY (id),
    CONSTRAINT fk_persona_natural_servicio FOREIGN KEY (id_servicio) REFERENCES SERVICIOS (id),
    CONSTRAINT ck_persona_natural_dni CHECK(dni LIKE('[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')),
);
GO

CREATE TABLE PERSONA_JURIDICA
(
    id INT IDENTITY NOT NULL,
    razonSocial VARCHAR(250),
    ruc CHAR(11),
    id_servicio INT,
    tel1 VARCHAR(15),
    tel2 VARCHAR(15),
    correo VARCHAR(320),
    direccion VARCHAR(320),
    usuario_creacion INT NOT NULL,
    estado BIT DEFAULT '1',
    CONSTRAINT pk_persona_juridica PRIMARY KEY (id),
    CONSTRAINT fk_persona_juridica_servicio FOREIGN KEY (id_servicio) REFERENCES SERVICIOS (id),
    CONSTRAINT ck_persona_juridica_ruc CHECK(ruc LIKE('[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')),
);
GO

CREATE TABLE PROVEEDORES
(
    id INT IDENTITY NOT NULL,
    tipo CHAR(1),
    id_per_nat INT,
    id_per_jur INT,
    usuario_creacion INT NOT NULL,
    estado BIT DEFAULT '1',
    CONSTRAINT pk_proveedor PRIMARY KEY (id),
    CONSTRAINT fk_proveedor_persona_juridica FOREIGN KEY (id_per_jur) REFERENCES PERSONA_JURIDICA (id),
    CONSTRAINT fk_proveedor_persona_natural FOREIGN KEY (id_per_nat) REFERENCES PERSONA_NATURAL (id),
    CONSTRAINT ck_proveedor_tipo CHECK(tipo IN('N','J')),
    CONSTRAINT fk_proveedor_usuario FOREIGN KEY (usuario_creacion) REFERENCES USUARIOS (id)
);
GO



CREATE TABLE MONEDAS
(
    id INT IDENTITY NOT NULL,
    moneda VARCHAR(12) NOT NULL,
    cambio DECIMAL(7, 2) NOT NULL,
    estado BIT DEFAULT '1',
    CONSTRAINT pk_monedas PRIMARY KEY (id),
);
GO

CREATE TABLE CICLOS
(
    id INT IDENTITY NOT NULL,
    tipo VARCHAR(15),
    ciclo INT,
    estado BIT DEFAULT '1',
    CONSTRAINT pk_ciclo PRIMARY KEY (id),
);
GO

CREATE TABLE SUBSCRIPCIONES
(
    id INT IDENTITY NOT NULL,
    id_proveedor INT,
    id_ciclo INT,
    id_moneda INT,
    monto DECIMAL(5,2),
    fec_inicio DATE,
    prorroga INT,
    usuario_creacion INT NOT NULL,
    estado BIT DEFAULT '1',
    CONSTRAINT pk_subscripcion PRIMARY KEY (id),
    CONSTRAINT fk_subscripcion_usuario FOREIGN KEY (usuario_creacion) REFERENCES USUARIOS(id),
    CONSTRAINT fk_subscripcion_proveedor FOREIGN KEY (id_proveedor) REFERENCES PROVEEDORES(id),
    CONSTRAINT fk_subscripcion_ciclo FOREIGN KEY (id_ciclo) REFERENCES CICLOS(id),
    CONSTRAINT fk_subscripcion_moneda FOREIGN KEY (id_moneda) REFERENCES CICLOS(id),
);
GO

CREATE TABLE HISTORIALES
(
    id INT IDENTITY NOT NULL,
    id_proveedor INT,
    monto DECIMAL(5,2),
    fecha DATE DEFAULT GETDATE(),
    usuario_creacion INT NOT NULL,
    CONSTRAINT pk_historial PRIMARY KEY (id),
    CONSTRAINT fk_historial_usuario FOREIGN KEY (usuario_creacion) REFERENCES USUARIOS(id),
    CONSTRAINT fk_historial_proveedor FOREIGN KEY (id_proveedor) REFERENCES PROVEEDORES(id),
);
GO