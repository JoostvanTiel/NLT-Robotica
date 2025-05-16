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

# Hoofdstuk 5: If-statements en operatoren

De omgeving van de robot verandert en hier moet de robot op kunnen reageren. Daarvoor zijn statements erg handig. Je kunt de robot specifieke acties laten uitvoeren op het juiste moment. Daarvoor kun je gebruik maken van if-statements.

## Operatoren

Voor alle soorten statements moeten checks uitgevoerd worden waarbij de robot controleert of er aan een bepaalde voorwaarde wordt voldaan. Om een check uit te voeren, worden operatoren gebruikt. Een operator kun je zien als het stellen van een vraag (is de afstand tot de muur kleiner dan 15 cm?). Vervolgens wordt de statement gebruikt om een vervolgactie te ondernemen.
De basisoperatoren zijn als volgt:

| Operator | Naam                      | Voorbeeld |
|:---------|:--------------------------|:----------|
| ==       | Gelijk aan                | x == y    |
| !=       | Niet gelijk aan           | x != y    |
| >        | Groter dan                | x > y     |
| <        | Kleiner dan               | x < y     |
| >=       | Groter dan of gelijk aan  | x >= y    |
| <=       | Kleiner dan of gelijk aan | x <= y    |

## if-statements

Je wilt dat een robot in bepaalde situaties bepaald gedrag vertoont. Bijvoorbeeld: als de robot van de lijn afwijkt, moet hij gaan bijsturen om weer op de lijn te staan. Je weet van te voren niet of de robot links of rechts van de lijn zal afwijken. Daarom moet je afhankelijk van de situatie kunnen beheersen welk gedrag de robot vertoont. Daarvoor gebruik je het if-statement. Dit ziet er zo uit:

	if voorwaarde:
		instructies...

De voorwaarde is waar aan voldaan moet worden. Als er aan de voorwaarde voldaan wordt, dan worden de instructies die daarop volgen uitgevoerd. Bijvoorbeeld:

	x = 4
	y = 7

	if x < y:
		display.scroll("y is groter dan x.")

Hieronder zie je een voorbeeld waarin de robot naar rechts stuurt als hij links van de lijn afwijkt en andersom.

	if read_line_sensor(lijnsensor_l1) < 100:
		draaiRechts(1000)
		
	if read_line_sensor(lijnsensor_r1) < 100:
		draaiLinks(1000)

Een voorwaarde kan van alles zijn en is meestal een vergelijking. In het bovenstaande voorbeeld is de voorwaarde: De lijnsensor_l1 ziet een lijn.
Soms wil je bij het if-statement als er niet aan de voorwaarde wordt voldaan, dat hij altijd een ander stukje code uitvoert. Bijvoorbeeld: Als de de lijnsensor_m de lijn ziet, moet de robot vooruit rijden en anders moet de robot stoppen.
Je kunt dan else-statements gebruiken. Een else-statement werkt alleen als het direct volgt op een if-statement of een elif-statment (zie verderop):

	if voorwaarde:
		instructies...
	else:
		instructies...

Bijvoorbeeld:

	x = 8
	y = 5

	if x < y:
		display.scroll("y is groter dan x.")
	else:
		display.scroll("x is groter dan y.")

In het onderstaande voorbeeld rijdt de robot rechtdoor als lijnsensor_m de lijn ziet, anders stopt hij:

	if read_line_sensor(lijnsensor_m) < 100:
		motor_aan(motor_links)
		motor_aan(motor_rechts)
	else:
		motor_uit(motor_links)
		motor_uit(motor_rechts)

In het bovenstaande voorbeeld gaat de motor uit als de robot van de lijn afwijkt, maar dat is niet altijd gewenst. Soms wil je dat er verschillende acties uit worden gevoerd als er niet voldaan wordt aan de eerste voorwaarde (`lijnsensor_m < 100`). Je kunt dan een `elif`-statement gebruiken. Dit staat voor 'else if' en er kan dus nogmaals een voorwaarde worden gecontroleert. Er kunnen meerdere `elif`-statements na elkaar gebruikt worden. Een `elif`-statement werkt alleen als het direct volgt op een if-statement of op een elif-statement:

	if voorwaarde:
		instructies...
	elif andere_voorwaarde:
		instructies...
	else:
		instructies...

Bijvoorbeeld:

	x = 3
	y = 3

	if x < y:
		display.scroll("y is groter dan x.")
	elif x == y:
		display.scroll("y is gelijk aan x.")
	else:
		display.scroll("x is groter dan y.")

In het onderstaande voorbeeld rijdt de robot rechtdoor als lijnsensor_m de lijn ziet. Als dat niet het geval is, stuurt hij naar rechts als lijnsensor_l1 de lijn ziet en naar links als lijnsensor_r1 de lijn ziet. Anders zet hij de motor uit:

	if read_line_sensor(lijnsensor_m) < 100:
		motor_aan(motor_links)
		motor_aan(motor_rechts)
	elif read_line_sensor(lijnsensor_l1) < 100:
		draaiRechts(1000)
	elif read_line_sensor(lijnsensor_r1) < 100:
		draaiLinks(1000)
	else:
		motor_uit(motor_links)
		motor_uit(motor_rechts)

