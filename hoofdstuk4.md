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

# Hoofdstuk 4: Condities en if-statements

In dit hoofdstuk leer je hoe een robot keuzes maakt. Een robot moet namelijk steeds beslissen wat hij moet doen op basis van sensorwaarden. Met condities en if-statements kun je die beslissingen programmeren.

## operatoren

Om condities te kunnen checken worden de volgende operatoren gebruikt:

| Operator | Naam                      | Voorbeeld              |
| :------- | :------------------------ | :--------------------- |
| ==       | Gelijk aan                | afstand == 20          |
| !=       | Niet gelijk aan           | lijnsensor_m != 1      |
| >        | Groter dan                | snelheid > 100         |
| <        | Kleiner dan               | afstand < 15           |
| >=       | Groter dan of gelijk aan  | batterij >= 3.2        |
| <=       | Kleiner dan of gelijk aan | afstand <= stopafstand |

## if statements

    if conditie:
    	instructies...
    elif andere_conditie: # optioneel
    	instructies...
    else:		      # optioneel
    	instructies...

```{code-cell} ipython3
:tags: [ifStatement]

afstand = 12
stopafstand = 15

if afstand < stopafstand:
	print("Obstakel dichtbij: stop de robot.")
elif afstand == stopafstand:
	print("Exact op de grens: rijd langzaam.")
else:
	print("Vrije weg: rijd door.")
```

Meerdere condities tegelijk checken

| Operator | Beschrijving                                                           | Voorbeeld                                |
| :------- | :--------------------------------------------------------------------- | :--------------------------------------- |
| and      | Retourneert `True` als beide condities waar zijn.                      | afstand < 15 and snelheid > 0            |
| or       | Retourneert `True` als één van beide condities waar is.                | lijnsensor_l1 == 1 or lijnsensor_r1 == 1 |
| not      | Keert het resultaat om, retourneert `False` als het resultaat waar is. | not(knop_a_ingedrukt)                    |

Bijvoorbeeld:

```{code-cell} ipython3
:tags: [ifStatement]

afstand = 10
snelheid = 80
lijnsensor_m = 1
lijnsensor_l1 = 0
lijnsensor_r1 = 0

if afstand < 15 and snelheid > 0:
	print("Obstakel gedetecteerd: remmen.")

if lijnsensor_m == 1 and afstand >= 15:
	print("Robot volgt de lijn en rijdt door.")
elif lijnsensor_l1 == 1 or lijnsensor_r1 == 1:
	print("Corrigeer koers naar het midden van de lijn.")

if not(lijnsensor_m == 1):
	print("Midden-sensor ziet geen lijn: zoek de lijn opnieuw.")
```

## Condities met de Maqueen

In een echt robotprogramma combineer je condities met functies uit `maqueen.py` en `microbit`.

Voorbeeld in pseudocode:

    Als afstand kleiner is dan 15 cm:
    	Stop de motor
    Anders:
    	Rijd vooruit

Voorbeeldcode:

    from maqueen import *
    from microbit import *

    init_maqueen()

    while True:
    	afstand = rangefinder()
    	if afstand < 15:
    		motor_uit()
    	else:
    		motor_aan(60, 0)

## Opdrachten hoofdstuk 4

1. Schrijf een programma dat op de micro:bit de tekst "STOP" toont als de afstand kleiner is dan 20 cm, en anders "RIJD".

2. Schrijf een programma waarin de robot alleen vooruit rijdt als knop A is ingedrukt. Anders moet de robot stilstaan.

3. Gebruik `if`, `elif` en `else` om drie zones te maken op basis van afstand:
   - kleiner dan 10 cm: stoppen;
   - tussen 10 en 25 cm: langzaam rijden;
   - groter dan 25 cm: normaal rijden.

4. Schrijf een programma dat de middelste lijnsensor uitleest:
   - als `lijnsensor_m == 1`: rijd vooruit;
   - anders: stop de robot.

5. Breid opdracht 4 uit met linker en rechter lijnsensor (`lijnsensor_l1`, `lijnsensor_r1`) zodat de robot kan bijsturen naar links of rechts.

6. Maak een programma met een veiligheidsvoorwaarde: de robot mag alleen rijden als:
   - de afstand groter is dan 15 cm, en
   - knop B niet is ingedrukt.

7. Uitdagingsopdracht: combineer lijnvolgen en obstakeldetectie.
   - Volg de lijn zolang er geen obstakel is.
   - Als er een obstakel binnen 15 cm is: stop, wacht 1 seconde, en probeer daarna opnieuw te rijden.
