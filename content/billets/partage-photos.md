title=Partage de photos entre utilisateurs
date=2016-07-25
tags=photo
status=draft
type=post
~~~~~~

Pour les photos partagées entre plusieurs utilisateurs


Les utilisateurs de ma machine


Imaginons un ordinateur familial partagé par plusieurs utilisateurs. Chaque utilisateur a son compte et ses photos personnelles se trouvent dans son ~/Images.

## Description du problème

Tous les utilisateurs ont de très nombreuses photos communes (évènements familiaux, vacances, etc). Pour éviter la duplication, ils partagent photos communes dans un répertoire partagé (/home/partage/Images)
Chaque utilisateur doit pouvoir importer des photos dans le dossier partagé
L'autre utilisateur verra automatiquement les nouvelles photos dans son logiciel lors du prochain lancement
Pour éviter la duplication de l'effort, le nom de l'album et les éventuelles étiquettes devront aussi être partagées de manière à ce que l'autre utilisateur en profite.

## Contraintes

Les photos doivent être accessibles hors-ligne.

Idéalement :
- l'importation devrait juste demander le nom de l'album puis automatiquement importer toutes les photos dans un dossier au nom de l'album.
- l'album se trouvant dans une arborescence de date :
-- par exemple, l'album "Voyage en Belgique" se trouvera dans l'arborescence "2016/08-aout/Voyage en Belgique"
-- si cela doit être configuré, ca serait bien que cela soit persistant
- les 2 collections (privée et partagée) doivent se gérer depuis la même instance du logiciel (plus pratique à mes yeux)
- le choix de la collection doit se faire au moment de l'importation

# KDE

digikam permet d'entretenir plusieurs collections (album de haut niveau)
mise à jour automatique des collections ?
partage des étiquettes ?
partage des noms d'albums ?



# GNOME
Script d'initilisation (dans ~/bin)
Faire un .desktop dédié
Place this file in the /usr/share/applications directory so that it is accessible by everyone, or in ~/.local/share/applications

https://developer.gnome.org/integration-guide/stable/desktop-files.html.en
