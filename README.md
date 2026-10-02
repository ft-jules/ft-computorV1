# computorV1

Résolution d'équations polynomiales de degré 2 ou moins, en Python, sans
bibliothèque mathématique.

## Utilisation

Python 3, aucune dépendance.

```sh
python3 computor.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
```

```
Reduced form: 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0
Polynomial degree: 2
Discriminant is strictly positive, the two solutions are:
0.9052389907905898
-0.47513146390886934
```

Le programme affiche la forme réduite, le degré et les solutions. Au-dessus du
degré 2, il s'arrête et le signale.

Cas gérés : discriminant nul ou négatif (solutions complexes), degré 0 sans
solution ou avec une infinité de solutions, coefficient nul qui ne compte pas
dans le degré.

## Bonus

```sh
python3 bonus/computor_bonus.py "5 + 4 * X + X^2 = X^2"
```

- forme libre : `5`, `4X`, `X`, `x^2` acceptés dans n'importe quel ordre
- erreurs de syntaxe signalées avec la position du caractère fautif
- solutions rationnelles affichées aussi en fraction réduite
- affichage des étapes du calcul

## Fichiers

```
computor.py          partie obligatoire, autonome
test.sh              tests
setupV1.sh           env de dev (black, flake8), optionnel
bonus/
  computor_bonus.py
  utils.py           parsing, PGCD, fractions, formatage
  test_bonus.sh
```

## Tests

```sh
./test.sh
cd bonus && ./test_bonus.sh
```

Le code passe flake8 sans avertissement.

## Racine carrée

`math.sqrt` et `** 0.5` ne sont pas utilisés. `ft_sqrt` applique la méthode de
Newton a f(x) = x * x - n :

```
x = (x + n / x) / 2
```

Le point de départ est `max(n, 1.0)` : pour n < 1 la racine est plus grande que
n, donc partir de n casserait la décroissance de la suite. Il n'y a pas de
tolérance fixée à la main, on s'arrête quand la suite ne décroît plus, c'est à
dire quand la précision machine est atteinte.