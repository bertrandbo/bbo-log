title=Désactiver le pavé tactile sur Mate
date=2014-09-03
modified=2014-09-11
tags=mate, debian, wheezy
slug=desactiver-touchpad-mate
summary=Comment désactiver le touchpad sur Mate 1.8 ?
status=published
type=post
~~~~~~

Depuis les préférences de Mate (Souris > Pavé tactile), il est seulement possible de le désactiver pendant la frappe. Pour le désactiver complètement, cela peut se faire pour la session utilisateur courante à l'aide d'une propriété `dconf`.

Ouvrir `dconf-editor` puis déplier l'arbre jusqu'à `org.mate.desktop.peripherals.touchpad`. Décocher `touchpad.enabled`. Le changement est pris en compte immédiatement.

