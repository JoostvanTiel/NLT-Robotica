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

De gemeten sensorwaarde van de lijnsensoren ligt tussen 0 en 255. In dit hoofdstuk gebruiken we bij de lijnsensoren een drempelwaarde van 150, maar de juiste drempel kan per robot verschillen en bepaal je met de kalibratie uit opdracht 2 van hoofdstuk 3.

## operatoren

Om condities te kunnen checken worden de volgende operatoren gebruikt:

| Operator | Naam                      | Voorbeeld           |
| :------- | :------------------------ | :------------------ |
| ==       | Gelijk aan                | afstand == 20       |
| !=       | Niet gelijk aan           | afstand != 100      |
| >        | Groter dan                | afstand > 100       |
| <        | Kleiner dan               | lijnsensor_r1 < 200 |
| >=       | Groter dan of gelijk aan  | lijnsensor_m >= 75  |
| <=       | Kleiner dan of gelijk aan | lijnsensor_l1 <= 50 |

## if statements

    if conditie:
    	instructies...
    elif andere_conditie: # optioneel
    	instructies...
    else:		      # optioneel
    	instructies...

```{code-cell} ipython3
:tags: [ifStatement]

afstand = afstand_tot_voorwerp()
stopafstand = 30

if afstand < stopafstand:
   # Obstakel dichtbij: stop de robot.
   motor_links(uit)
   motor_rechts(uit)
elif afstand == stopafstand:
   # Exact op de grens: rijd langzaam.
   motor_links(aan, snelheid=20)
   motor_rechts(aan, snelheid=20)
else:
	# Vrije weg: rijd door.
   motor_links(aan, snelheid=100)
   motor_rechts(aan, snelheid=100)
```

Meerdere condities tegelijk checken

| Operator | Beschrijving                                                           | Voorbeeld                                  |
| :------- | :--------------------------------------------------------------------- | :----------------------------------------- |
| and      | Retourneert `True` als beide condities waar zijn.                      | afstand < 15 and lijnsensor_m > 0          |
| or       | Retourneert `True` als één van beide condities waar is.                | lijnsensor_l1 < 150 or lijnsensor_r1 < 150 |
| not      | Keert het resultaat om, retourneert `False` als het resultaat waar is. | not(knop_a_ingedrukt)                      |

Bijvoorbeeld:

```{code-cell} ipython3
:tags: [ifStatement]

if afstand_tot_voorwerp() < 25 and lees_lijnsensor(m) < 150:
	# Robot op lijn, maar obstakel gedetecteerd: remmen.
   motor_links(uit)
   motor_rechts(uit)
elif lees_lijnsensor(m) < 150 and afstand_tot_voorwerp() >= 25:
	# Robot volgt de lijn en rijdt door.
   motor_links(aan, snelheid=100)
   motor_rechts(aan, snelheid=100)
elif lees_lijnsensor(l1) < 150 or lees_lijnsensor(r1) < 150:
   # Corrigeer koers naar het midden van de lijn.
   if lees_lijnsensor(l1) < 150:
      # Draai naar links
      motor_links(uit)
      motor_rechts(aan, snelheid=100)
   elif lees_lijnsensor(r1) < 150:
      # Draai naar rechts
      motor_links(aan, snelheid=100)
      motor_rechts(uit)
else:
   # Robot ziet geen lijn, stop maar en geef dit aan
   motor_links(uit)
   motor_rechts(uit)
   display.show(Image.CONFUSED)
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
    	if afstand_tot_voorwerp() < 15:
    		motor_links(uit)
         motor_rechts(uit)
    	else:
    		motor_links(aan, snelheid=60)
         motor_rechts(aan, snelheid=60)

## Opdrachten hoofdstuk 4

1. Schrijf een programma dat op de micro:bit de tekst "STOP" toont als de afstand kleiner is dan 20 cm, en anders "RIJD".
2. Schrijf een programma waarin de robot alleen vooruit rijdt als knop A is ingedrukt. Anders moet de robot stilstaan.
3. Gebruik `if`, `elif` en `else` om drie zones te maken op basis van afstand:
   1. kleiner dan 10 cm: stoppen;
   2. tussen 10 en 50 cm: langzaam rijden;
   3. groter dan 50 cm: normaal rijden.
4. Pak een groot wit A2 vel en schrijf in een hoek de namen van jou en je partner. Maak met zwarte tape een rechte lijn op je vel.
5. Schrijf een programma dat de middelste lijnsensor uitleest en de robot over de lijn van de vorige opdracht laat rijden. Gebruik weer de drempelwaarde uit opdracht 2 van hoofdstuk 2:
   1. als `lees_lijnsensor(m) < drempelwaarde`: rijd vooruit;
   2. anders: stop de robot.
6. Breid de vorige opdracht uit met linker en rechter lijnsensor (`l1`, `r1`) zodat de robot kan bijsturen naar links of rechts op basis van dezelfde drempelwaarde.
7. Maak een programma met een veiligheidsvoorwaarde: de robot mag alleen rijden als:
   1. de afstand groter is dan 15 cm, en
   2. knop B niet is ingedrukt.
8. Uitdagingsopdracht: combineer lijnvolgen en obstakeldetectie.
   1. Volg de lijn zolang er geen obstakel is.
   2. Als er een obstakel binnen 15 cm is: stop, wacht 1 seconde, en probeer daarna opnieuw te rijden.
