CREATE DATABASE ProyectoIntegrador;
USE ProyectoIntegrador;

CREATE TABLE Estudiante (
    matricula VARCHAR (20) PRIMARY KEY,
    nombre VARCHAR(100),
    correo VARCHAR(100) UNIQUE,
    contraseña VARCHAR(100)
);

CREATE TABLE Ejercicio (
    idEjercicio INT PRIMARY KEY,
    descripcion TEXT,
    resuelto BOOLEAN
);

CREATE TABLE Quiz (
    idQuiz INT PRIMARY KEY,
    resuelto BOOLEAN
);

CREATE TABLE Estudiante_Ejercicio (
    matricula VARCHAR (20),
    idEjercicio INT,
    PRIMARY KEY (matricula, idEjercicio),
    FOREIGN KEY (matricula) REFERENCES Estudiante(matricula),
    FOREIGN KEY (idEjercicio) REFERENCES Ejercicio(idEjercicio)
);

CREATE TABLE Estudiante_Quiz (
    matricula VARCHAR (20),
    idQuiz INT,
    PRIMARY KEY (matricula, idQuiz),
    FOREIGN KEY (matricula) REFERENCES Estudiante(matricula),
    FOREIGN KEY (idQuiz) REFERENCES Quiz(idQuiz)
);