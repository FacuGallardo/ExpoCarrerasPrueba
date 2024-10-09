CREATE DATABASE IF NOT EXISTS isaui;
USE isaui;

CREATE TABLE IF NOT EXISTS carreras (
  id_carreras INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(45) NOT NULL,
  PRIMARY KEY (id_carreras)
);

CREATE TABLE IF NOT EXISTS personas (
  id_persona INT NOT NULL AUTO_INCREMENT,
  apellido VARCHAR(45) NOT NULL,
  nombre VARCHAR(45) NOT NULL,
  dni VARCHAR(45) NOT NULL,
  telefono VARCHAR(45),
  correo VARCHAR(45),
  domicilio VARCHAR(45),
  ciudad VARCHAR(45),
  instagram VARCHAR(45),
  id_carreras INT NOT NULL,
  PRIMARY KEY (id_persona),
  FOREIGN KEY (id_carreras) REFERENCES carreras(id_carreras)
);
