
========================================================
Description

========================================================

Cette application réalise l'analyse des données issues de plusieurs céréals.
Voici sa structure:

-data
 --	input:              contient les données d'entrée
 --	output:             contient les résultats de sortie

-DataAnalyser
 --	data_viz.py:        module de visualisation
 --	statistics.py:      module de statistique descriptive

-data_loader.py:        module de chargement de vérification des données

-app.py:                script principal de l'application
-__main__:               script de lancement de l'application


========================================================
Déploiement de l'application

========================================================

Préparer l'environnement:
	Construire un environnement virtuel de "Python 3.7", l'activer, puis y installer l'ensemble des packages nécéssaires avec: pip install -r requirement.txt

Télécharcher l'appli:
	Télécharcher / Copier le dépôt de l'application "CerealAnalysis-repo" 

Lancer l'appliction:
	Depuis un terminal, se placer dans le dépôt de l'appli
	Excécuter la commande suivante: Env_cereal CerealAnalysis (si Env_cereal est l'env. créé)