## Meerdere voorwaarden tegelijk

Het is ook mogelijk om meerdere voorwaarden tegelijk te controleren. Daarvoor gebruiken we de volgende operatoren:

| Operator | Beschrijving                                                          | Voorbeeld               |
|:---------|:----------------------------------------------------------------------|:------------------------|
| and      | Retourneert `True` als beide voorwaarden waar zijn.                   | x < 10 and y > 4        |
| or       | Retourneert `True` als één van beide voorwaarden waar is.             | x < 5 or y > 4          |
| not      | Keert het resultaat om, retourneert `False` als het resultaat waar is.| not( x < 4 and y > 10 ) |

Bijvoorbeeld:

	x = 3
	y = 6
	z = 9

	if x < y and y < z:
		display.scroll("x is het kleinste getal.")

	if y < x and y < z:
		display.scroll("y is het kleinste getal.")
	elif y < x or y < z:
		display.scroll("y is niet het grootste getal.")

	if z < y and z < x:
		display.scroll("z is het kleinste getal.")
	elif not(z < y and z < x):
		display.scroll("z is het grootste getal.")
	else:
		display.scroll("z is niet het grootste en niet het kleinste getal.")


In het onderstaande voorbeeld is nogmaals het voorbeeld van hierboven gegeven, maar nu is een extra controle toegevoegd. De robot rijdt rechtdoor als lijnsensor_m de lijn ziet **en** als er geen voorwerp binnen 30 cm van de robot staat:

	if read_line_sensor(lijnsensor_m) < 100 and afstand_tot_voorwerp() >= 30:
		motor_aan(motor_links)
		motor_aan(motor_rechts)
	elif read_line_sensor(lijnsensor_l1) < 100:
		draaiRechts(1000)
	elif read_line_sensor(lijnsensor_r1) < 100:
		draaiLinks(1000)
	else:
		motor_uit(motor_links)
		motor_uit(motor_rechts)

## Opdrachten hoofdstuk 5

### Zonder robot
Haal de micro:bit uit de robot en gebruik voor de eerste drie opdrachten de hulp in de 'Reference' links in het scherm.

1. Schrijf een programma dat controleert of knop A of knop B wordt ingedrukt:
	+ Als knop A wordt ingedrukt, toont de micro:bit een hartje.
	+ Als knop B wordt ingedrukt, toont de micro:bit een lachend gezichtje.
	+ Als geen van beide knoppen wordt ingedrukt, toont de micro:bit een streepje (-).
	+ Onderzoek welke knop 'voorrang' krijgt.

2. Schrijf een programma dat:
	+ Een hart toont als zowel knop A als knop B tegelijkertijd worden ingedrukt.
	+ Een klein hartje toont als slechts één knop wordt ingedrukt.
	+ Niets toont als geen van de knoppen wordt ingedrukt.

3. Maak een automatische zaklamp. Schrijf een programma dat het scherm helderder maakt als het donker is. Gebruik daarvoor de lichtsensor om te bepalen hoeveel licht er is:
	+ Als het donkerder is dan 50 (lichtniveau), zet de micro:bit alle lampjes op het scherm maximaal aan (zelfgemaakte afbeelding).
	+ Als het lichtniveau tussen 50 en 200 ligt, zet de micro:bit alle lampjes op niveau 5.
	+ Als het lichtniveau boven de 200 is, maakt de micro:bit het scherm leeg.
	+ Experimenteer met de drempelwaarden om te zien hoe de sensor reageert.

### Met robot
Stop nu de micro:bit in de robot

4. Schrijf een programma dat de robot vooruit laat rijden tot aan een zwarte streep.

5. Schrijf een programma dat de robot vooruit laat rijden tot 30 cm van een voorwerp.

6. Breidt het programma van opdracht 4 en 5 als volgt uit:
	+ Als de robot bij een lijn is aangekomen **en** er geen voorwerp binnen 10 cm staat, moet deze zich omdraaien.
	+ Als de robot bij een lijn is aangekomen **en** er wel een voorwerp binnen 10 cm staat, moet de robot stoppen en er moet een geluidssignaal `audio.play(Sound.GIGGLE)` worden afgespeeld.
	+ Anders moet de robot gewoon vooruit rijden.
	+ Test het gedrag van de robot op het speelveld.

7. Schrijf een programma dat de robot laat stoppen of rijden afhankelijk van de afstand tot een object. Pas ook de kleur van de underglow `set_underglow(kleur)` aan:
	+ Als een object dichterbij komt dan 10 cm, laat de robot stoppen en zet de underglow op rood.
	+ Als de afstand tussen 10 en 30 cm ligt, laat de robot langzaam rijden en zet de underglow op geel.
	+ Als de afstand groter is dan 30 cm, laat de robot normaal rijden en zet de underglow op groen.

8. Schrijf een programma dat de robot obstakels laat ontwijken:
	+ Als een object dichterbij komt dan 10 cm, moet de robot stoppen en 90 graden draaien.
	+ Als de robot weer ruimte heeft (afstand > 10 cm), moet deze verder rijden.
	+ Test zelf welke tijd in de functie `draaiLinks()` of `draaiRechts()` van hoofdstuk 3 moet worden ingevuld om de robot 90 graden te laten draaien.
