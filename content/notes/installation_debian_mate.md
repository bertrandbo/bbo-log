Title: Installer Mate sur Debian
Date: 2014-09-01
Modified: 2014-09-17
Tags: debian, wheezy, mate
Slug: installer-mate-debian
Summary: Installation d'une Debian 7 minimale avec le bureau Mate 1.8

L'idée est d'installer un petit environnement de travail sans prétention sur une machine assez ancienne et peu puissante (mono-coeur 1.8 GHz et 512 Mo de RAM)
Je me suis arrêté sur le bureau [Mate](http://mate-desktop.org/) et la distribution [Debian](https://www.debian.org/index.fr.html).

## Installation de Debian

A partir de l'[ISO d'installation réseau](https://www.debian.org/CD/netinst/), je réalise une installation minimale de Debian 7.6 *i.e.* j'enlève tout sauf les utilitaires systèmes. Je crée mes 3 partitions `/`, `/home` et `swap`. N'étant pas fan du `sudo`, je crée mon `root`.

L'installateur semi-graphique est vraiment bien fait et très facile à utiliser. L'installation se passe sans problèmes. J'ai configuré le miroir de l'[université de Picardie](http://ftp.u-picardie.fr) qui s'avère être très réactif.

### Activation des dépôts
Mate est désormais disponible dans les `backport` de Debian. Ainsi, les [instructions](http://backports.debian.org/Instructions/) nous disent qu'il suffit d'ajouter le dépôt dans ses sources . A l'aide de `nano` en `root`, j'ajoute dans `/etc/apt/sources.list` la ligne `deb http://http.debian.net/debian wheezy-backports main`

### Installation
Après sauvegarde, mettre à jour la liste des paquets, puis installer :

- le système de fenêtrage X Window et sa documentation (ca peut toujours servir et ca coute pas plus cher),
- le gestionnaire d'affichage (*Display Manager* en anglais) ; je suis les conseils des forums en partant sur LightDM et non pas sur SliM (utilisé par CrunchBang notamment)
- le bureau Mate avec les extras et PulseAudio plutôt que GStreamer

Ce qui nous donne :

	:::console
	# apt-get update
	# apt-get install xorg xorg-docs
	# apt-get install ligthdm accountsservice upower
	# apt-get install mate-desktop-environment-extra mate-media-pulse

Pas besoin de passer des options particulières à `APT` car je souhaite l'installation des paquets recommandés par les mainteneurs Debian et leurs paquets suggérés ne m'intéressent pas, sauf dans le cas de LightDM où les paquets suggérés me paraissaient intéressants (`accountsservice` et `upower`). Mais l'option `--install-suggests` de `APT` étant récursive, on se retrouve avec des dizaines de paquets à installer...  Donc, il faut installer les paquets recommandés à la main.

On finit par un redémarrage de la machine :

	:::console
	# shutdown -r now

### Configuration de Mate
Le comportement par défaut de Mate me convient. Je ne configure que deux choses :

- Le magnetisme des fenêtres (_Centre de contrôle > Fenêtres > Placement > Activer la mosaique côte à côte_) : cela redimensionne la fenêtre pour prendre la moitié de l'écran quand on glisse la fenêtre contre le bord de l'écran
- Le simple clic pour ouvrir les éléménts (_Centre de contrôle > Gestion de fichiers > Comportement_)

Si ma machine avait été plus puissante, j'aurai également activé la composition pour le gestionnaire de fenêtre (_Centre de contrôle > Fenêtres > Général_) car c'est quand même plus joli.

## Logiciels

J'installe ensuite les logiciels qu'il me manque :

- Firefox (qui s'appelle IceWeasel chez Debian) comme navigateur web
- Exaile comme lecteur de musique (avec l'icone de controle dans la zone de notification) : 
- Totem et MPlayer (juste au cas où) comme lecteurs de vidéos et de DVD
- gFTP comme client FTP
- Brasero comme logiciel de gravure
- LibreOffice (avec l'aide en francais) pour la bureautique

L'installation en console se passe comme suit :

	:::console
	# apt-get install iceweasel exaile python-eggtrayicon totem gnome-player gftp brasero
	# apt-get install libreoffice-{write, calc, impress} libreoffice-help-fr

### Codecs multimédia
Jusqu'à présent, le système restait libre (je n'ai pas activé les dépôts `non-free` et `contrib`). Mais plusieurs de mes fichiers vidéos et mes DVD n'étaient pas lisibles par le système. J'ai donc activé les [dépôts multimédia de Debian](https://wiki.debian.org/fr/MultimediaCodecs).

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
