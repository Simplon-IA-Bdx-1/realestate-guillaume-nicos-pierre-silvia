-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le :  mer. 15 jan. 2020 à 15:13
-- Version du serveur :  8.0.13-4
-- Version de PHP :  7.2.24-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `JSUTnsk4Jo`
--

-- --------------------------------------------------------

--
-- Structure de la table `annonces`
--

CREATE TABLE `annonces` (
  `id` int(11) NOT NULL,
  `idannonce` int(11) NOT NULL,
  `typedetransaction` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `position` int(11) NOT NULL,
  `codepostal` int(11) NOT NULL,
  `codeinseed` int(11) NOT NULL,
  `ville` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `etage` tinyint(4) NOT NULL,
  `idtypechauffage` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `idtypecuisine` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `naturebien` tinyint(4) NOT NULL,
  `si_balcon` tinyint(4) NOT NULL,
  `nb_chambres` tinyint(4) NOT NULL,
  `nb_pieces` tinyint(4) NOT NULL,
  `si_sdbain` tinyint(4) NOT NULL,
  `si_sdEau` tinyint(4) NOT NULL,
  `nb_photos` tinyint(4) NOT NULL,
  `prix` smallint(6) NOT NULL,
  `surface` smallint(6) NOT NULL,
  `dpeL` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `dpeC` varchar(10) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `annonces`
--
ALTER TABLE `annonces`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `idannonce` (`idannonce`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `annonces`
--
ALTER TABLE `annonces`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
