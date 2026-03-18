# Hoofdstuk 6: Herhalingen en loops

In hoofdstuk 4 heb je gewerkt met condities en in hoofdstuk 5 met functies. In dit hoofdstuk combineren we die kennis met **loops**. Daarmee laat je de robot acties herhalen zonder steeds dezelfde regels opnieuw te schrijven.

Je leert twee soorten loops:

- `while`-loops: herhalen zolang een conditie waar is;
- `for`-loops: herhalen een vast aantal keer.

Daarna pas je dit toe op de Maqueen met sensoren, motoren en veiligheid.

## Waarom loops?

Zonder loops zou je veel code moeten kopiëren en plakken. Met loops maak je je programma:

- korter;
- overzichtelijker;
- makkelijker aan te passen;
- minder foutgevoelig.

## while-loop

Een `while`-loop blijft doorgaan zolang de conditie `True` is.

    while conditie:
        instructies...

Voorbeeld: tel van 0 tot en met 9.

```{code-cell} ipython3
:tags: [whileLoop]

n = 0

while n < 10:
    print(n)
    n = n + 1
```

### Oneindige while-loop

Bij robots zie je vaak:

    while True:
        instructies...

Dat is handig, omdat de robot dan continu kan blijven reageren op sensoren.

## break en continue

In loops gebruik je vaak deze twee commando's:

- `break`: stopt de hele loop direct;
- `continue`: slaat de rest van deze ronde over en gaat direct naar de volgende ronde.

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

In dit voorbeeld wordt 3 niet geprint en stopt de loop bij 6.

## for-loop

Een `for`-loop gebruik je als je vooraf weet hoe vaak iets moet gebeuren.

    for x in range(getal):
        instructies...

Voorbeeld:

```{code-cell} ipython3
:tags: [forLoop]

for x in range(10):
    print(x)
```

`range(10)` geeft de getallen 0 tot en met 9.

Je kunt ook een begin- en eindwaarde gebruiken:

```{code-cell} ipython3
:tags: [forLoop]

for x in range(2, 7):
    print(x)
```

Dit print 2, 3, 4, 5 en 6.

## while of for?

- Gebruik `while` als het aantal herhalingen afhangt van een conditie (bijvoorbeeld sensorwaarde).
- Gebruik `for` als je een actie exact een vast aantal keer wilt herhalen.

## Loops met de Maqueen

In robotprogramma's combineer je loops bijna altijd met functies uit `maqueen.py` en `microbit`.

### Voorbeeld 1: 5 keer kort vooruit rijden

    from maqueen import *
    from microbit import *

    init_maqueen()

    for i in range(5):
        motor_links(aan, snelheid=80)
        motor_rechts(aan, snelheid=80)
        sleep(500)
        motor_links(uit)
        motor_rechts(uit)
        sleep(300)

### Voorbeeld 2: rijden tot obstakel

    from maqueen import *
    from microbit import *

    init_maqueen()

    while True:
        afstand = afstand_tot_voorwerp()
        if afstand < 15:
            motor_links(uit)
            motor_rechts(uit)
            break

        motor_links(aan, snelheid=60)
        motor_rechts(aan, snelheid=60)

### Voorbeeld 3: lijn volgen met drempelwaarde

Gebruik de drempelwaarde die je in hoofdstuk 3 hebt gekalibreerd (bijvoorbeeld `150`).

    from maqueen import *
    from microbit import *

    init_maqueen()

    drempelwaarde = 150

    while True:
        if lees_lijnsensor(m) < drempelwaarde:
            motor_links(aan, snelheid=70)
            motor_rechts(aan, snelheid=70)
        else:
            motor_links(uit)
            motor_rechts(uit)

## Opdrachten hoofdstuk 6

1. Leg in je eigen woorden uit:
1. Wanneer kies je voor een `while`-loop?
1. Wanneer kies je voor een `for`-loop?
1. Wat is het verschil tussen `break` en `continue`?
1. Waarom is een drempelwaarde belangrijk bij lijnsensoren?

1. Schrijf een programma met een `for`-loop dat de getallen 1 tot en met 10 print.

1. Schrijf een programma met een `while`-loop dat start bij `n = 20` en aftelt naar 0.

1. Schrijf een programma met een `for`-loop dat alleen de even getallen tussen 0 en 20 print.

1. Maak een programma met een `while True`-loop dat steeds de afstand (`afstand_tot_voorwerp()`) op de micro:bit toont. Voeg `sleep(200)` toe zodat de waarde rustig vernieuwt.

1. Laat de Maqueen vooruit rijden totdat de afstand kleiner is dan 20 cm. Stop daarna met beide motoren.

1. Schrijf een programma dat de robot 4 keer een vierkant-hoek laat maken:
   - rijd 1 seconde vooruit;
   - draai ongeveer 0,4 seconde naar rechts;
   - herhaal dit 4 keer.

1. Gebruik een `for`-loop om de robot eerst 3 keer kort naar links te laten draaien en daarna 3 keer kort naar rechts.

1. Maak een programma met `while True` waarin de robot blijft rijden, maar stopt met `break` zodra knop A is ingedrukt.

1. Gebruik de middelste lijnsensor in een `while True`-loop met drempelwaarde:

- als `lees_lijnsensor(m) < drempelwaarde`: rijd vooruit;
- anders: stop.

11. Breid de vorige opdracht uit met bijsturen:

- als `lees_lijnsensor(l1) < drempelwaarde`: stuur naar links;
- als `lees_lijnsensor(r1) < drempelwaarde`: stuur naar rechts;
- anders: stop.

12. Maak een programma dat twee veiligheidsregels combineert in een loop:

- stop als afstand < 15 cm;
- stop ook als knop B wordt ingedrukt.

13. Uitdagingsopdracht: laat de robot 30 seconden autonoom rijden en obstakels ontwijken.
    Gebruik minimaal:

- 1 `while`-loop;
- 1 `for`-loop;
- 1 `break` of `continue`;
- 1 lijnsensor met drempelwaarde.
