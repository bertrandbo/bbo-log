Title: Installation de Mate 1.8 sur Debian 7
Date: 2014-09-01
Tags: debian, wheezy, mate
Summary: Installation pas-à-pas d'une Debian 7 minimale avec le bureau Mate 1.8

L'idée est d'installer un petit environnement de travail sans prétention sur une machine assez ancienne et peu puissante (mono-coeur 1.8 GHz et 512 Mo de RAM)
Je me suis arrêté sur le bureau [Mate](http://mate-desktop.org/) et la distribution [Debian](https://www.debian.org/index.fr.html).

## Installation de Debian

A partir de l'[ISO d'installation réseau](https://www.debian.org/CD/netinst/), je réalise une installation minimale de Debian 7.6 *i.e.* j'enlève tout sauf les utilitaires systèmes. Je crée mes 3 partitions `/`, `/home` et `swap`. N'étant pas fan du `sudo`, je crée mon `root`.

L'installateur semi-graphique est vraiment bien fait et très facile à utiliser. L'installation se passe sans problèmes. J'ai configuré le miroir de l'[université de Picardie](http://ftp.u-picardie.fr) qui s'avère être très réactif.

## Installation de Mate

Pas besoin de passer des options particulières à `APT` car je souhaite l'installation des paquets recommandés par les mainteneurs Debian et leurs paquets suggérés ne m'intéressent pas.

### Activation des dépôts
Mate est désormais disponible dans les `backport` de Debian. Ainsi, les [instructions](http://backports.debian.org/Instructions/) nous disent qu'il suffit d'ajouter le dépôt dans ses sources . A l'aide de `nano` en `root`, j'ajoute dans `/etc/apt/sources.list` la ligne

	:::console
	deb http://http.debian.net/debian wheezy-backports main

Après sauvegarde, mettre à jour la liste des paquets

	:::console
	# apt-get update

### Système de fenêtrage X
J'installe X Window et sa documentation (ca peut toujours servir et ca coute pas plus cher)

	:::console
	# apt-get install xorg xorg-docs

### Gestionnaire d'affichage
Comme gestionnaire d'affichage (*Display Manager* en anglais), je suis les conseils des forums en partant sur LightDM et non pas sur SliM (utilisé par CrunchBang notamment). Dans ce cas précis, les paquets suggérés me paraissaient intéressants (`accountsservice` et `upower`). Mais l'option `--install-suggests` de `APT` étant récursive, on se retrouve avec des dizaines de paquets à installer...  Donc, on les installe à la main :

	:::console
	# apt-get install ligthdm accountsservice upower

### Bureau Mate
Enfin, j'installe le bureau avec les extras

	:::console
	# apt-get install mate-desktop-environment-extra

Mate n'utilise pas PulseAudio par défaut, mais GStreamer. Je passe à PulseAudio :

	:::console
	# apt-get install mate-media-pulse

Cela supprime le paquet `mate-media-gstreamer` et installe automatiquement un applet de son dans la zone de notification. Je conclus cette installation fraiche par un redémarrage :

	:::console
	# shutdown -r now

### Configuration de Mate
Le comportement par défaut de Mate me convient. Je ne configure que deux choses :
- Le magnetisme des fenêtres (Centre de contrôle > Fenêtres > Placement > Activer la mosaique côte à côte) : cela redimensionne la fenêtre pour prendre la moitié de l'écran quand on glisse la fenêtre contre le bord de l'écran
- Le simple clic pour ouvrir les éléménts (Centre de contrôle > Gestion de fichiers > Comportement)

Si ma machine avait été plus puissante, j'aurai également activé la composition pour le gestionnaire de fenêtre (Centre de contrôle > Fenêtres > Général) car c'est quand même plus joli.

## Logiciels

J'installe ensuite les logiciels qu'il me manque :
- Firefox (qui s'appelle IceWeasel chez Debian) comme navigateur web
- Exaile comme lecteur de musique (avec l'icone de controle dans la zone de notification) : 
- Totem et MPlayer (juste au cas où) comme lecteurs de vidéos et de DVD
- gFTP comme client FTP
- Brasero comme logiciel de gravure
- LibreOffice (avec l'aide en francais) pour la bureautique

	:::console
	# apt-get install iceweasel exaile python-eggtrayicon totem gnome-player gftp brasero
	# apt-get install libreoffice-{write, calc, impress} libreoffice-help-fr

### Codecs multimédia
Jusqu'à présent, le système restait libre (je n'ai pas activé les dépôts `non-free` et `contrib`). Mais plusieurs de mes fichiers vidéos et mes DVD n'étaient pas lisibles par le système. J'ai donc activé les [dépôts multimédia de Debian] (https://wiki.debian.org/fr/MultimediaCodecs).

En suivant la doc, j'ai juste installé

	:::console
	# apt-get install libdvdcss2 w32codecs

J'ajouterai juste que l'installation de la clef en ligne de commande se fait comme suit

	:::console
	# wget http://deb-multimedia.org/pool/main/d/deb-multimedia-keyring/deb-multimedia-keyring_2012.05.10-dmo4_all.deb 
	# dpkg -i deb-multimedia-keyring_2012.05.10-dmo4_all.deb

### Nettoyage
Je finis par un nettoyage des paquets téléchargés

	:::console
	# apt-get autoclean
