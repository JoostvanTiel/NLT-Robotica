---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Hoofdstuk 5: Condities en loops

## operatoren
Om condities te kunnen checken worden de volgende operatoren gebruikt:

| Operator | Naam                      | Voorbeeld |
|:---------|:--------------------------|:----------|
| ==       | Gelijk aan                | x == y    |
| !=       | Niet gelijk aan           | x != y    |
| >        | Groter dan                | x > y     |
| <        | Kleiner dan               | x < y     |
| >=       | Groter dan of gelijk aan  | x >= y    |
| <=       | Kleiner dan of gelijk aan | x <= y    |

## if statements

	if conditie:
		instructies...
	elif andere_conditie: # optioneel
		instructies...
	else:		      # optioneel
		instructies...

```{code-cell} ipython3
:tags: [ifStatement]

x = 8
y = 5

if x < y:
	print("y is groter dan x.")
elif x == y:
	print("y is gelijk aan x.")
else:
	print("x is groter dan y.")
```

Meerdere condities tegelijk checken

| Operator | Beschrijving                                                          | Voorbeeld             |
|:---------|:----------------------------------------------------------------------|:----------------------|
| and      | Retourneert `True` als beide condities waar zijn.                     | x < 5 and y > 10      |
| or       | Retourneert `True` als één van beide condities waar is.               | x < 5 or y > 10       |
| not      | Keert het resultaat om, retourneert `False` als het resultaat waar is.| not(x < 5 and y > 10) |

Bijvoorbeeld:
```{code-cell} ipython3
:tags: [ifStatement]

x = 3
y = 6
z = 9

if x < y and y < z:
	print("x is het kleinste getal.")

if x > y and z > y:
	print("y is het kleinste getal.")
elif x > y or z > y:
	print("y is niet het grootste getal.")

if z < y and z < x:
	print("z is het kleinste getal.")
elif not(z < y and z < x):
	print("z is het grootste getal.")
```

## while loops

	while conditie:
		instructies...

```{code-cell} ipython3
:tags: [whileLoop]

done = False
n = 0

while not done:
	if n >= 10:
		done = True
	else: 
		print(n)
		n = n + 1
```

## for loops

	for x in range(getal):
		instructies...

```{code-cell} ipython3
:tags: [ifStatement]

for x in range(10):
	print(x)
```