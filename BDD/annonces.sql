-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le :  lun. 20 jan. 2020 à 13:48
-- Version du serveur :  8.0.13-4
-- Version de PHP :  7.2.24-0ubuntu0.18.04.2

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
  `position` int(11) DEFAULT NULL,
  `codepostal` int(11) DEFAULT NULL,
  `codeinsee` int(11) DEFAULT NULL,
  `ville` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `etage` tinyint(4) DEFAULT NULL,
  `idtypechauffage` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `idtypecuisine` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `naturebien` tinyint(4) DEFAULT NULL,
  `si_balcon` tinyint(4) DEFAULT NULL,
  `nb_chambres` tinyint(4) DEFAULT NULL,
  `nb_pieces` tinyint(4) DEFAULT NULL,
  `si_sdbain` tinyint(4) DEFAULT NULL,
  `si_sdEau` tinyint(4) DEFAULT NULL,
  `nb_photos` tinyint(4) DEFAULT NULL,
  `prix` int(11) NOT NULL,
  `surface` smallint(6) DEFAULT NULL,
  `dpeL` varchar(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `dpeC` varchar(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `description` text COLLATE utf8_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `annonces`
--

INSERT INTO `annonces` (`id`, `idannonce`, `position`, `codepostal`, `codeinsee`, `ville`, `etage`, `idtypechauffage`, `idtypecuisine`, `naturebien`, `si_balcon`, `nb_chambres`, `nb_pieces`, `si_sdbain`, `si_sdEau`, `nb_photos`, `prix`, `surface`, `dpeL`, `dpeC`, `description`) VALUES
(1, 12345, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1234, NULL, NULL, NULL, NULL);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
