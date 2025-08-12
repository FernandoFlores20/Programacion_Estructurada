-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-08-2025 a las 22:54:52
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_casino`
--
CREATE DATABASE IF NOT EXISTS `bd_casino` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `bd_casino`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `id_cliente` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `telefono` bigint(10) NOT NULL,
  `domicilio` varchar(40) NOT NULL,
  `status` varchar(8) NOT NULL,
  `genero` varchar(1) NOT NULL,
  `membresia` varchar(8) NOT NULL,
  `dinero` decimal(10,2) NOT NULL,
  `contraseña` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`id_cliente`, `nombre`, `telefono`, `domicilio`, `status`, `genero`, `membresia`, `dinero`, `contraseña`) VALUES
(1, 'ADMIN', 6181696301, 'CALLE VECINA #123', 'M', 'A', 'VIP', 1001.00, 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),
(2, 'FERNANDO', 6183223010, 'CASA', 'M', 'A', 'VIP', 1000.00, 'b3a8e0e1f9ab1bfe3a36f231f676f78bb30a519d2b21e6c530c0eee8ebb4a5d0'),
(3, 'ERIK AQUINO', 6182223344, 'CALLE TACOS #843', 'ACTIVO', 'M', 'ESTANDAR', 1000.00, '35a9e381b1a27567549b5f8a6f783c167ebf809f1c4d6a9e367240484d8ce281'),
(4, 'PEPE', 6181112233, 'CASA', 'ACTIVO', 'M', 'VIP', 1000.00, '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `juegos`
--

CREATE TABLE `juegos` (
  `id_juego` int(11) NOT NULL,
  `nombre` varchar(25) NOT NULL,
  `tipo` varchar(15) NOT NULL,
  `descripcion` varchar(250) NOT NULL,
  `estado` varchar(8) NOT NULL,
  `id_cliente` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `juegos`
--

INSERT INTO `juegos` (`id_juego`, `nombre`, `tipo`, `descripcion`, `estado`, `id_cliente`) VALUES
(1, 'BLACKJACK', 'CARTAS', 'Juego de cartas donde el objetivo es sumar 21 puntos o lo más cercano posible sin pasarse. Cada jugador compite contra el crupier. Las cartas numéricas valen su número, las figuras valen 10, y el As vale 1 u 11.', 'ACTIVO', 2),
(2, 'POKER', 'CARTAS', 'El jugador compite contra el crupier, usando las reglas básicas del póker para formar la mejor mano de 5 cartas', 'INACTIVO', 1),
(3, 'RULETA', 'MESA', 'Juego de azar con una rueda giratoria con casillas numeradas del 0 al 36. Se apuesta al número, color (rojo/negro), par/impar, etc.', 'ACTIVO', 1),
(4, 'TRAGAPERRAS', 'MAQUINA', 'Máquinas con carretes giratorios que muestran símbolos. El jugador gira y gana si aparecen combinaciones específicas.', 'ACTIVO', 2),
(5, 'BACCARAT', 'CARTAS', 'Juego de cartas donde se apuesta por quién tendrá la mano más cercana a 9 puntos: el jugador, la banca, o un empate. Solo se usan las unidades de la suma total (ej. 14 = 4).', 'ACTIVO', 2),
(6, 'TRAGAPERRAS', 'MAQUINA', 'tragaperras 2', 'ACTIVO', 2);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id_cliente`),
  ADD UNIQUE KEY `telefono` (`telefono`);

--
-- Indices de la tabla `juegos`
--
ALTER TABLE `juegos`
  ADD PRIMARY KEY (`id_juego`),
  ADD KEY `id_cliente` (`id_cliente`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id_cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `juegos`
--
ALTER TABLE `juegos`
  MODIFY `id_juego` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `juegos`
--
ALTER TABLE `juegos`
  ADD CONSTRAINT `juegos_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
