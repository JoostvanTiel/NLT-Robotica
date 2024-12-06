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

# Hoofdstuk 6: Lussen
In dit hoofdstuk worden while-statements en for-statements behandeld.

## while lussen

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

## for lussen

	for x in range(getal):
		instructies...

```{code-cell} ipython3
:tags: [ifStatement]

for x in range(10):
	print(x)
```

## Opdrachten hoofdstuk 6

1. 

2. 

3. 

4. 