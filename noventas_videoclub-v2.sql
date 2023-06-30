-- Active: 1688166046626@@codo-a-codo-linuxeros.clfcnl4qjyxz.sa-east-1.rds.amazonaws.com@3306
CREATE DATABASE CineCode
    DEFAULT CHARACTER SET = 'utf8mb4';

use CineCode;

CREATE TABLE `carrito` (
  `IdCarrito` int(11) NOT NULL,
  `IdCliente` int(11) DEFAULT NULL,
  `IdPeliculas` int(11) DEFAULT NULL,
  `Cantidad` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `clientes` (
  `IdCliente` int(11) NOT NULL,
  `Nombre` varchar(30) DEFAULT NULL,
  `Apellido` varchar(30) DEFAULT NULL,
  `Direccion` varchar(30) DEFAULT NULL,
  `Email` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `peliculas` (
  `IdPeliculas` int(11) NOT NULL,
  `Nombre` varchar(30) DEFAULT NULL,
  `Genero` varchar(30) DEFAULT NULL,
  `Año` int(4) DEFAULT NULL,
  `Stock` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

ALTER TABLE `carrito`
  ADD PRIMARY KEY (`IdCarrito`),
  ADD KEY `IdCliente` (`IdCliente`),
  ADD KEY `IdPeliculas` (`IdPeliculas`);


ALTER TABLE `clientes`
  ADD PRIMARY KEY (`IdCliente`);

ALTER TABLE `peliculas`
  ADD PRIMARY KEY (`IdPeliculas`);


ALTER TABLE `carrito`
  MODIFY `IdCarrito` int(11) NOT NULL AUTO_INCREMENT;


ALTER TABLE `clientes`
  MODIFY `IdCliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;


ALTER TABLE `peliculas`
  MODIFY `IdPeliculas` int(11) NOT NULL AUTO_INCREMENT;


ALTER TABLE `carrito`
  ADD CONSTRAINT `carrito_ibfk_1` FOREIGN KEY (`IdPeliculas`) REFERENCES `peliculas` (`IdPeliculas`),
  ADD CONSTRAINT `carrito_ibfk_2` FOREIGN KEY (`IdCliente`) REFERENCES `clientes` (`IdCliente`);


COMMIT;