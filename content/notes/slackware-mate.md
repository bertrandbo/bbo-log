Title: Installer Mate sur Slackware
Tags: slackware, mate, slim
Date: 2014-09-29
Modified: 2014-10-06
Summary: Installer Mate 1.8 sur Slackware 14.1

Basé sur mon installation [Slackware 14.1 + XFCE]({filename}slackware.md), je souhaitais profiter de Mate. Une petite équipe de développeurs proposent [un SlackBuild et une version compilée de Mate](http://mateslackbuilds.github.io/). L'avantage de cette solution est qu'elle se base sur les packages disponibles dans l'installation de base. Contrairement à [MLED](http://www.microlinux.fr/mled.php) qui, à une époque, [se basait sur Mate](http://linuxfr.org/news/mled-passe-de-xfce-a-mate). Mais certains paquets du système de base étaient recompilés par le mainteneur. Je trouve cela moins pratique.

## Installation

J'avais installé `slackpkg` pour gérer les mises à jour de mon système plus facilement. Comme `slackpkg` ne gère qu'un seul dépôt, j'ai installé l'extension [slackpkg+](http://slakfinder.org/slackpkg+.html) pour pouvoir gérer le multi-dépôts et ajouter celui de [Mate](http://slackware.org.uk/msb/14.1/1.8/x86/). En `root`, on installe Mate et ses extras :

	:::console
	# slackpkg upgrade gpg
	# slackpkg update
	# slackpkg install SLACKPKGPLUS_msb/base/*
	# slackpkg install SLACKPKGPLUS_msb/extra/*

## Lancement

Pour lancer Mate à la connexion, il faut éditer le fichier `.xinitrc` (lancé par SLiM lors de la connexion). Il faut remplacer les appels à `/usr/bin/startxfce4` par `/usr/bin/mate-session`

Enfin, on peut paramétrer Mate comme environnement par défaut dans le fichier de configuration de SLiM, `/etc/slim.conf` :

	:::console
	sessions            mate-session,xfce4,icewm-session,wmaker,blackbox

## Points d'attention

Sur une slackware par défaut, Mate sera en anglais avec un clavier `qwerty`. Si l'anglais ne pose pas de problème, il est possible de juste changer la disposition du clavier en passant _Control Center > Keyboard > Layouts_ (ajouter le clavier francais et supprimer le clavier américain).

Pour avoir la totale sans forcer, il suffit de [franciser slackware]({filename}slackware.md).
