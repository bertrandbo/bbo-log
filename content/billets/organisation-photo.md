Title: Gestion de ma phototèque
Date: 2016-07-28
Modified: 2016-10-06
Tags: photo

_Note : article commencé cet été mais jamais publié car jamais considéré comme terminé. Est-il plus terminé maintenant, je ne sais pas. Mais au moins il est publié..._

Dans le [dernier numéro de Compétence Photo](http://www.competencephoto.com/Competence-Photo-Numero-53-en-kiosque-le-30-juin-2016_a2817.html), un article traite du catalogage de ses photos.

Je saisi la balle au bond pour partager ma manière de faire. Je précise que 95% de mes photos sont de la photo de famille/photo souvenir et que je shoote en JPEG.

## Stratégie

Je range mes photos à deux endroits :

- Dans le répertoire Images de mon compte pour les photos personnelles, de sorties, d'essais, etc. Au risque d'enfoncer une porte ouverte, ce répertoire n'est accessible que par moi.
- Dans un répertoire partagé pour les photos familiales/communes. Il est accessible par tous les utilisateurs de l'ordinateur

L'avantage d'avoir deux endroits permet à chaque utilisateur de conserver son espace privé tout en évitant la duplication des photos communes.

## Logiciel

Je suis un utilisateur de [Shotwell](https://wiki.gnome.org/Apps/Shotwell). Il me permet d'importer les photos dans mon répertoire personnel ou dans le répertoire partagé en fonction de la série.

## Arborescence

Comme l'auteur de l'article, j'ai choisi une arborescence par date et non par thème. Après avoir essayé il y a quelques années une arborescence à 2 niveaux _année-mois/jour_, le volume important de dossiers m'a fait passé il y a plusieurs mois sur une arborescence à 3 niveaux _année/mois/jour_. 

Pour illustrer mon arborescence, une photo du 27 juillet 2016 sera placée dans le dossier _2016/07-juillet/2016-07-27_.

Quelques précisions :

- J'aime bien voir le mois écrit de toute lettre (un TOC peut-être ?). Je préfixe avec le numéro pour que les mois soient correctement classés dans mon navigateur de fichier
- Le dossier du jour contient aussi l'année et le mois car cela facilite l'export du dossier, sur clef USB par exemple (cela évite de se retrouver avec un 27.zip sur la clef).

## Renommage

Contrairement à l'auteur, je ne renomme pas mes dossiers importés pour ajouter l'évènement. Pourtant, je pense que ca serait pratique d'avoir l'info à ce niveau là.

Je ne renomme pas non plus les photos. Elles conservent le nom donné par l'appareil. Comme j'importe souvent plusieurs évènements d'un coup, cela me permet juste de laisser le logiciel faire automatiquement le rangement.

Il faudrait cependant que je vérifie si Shotwell a une fonction de renommage de masse.

## Etiquettes

Shotwell possède une fonctionnalité "basique" d'étiquettage des photos. Son seul inconvénient est de ne pas être capable de hiérarchiser les mot-clefs. Je tag les lieux et les personnes principales. Si je faisais plus de séries, j'utiliserai aussi les tag pour décrire le thème.

L'article m'a fait prendre conscience que je devrais plus utilisé les champs standard IPTC. Notamment pour le lieu.

Je configure Shotwell pour écrire les étiquettes dans les données IPTC des photos. Cela me permet de ne décrire les photos qu'une fois et que l'information soit partagées par tous les utilisateurs de la machine.

## Sauvegardes

Je sauvegarde mes photos sur disque externe à l'aide de [rsync](https://rsync.samba.org/). Rustique mais assez efficace.
