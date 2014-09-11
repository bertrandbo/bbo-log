Title: Désactiver le touchpad sur Mate 1.8
Date: 2014-09-03 10:00
Tags: mate, debian, wheezy
Slug: desactiver-touchpade-mate
Summary: Comment désactiver le touchpad sur Mate 1.8 ?

J'ai un problème : le curseur saute tout seul de ligne en ligne et de colonnes en colonnes. En gros, le curseur vit sa vie un peu comme il l'entend. C'est assez pénible.

Je prends l'hypothèse que cela vient du touchpad. Je décide de le désactiver pour vérifier. Cele peut facilement se faire pour la session utilisateur courante à l'aide d'une propriété `dconf`.

Ouvrir `dconf-editor` puis déplier l'arbre jusqu'à `org.mate.desktop.peripherals.touchpad`. Décocher `touchpad.enabled`. Le changement est pris en compte immédiatement.

Bilan : c'est mieux mais il arrive encore au curseur de sauter.

