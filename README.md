# Télécommande virtuelle pour la box VOO .évasion

Une télécommande virtuelle pour la box .évasion. Ce projet utilise une API développée en Python afin d'envoyer les différentes commandes via le réseau à la box .évasion. Cette application ainsi que [cette API](https://github.com/Vincent-Stragier/voo-tv/tree/main) sont Open Sources.

## Installation

Initialement, l'application est un script Python, donc il sufft d'installer une version de Python (a priori 3.11 ou plus récent) et de lancer le script `remote.py`. L'application n'a été testée que sous Windows.

Une autre option est de [télécharger l'exécutable (Télécommande VOO .évasion ([...]).exe)](https://github.com/Vincent-Stragier/voo-tv-gui/releases/tag/latest) et de le placer dans un dossier d'installation au choix. À la première exécution, le programme va créer un dossier `data` pour stocker les paramètres (dans `config.json`) de l'application. 

## Configuration de la télécommande

Afin de configurer la télécommande vous devez connaître l'addresse IP de votre box .évasion. Pour l'instant vous devez faire cette recherche manuellement, cependant, la box elle même peut afficher ces informations (home > paramètre (roue dentée en haut à droite) > Diagnostics (en bas à gauche) > Diagnostic du réseau > Voir, l'adresse est à droite de `LAN IP address`).

Il suffira ensuite de renseigner l'adresse dans l'interface de la télécommande sous `Settings` (en haut à gauche), `Change settings`, dans le champs `IP address`. Comme depuis la mise à jour vers VOO TV+ il est nécessaire de renseigner le port 38520 et de choisir le protocol HTTP.

Pour l'instant l'interface ne permet l'utilisation que d'une télécommande à la fois.

## Enpacktage du projet (utilisateurs avancés)

Afin de faciliter l'utilisation de cette application (du moins sur Windows), il est possible de générer un exécutable. Pour cela, il suffit d'installer une version de Python (par exemple Python 3.11) et de lancer le script `compile_recipe.py` (`py -3.11 compile_recipe.py`).
