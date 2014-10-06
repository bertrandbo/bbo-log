Title: Mise en place de Pelican
Date: 2014-08-19
Modified: 2014-09-10
Tags: debian, pelican
Summary: Mise en place de Pelican (version 3.4.0) sur ma Debian Wheezy pour mon blog personnel

Je souhaite utiliser [Pelican](http://www.getpelican.com/) pour diffuser facilement mes notes et pense-bêtes.
L'idée est d'avoir quelque chose de léger et facilement versionnable.

## Prélude à l'installation
La version de Python installée sur ma Debian stable correspond au minimum requis (2.7)

	:::console
	bertrand@pc-bbo:~$ ls -l /usr/bin/python
	lrwxrwxrwx 1 root root 9 sept. 28  2013 /usr/bin/python -> python2.7

Avant d'installer Pelican, il faut s'assurer d'avoir installé PIP et virtualenv

	:::console
	$ su -
	# apt-get install python-pip
	# pip install virtualenv

L'installation via `PIP` doit se faire en `root` (ou avec `sudo`) sous peine d'avoir une erreur

	:::console
	`error: could not create '/usr/local/lib/python2.7/dist-packages/virtualenv_support': Permission denied`

## Installation

L'installation de Pelican proprement dite est bien expliquée sur la [documentation officielle](http://docs.getpelican.com/en/3.4.0/install.html)

Comme conseillé, j'installe Pelican (et Markdown) dans un environnement virtuel que je cache dans mon répertoire personnel :

	:::console
	bertrand@pc-bbo:~$ mkdir .virtualenv .virtualenv/pelican
	bertrand@pc-bbo:~$ cd .virtualenv/pelican
	bertrand@pc-bbo:~/.virtualenv/pelican$ virtualenv .
	New python executable in ./bin/python
	Installing setuptools, pip...done.
	bertrand@pc-bbo:~/.virtualenv/pelican$ ls
	bin  include  lib  local
	bertrand@pc-bbo:~/.virtualenv/pelican$ source bin/activate
	(pelican)bertrand@pc-bbo:~/.virtualenv/pelican$ pip install pelican markdown

## Configuration

Une configuration de base est générée grâce au script `pelican-quickstart`. Ce script génère deux fichiers de configuration :
- 1 pour le site en local (`pelicanconf.py`)
- 1 pour le site en ligne (`pelicanpublish.conf`)
Pour le reste, tout est dans la [documentation très complète](http://docs.getpelican.com/en/3.4.0).

Je voulais des URL simplifiée avec une arborescence de date. Par exemple, `http://www.bertrand-bousquet.info/articles/2014/08/13/mise-en-place-pelican`. C'est tout à fait possible grâce aux propriétés `ARTICLE_URL` et `ARTICLE_SAVE_AS`.

Il est aussi possible de faire des archives par année, par mois et même par jour, via les propriétés `YEAR_ARCHIVE_SAVE_AS`, `MONTH_ARCHIVE_SAVE_AS` et `DAY_ARCHIVE_SAVE_AS`. Mais je remets cela à plus tard.

Enfin, niveau thème, il faut cloner le [dépôt git](https://github.com/getpelican/pelican-themes) et modifier la propriété `THEME` du fichier de configuration pour pointer vers le bon. C'est simple, rapide et pratique.

## Utilisation
J'écris mes billets en [Markdown](http://daringfireball.net/projects/markdown/). N'ayant pas besoin d'être plus précis, je ne renseigne la date qu'au jour près (Par exemple `Date: 2014-08-19`). Dans mon cas, renseigner l'heure et la minute me paraissait être de l'overkill. Cela fonctionne sans aucune configuration car Pelican supporte les formats de dates [suggérées par le W3C](http://www.w3.org/TR/NOTE-datetime).

On peut ajouter du code dans les billets via un bloc qui commence par `:::lexer`. . Visiblement, la coloration syntaxique n'implique pas de module supplémentaire (Pygments est suffisant). J'avoue ne pas avoir creusé cette partie pour le moment.

## Génération
Pour générer le site, j'utilise Make plutôt que Fabric. En effet, Make faisant le boulot, je ne voyais pas pourquoi j'allais installer un autre module.

## Et après ?
Sur le dépôt GitHub, l'équipe et les contributeurs de Pelican proposent toute une [série de plugins](https://github.com/getpelican/pelican-plugins) très pratiques, comme par exemple :

- Le plugin gallery couplé au plugin thumbnailer pour faire une belle galerie photo
- Le plugin pelican_comment_system pour gérer les commentaires statiquement et en Markdown.
