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
Tot nu toe hebben we gekeken naar manieren om een stukje code van de robot eenmalig uit te voeren. Vaak is het heel handig om een bepaalde handeling te herhalen. In dit hoofdstuk leer je hoet je `while` en `for` statements kunt gebruiken om dit voor elkaar te krijgen. Het stukje code dat met zo'n statement wordt uitgevoerd wordt ook wel een **lus** genoemd. Het doorlopen van een lus wordt ook wel **itereren** genoemd. Het eenmalig doorlopen van de lus heet een **iteratie**.

## while lussen
Een `while` lus herhaalt een set instructies zo lang aan een voorwaarde voldaan wordt. Achter het `while` statement moet dus een controle staan die `True` of `False` op kan leveren. 
De syntax om zo'n lus te maken is als volgt:

	while conditie:
		instructies...

Hieronder zie je een voorbeeld waarin een variabele (n) in eerste nul is. Vervolgens komt de while lus, waarin de waarde van n op het scherm wordt getoond. Vervolgens wordt de waarde van n met 1 verhoogd met de code `n = n + 1`.

	n = 0

	while n < 10:
		n = n + 1
		display.show(n)
		sleep(250)
		
	display.clear()

### break statements
Met het `break` statement kunnen we een while loop doorbreken, ook al is de voorwaarde die gecontrolleerd wordt nog steeds waar. Probeer het stukje code hieronder maar eens uit.

	n = 0

	while n < 10:
		display.show(n)
		sleep(250)
		if n == 3:
			break
		n = n + 1
		
	display.clear()

### continue statements
Met het `continue` statement kunnen we de huidige iteratie overslaan en doorgaan met de volgende iteratie, zoals te zien is in het volgende stukje code.

	n = 0

	while n < 9:
		n = n + 1
		if n == 3:
			continue
		display.show(n)
		sleep(250)
		
	display.clear()

## for lussen
Met een `for` lus kan geïtereerd worden over een reeks aan waardes. Die waardes kunnen getallen zijn, maar ook andere soorten variabelen (zoals strings).

	for variabele in reeks:
		instructies...

In het voorbeeld hieronder worden twee reeksen gedeclareerd: `getallen` en `letters`. Een reeks wordt gedeclareerd door een aantal waardes, gescheiden door komma's, tussen vierkante haakjes (`[` en `]`) te zetten. De `for` lus wordt voor iedere waarde in de reeks een keer doorlopen. De variabele krijgt in die iteratie de waarde van de reeks toegekend. De `for` lus wordt automatisch afgebroken als het eind van de reeks is bereikt.

	getallen = [0, 1, 2, 3, 4, 5]
	letters = ["a", "b", "c", "d", "e", "f"]

	for getal in getallen:
		display.show(getal)
		sleep(250)

	for letter in letters:
		display.show(letter)
		sleep(250)

	display.clear()

### De range() functie
Met de `range()` functie kan snel een reeks aan getallen worden aangemaakt. De functie maakt een reeks **tot** het getal dat als parameter wordt meegegeven.
Zo geeft `range(5)` de reeks `[0, 1, 2, 3, 4]`. 

	for x in range(5):
		display.show(x)
		sleep(250)

	display.clear()

Er kunnen ook meerdere parameters aan de `range()` functie worden meegegeven.
Laten we de parameters 'a', 'b' en 'c' noemen. In de functie `range(a, b, c)` is a het startgetal, b het eindgetal en c de stapgrootte.
De functie `range(3, 15, 4)` produceert dus de reeks `[3, 7, 11]`

	for x in range(3, 15, 4):
		display.scroll(x)
		sleep(250)

	display.clear()

Net als bij een `while` lus, kunnen de `break` en `continue` statements ook bij een `for` lus gebruikt worden. 

## else na een lus
Zowel bij `while` lussen als bij `for` lussen kan na het itereren door de lus een afsluitende set aan instructies worden uitgevoerd met `else`. 

	for x in range(2, 12, 2):
		display.scroll(x)
		sleep(250)
	else:
		display.show(5)
		sleep(1000)

	display.clear()

Deze instructies worden niet doorlopen als er uit de lus gebroken wordt met een `break` statement.

	for x in range(2, 12, 2):
		display.scroll(x)
		if x >= 8:
			break
		sleep(250)
	else:
		display.show(5)
		sleep(1000)

	display.clear()

## Opdrachten hoofdstuk 6

1. Nadenken over de volgorde van instructies bij de verschillende voorbeelden van de while statements met break en for.

2. 

3. 

4. 