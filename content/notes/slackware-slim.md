title=Installer SLiM sur Slackware
date=2014-09-27
modified=2014-10-06
tags=slackware,slim
summary=Installer SLiM sur Slackware 14.1
status=published
type=post
~~~~~~

Pour remplacer XDM, j'ai choisi SLiM (utilisé notamment, par [Crunchbang](http://crunchbang.org/)). La [documentation francophone de slackware](http://wiki.slackware-fr.org/xwindow:articles:slim) couvre l'essentiel pour installer et configurer SLiM.

Je n'ai juste pas fait l'installation à la main comme indiqué dans la documentation (i.e. `make install`). J'ai préféré utiliser le [SlackBuild disponible pour ma version](http://slackbuilds.org/repository/14.1/system/slim/).

J'utilise le [thème SLiM de ngc891](http://ngc891.blogdns.net/?p=74).

## Points d'attention

Par défaut, slackware est configuré en clavier `us`. SLiM sera donc en `qwerty`. Il faut penser à changer la [disposition du clavier par défaut du système](http://docs.slackware.com/howtos:window_managers:keyboard_layout#keyboard_layout_in_x).

Lors du login, obtenir le message `failed to execute login command` signifie que le fichier `.xinitrc` n'existe pas dans le répertoire utilisateur. Dans ce cas, copier celui du compte `root`.
