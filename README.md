# abelian_sandpile
Programme Python simulant le fonctionnement des tas de sable abéliens grâce à une grille de boutons utilisant TKinter(2021-2022)

## **Règles du modèle**

La grille est composée de 441 tas (21x21) représentés par des boutons.
Chaque case a une valeur.
Lorsqu'un tas a une valeur supérieur à 4, il va s'écrouler.
En s'écroulant, la valeur du tas va diminuer de 4 grains de sable et les quatre tas adjacents vont voir leur nombre grains augmenter de 1.

## **Utilisations du modèle**

Ce modèle est utilisé par des scientifiques pour étudier un phénomène appelé la **criticité auto-organisée**. (http://fr.scienceaq.com/Autres/1001105763.htm)
Il est aussi assez esthétique car lorsque l'on déroule l'algorithme avec un grand nombre de tas et de grains, une fractale peut en résulter.
