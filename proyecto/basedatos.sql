
/* Crear la base de datos si esta no existe*/
CREATE DATABASE IF NOT EXISTS master_python;

/*Usar la base de datos creada*/
use master_python;

/*TABLA USUARIO*/
CREATE TABLE usuarios(
    id          int(25) auto_increment not null,
    nombre      varchar(100),
    apellidos   varchar(255),
    email       varchar(255) not null,
    password    varchar(255) not null,
    fecha       date not null,
    /*Restricciones*/
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    /* NO SE REPITA*/
    CONSTRAINT uq_email UNIQUE(email)
    /*MANTENER LA INTEGRIDAD*/
)ENGINE = InnoDB;

/*TABLA DE NOTAS*/
CREATE TABLE notas(
    id          int(25) auto_increment not null,
    /* relacion en usuario */
    usuario_id  int(25) not null,
    titulo      varchar(255) not null,
    descripcion MEDIUMTEXT,
    fecha       date not null,
    /* Restricciones*/
    CONSTRAINT pk_notas PRIMARY KEY(id),
    /*Relacion*/
    CONSTRAINT fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE = InnoDB;
