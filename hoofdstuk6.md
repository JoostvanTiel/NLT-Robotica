# Hoofdstuk 6: Herhalingen en loops

In eerdere hoofdstukken heb je al gezien dat je met `while True:` code steeds opnieuw kunt uitvoeren. In dit hoofdstuk leer je hoe je herhalingen bewust en gecontroleerd gebruikt. We behandelen twee soorten loops: de `while`-loop en de `for`-loop. Daarna combineren we loops met sensoren en motoren van de Maqueen.

## Waarom loops?

Zonder loops zou je dezelfde regels code steeds opnieuw moeten typen. Met loops maak je programma's korter, overzichtelijker en makkelijker aan te passen.

Gebruik een loop bijvoorbeeld om:

- een sensor meerdere keren uit te lezen;
- een actie exact een bepaald aantal keer uit te voeren;
- code te blijven uitvoeren totdat aan een voorwaarde is voldaan.

## while-loops

    while conditie:
    	instructies...

Een `while`-loop blijft doorgaan zolang de conditie `True` is.

Voorbeeld: tel van 0 tot en met 9.

```{code-cell} ipython3
:tags: [whileLoop]

n = 0

while n < 10:
	print(n)
	n = n + 1
```

Vaak zie je in robotcode ook deze vorm:

	while True:
		instructies...

Deze loop stopt niet vanzelf. Dat is handig als je robot continu moet blijven reageren op sensoren.

## break en continue

In een loop kun je twee extra commando's gebruiken:

- `break`: stopt de hele loop direct.
- `continue`: slaat de rest van de huidige ronde over en gaat door met de volgende ronde.

```{code-cell} ipython3
:tags: [whileLoop]

n = 0

while True:
	n = n + 1

	if n == 3:
		continue

	print(n)

	if n == 6:
		break
```

In dit voorbeeld wordt 3 niet geprint (door `continue`) en stopt de loop bij 6 (door `break`).

## for-loops

    for x in range(getal):
    	instructies...

Een `for`-loop gebruik je als je van tevoren weet hoe vaak iets moet gebeuren.

```{code-cell} ipython3
:tags: [forLoop]

for x in range(10):
	print(x)
```

`range(10)` geeft de getallen 0 tot en met 9.

Je kunt ook een begin- en eindwaarde opgeven:

```{code-cell} ipython3
:tags: [forLoop]

for x in range(2, 7):
	print(x)
```

Dit print 2, 3, 4, 5 en 6.

## while of for?

- Gebruik `while` als het aantal herhalingen afhangt van een conditie of sensorwaarde.
- Gebruik `for` als je een actie een vast aantal keer wilt uitvoeren.

## Loops bij de Maqueen

Bij robotica gebruik je loops bijna altijd samen met functies uit `maqueen.py` en `microbit`.

Voorbeeld: laat de robot 5 keer kort vooruit rijden.

	from maqueen import *
	from microbit import *

	init_maqueen()

	for i in range(5):
		motor_aan(80, 0)
		sleep(500)
		motor_uit()
		sleep(300)

Voorbeeld: blijf rijden tot een voorwerp dichtbij is.

	from maqueen import *
	from microbit import *

	init_maqueen()

	while True:
		afstand = rangefinder()
		if afstand < 15:
			motor_uit()
			break
		motor_aan(60, 0)

## Opdrachten hoofdstuk 6

1. Schrijf een programma met een `for`-loop dat de getallen 1 tot en met 10 op het scherm van de simulator print.

2. Schrijf een programma met een `while`-loop dat start bij `n = 20` en aftelt naar 0.

3. Schrijf een programma met een `for`-loop dat alleen de even getallen tussen 0 en 20 print.

4. Maak een programma dat met een `while True`-loop steeds de afstand van de ultrasone sensor toont op de micro:bit. Voeg `sleep(200)` toe zodat de waarde rustig vernieuwt.

5. Laat de Maqueen vooruit rijden totdat `rangefinder()` kleiner is dan 20 cm. Stop dan met `motor_uit()`.

6. Laat de Maqueen een vierkant rijden: 4 keer een stuk vooruit, daarna een kwartslag draaien.

7. Gebruik een `for`-loop om de robot eerst 3 keer naar links te laten draaien en daarna 3 keer naar rechts.

8. Maak een programma waarin de robot blijft rijden met `while True`, maar stopt met `break` als knop A wordt ingedrukt op de micro:bit.

9. Combineer lijnsensoren en loops: laat de robot in een `while True`-loop de middelste lijnsensor uitlezen en:
   - vooruit rijden als `lijnsensor_m` op de lijn staat;
   - anders stoppen.

10. Uitdagingsopdracht: schrijf een programma dat de robot autonoom laat rondrijden en obstakels ontwijkt. Gebruik minstens:
    - 1 `while`-loop;
    - 1 `for`-loop;
    - 1 `break` of `continue`.

## Reflectie

Leg in je eigen woorden uit:

1. Wanneer kies je voor een `while`-loop?
2. Wanneer kies je voor een `for`-loop?
3. Wat doet `break` in een loop?
