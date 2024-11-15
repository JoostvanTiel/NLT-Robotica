# Hoofdstuk 3: Functies en variabelen

In de afgelopen twee hoofdstukken zijn we meerdere functies tegengekomen. In dit hoofdstuk gaan we dieper in op wat functies zijn en hoe je ze gebruikt. Hiervoor moeten we weten wat voor soorten functies en wat voor soorten variabelen er zijn. We zullen de belangrijkste in dit hoofdstuk bespreken. Daarna gaan we kijken naar de werking van verschillende functies die je kunt aanroepen om de Maqueen te besturen.   

## Functies 

In het vorige hoofdstuk zijn we het commando `motor_aan()` tegengekomen. Dit is een voorbeeld van een functie. Je kunt een functie herkennen aan de haakjes die achter het commando staan. Functies gebruik je vooral bij langere codes, omdat die anders snel onoverzichtelijk worden. Je splitst in dit geval je code op in verschillende kleinere programma’s (de functies). Zo kun je complexere programma’s overzichtelijk en makkelijk te begrijpen houden. Verder kunnen functies ook helpen om geheugen te besparen, omdat je een bepaalde functie meerdere keren  kunt aanroepen. Je kunt deze functies vergelijken als een functie in de wiskunde. Je stopt er iets in (invoer), de  functie verwerkt dat, en je krijgt er weer iets uit (uitvoer).  

Naast de functies die we al zijn tegengekomen, en alle functies die in de map `maqueen.py` staan, kun je ook je eigen functies schrijven. Een voorbeeld van een simpele functie is: 

	# rekent de oppervlakte van een rechthoek uit
	# hoogte: de hoogte van de rechthoek
	# breedte: de breedte van de rechthoek
	# return: de oppervlakte van de rechthoek
	
	def Oppervlakte(hoogte, breedte):
		Opp = hoogte * breedte
		return Opp

Je ziet dat de code begint met eerst in commentaar uitleggen  wat de functie doet, welke waardes hij meekrijgt en wat hij oplevert. Dit moet je er altijd bij schrijven als je een functie maakt. Zo blijft het altijd duidelijk wat welke functie doet. Om de functie te schrijven begin je altijd met def . Hiermee vertel je aan het programma dat je een functie gaat schrijven. Daarna geef je de functie een naam en zet je tussen haakjes de parameters.  

### Parameters 

Tussen de haakjes staan de waardes die de functie meekrijgt. Dit worden ook wel parameters genoemd. Parameters zijn de invoer van een functie. Binnen de functie gebruik je de parameters als variabelen. De waarden van de parameters weet je niet als je de functie schrijft. Die worden pas bepaald als de functie wordt aangeroepen. Als je de functie schrijft moet je wel aangeven hoe je de parameter noemt. Het maakt niet uit hoeveel parameters een functie heeft. Als je geen parameters hebt, dan laat je het gedeelte tussen de haakjes leeg. 

### Returnwaarde 

Een functie kan hooguit 1 waarde als uitvoer hebben. Dit is de returnwaarde. In de code van de functie moet je aangeven welke waarde teruggegeven moet worden. Dit doe je door `return` te gebruiken. Achter return geef je aan wat je terug wilt geven. Dit kan een variabele zijn, maar ook een letterlijke waarde. 

### Functies aanroepen 

Om functies te kunnen gebruiken moet je deze aanroepen. Dit doe je door de naam van de functie op te geven, gevolgd door de waarden van de parameters. Om een functie aan te roepen hoef je dus niet te weten hoe de parameters heten, als je maar weet hoeveel parameters je op moet geven. 

	# rekent de oppervlakte van een rechthoek uit 
	# hoogte: de hoogte van de rechthoek
	# breedte: de breedte van de rechthoek
	# return: de oppervlakte van de rechthoek
	
	def Oppervlakte(hoogte, breedte):
		Opp = hoogte * breedte
		return Opp
		
	Opp_rechthoek = Oppervlakte(2,3)

Hierin zie je een voorbeeld van het aanroepen van de eerder geschreven functie. In dit geval wordt dus het oppervlak uitgerekend van een rechthoek van 2 bij 3. De resulterende waarde wordt vervolgens opgeslagen in een variabele genoemd Opp_rechthoek. Deze variabele krijgt nu dus de waarde 6. Als je een nieuwe functie maakt, moet deze gedefinieerd zijn voordat hij wordt aangeroepen. Anders weet de compiler niet welke functie je aan probeert te roepen, want de compiler werkt van boven naar beneden. 

### Void-functie 

Soms wil je ook functies maken die geen variabele oplevert. In zo’n geval gebruik je een void-functie. Het type void geeft aan dat de functie geen resultaat heeft. We zijn in deze module al veel void-functies  tegen gekomen.  Bijvoorbeeld de functie `motor_aan()`, maar ook de functie `display.show(Image.HEART)` hebben geen returnwaarde.  In het laatste voorbeeld zie je dat ook void-functies parameters kunnen bevatten. Hoewel ze geen returnwaarde hebben, kunnen ze wel een actie in gang zetten. 

## Variabelen 

In een functie vul je parameters in. Deze parameters zijn variabelen, en kunnen dus verschillende waarden aannemen. Variabelen kunnen van verschillende datatypen zijn. Het is belangrijk dat je variabelen van het correcte datatype meegeeft aan een functie. Probeer een variabele altijd een naam te geven, waaruit je kan opmaken wat er in opgeslagen wordt. In Python krijgt een variabele automatisch het datatype van hetgeen je hem meegeeft. Je kent iets toe aan een variabele door het gebruik van één “=” teken. Dit betekent “krijgt de waarde”. Een dubbel “==” teken is een vergelijking. Er wordt dan nagegaan of voor en na de “==” hetzelfde staat. De meeste gebruikte datatypen zijn 

	integer	# een geheel getal 
	bool	# True of false 
	float	# kommagetal 
	string	# woord of zin 

### integer 

De integer variabele gebruik je om gehele getallen in op te slaan. Je kan er bijvoorbeeld mee bijhouden hoe vaak je een object hebt gezien. Een voorbeeld van een toekenning is 

	x = 5 

Als je de variabele wilt gebruiken kun je de variabele aanroepen door de naam te gebruiken. In dit geval is dat ‘x’. Je kunt de variabele als volgt gebruiken: 

	x = 5 * 2 
	x = x * 2 

Bij de tweede regel gebruik je de oude waarde van x, om de nieuwe waarde te berekenen. In de eerste regel heeft x de waarde 10. In de tweede regel wordt dus 10 ingevuld voor x. Zo komt er te staan: x = 10 \* 2. De waarde van x wordt dan 20. De functie Oppervlakte is een voorbeeld van een functie met parameters van datatype integer.  

### bool 

Bool is de afkorting van boolean. Boolean betekent dat het maar 2 waardes kan hebben, waar of niet waar. In een programmeertaal wordt daarvoor `true` en `false` gebruikt. De bool variabele gebruik je bijvoorbeeld om op te slaan of je iets al gedaan of gezien hebt. We zijn hem al vaker tegengekomen in de vorm `while True`. Je kunt  hem bijvoorbeeld gebruiken om aan te geven dat je iets al een keer bent tegengekomen. Zo kun je de while-loop afbreken die we in eerdere hoofdstukken gezien hebben. Een voorbeeld hiervan is: 

	# laat 1 sec lang een afbeelding zien van een hart
	# scroll vervolgens het woord "Hello"
	# De while-loop wordt afgebroken
	
	niet_gezien = True
	while niet_gezien:
		display.show(Image.HEART)
		sleep(1000)
		display.scroll('Hello')
		niet_gezien = False

### float 

In een float-variabele kun je een kommagetal opslaan. Dit kan handig zijn als je waardes nauwkeurig wilt bepalen. Als je getallen gebruikt van het type integer voor een berekening, wordt de waarde namelijk afgerond. Om dit te voorkomen gebruiken we het type float. Dit doe je door een kommagetal in te vullen. In de functie `Oppervlakte` kun je de parameters ook invullen in het type float. Dit doe je dan als volgt: `Oppervlakte(2.2,2.3)`. Met een float kun je verder dezelfde dingen doen als met een int-variabele. 

### string 

In een string-variabele kun je een woord of hele zin opslaan. Een string kun je bijvoorbeeld gebruiken om een zin op het schermpje van de robot te zetten. We hebben deze bijvoorbeeld eerder gezien in de vorm `Display.scroll("Hello")`. Een string zet je altijd tussen aanhalingstekens. De functie `Display.scroll()` kan dus alleen parameters verwerken met datatype string.

## Werking motor 

Nu we weten hoe functies en hun parameters werken, kunnen we eerder gebruikte functies beter bekijken. We zijn eerder de functie `motor_aan()` tegengekomen. Het lijkt alsof deze functie geen parameters heeft. Toch is dit niet helemaal waar. Eigenlijk heeft de functie twee parameters: de snelheid en de richting van de robot. We hebben deze waarden voorheen niet meegegeven, omdat in de functie standaardwaarden zijn gegeven. Dat houdt in dat als er geen variabelen worden meegegeven, de functie automatisch de standaardwaarde pakt. De snelheid in deze functie kan worden ingevuld van 0 (stilstaan) tot 255 (het snelst). Voor de richting kan 0 (vooruit) en 1 (achteruit) worden ingevuld. Dit betekent dat bijvoorbeeld het commando `motor_aan(10, 1)` de robot achteruit laat rijden. De functie `motor_enkel()` heeft dan dus drie parameters: welke motor, de snelheid, en de richting.  

## Lampen 

Met de functie `headlights()` kun je de lampen van de robot besturen. De functie heeft twee parameters: de lamp (led_links, led_rechts of led_beide) en de staat (aan of uit). Om het commando te geven dat beide lampen aan moeten, roep je de functie dus aan via headlights(led_beide, aan). 

## Random getallen 

Soms is het handig als de robot willekeurig een bepaalde actie doet. Dit maakt de robot minder voorspelbaar, waardoor hij sneller intelligenter overkomt. Om random getallen te gebruiken kun je een variabele maken die je random een getal toewijst.  Hiervoor moet je eerst de bijbehorende package importeren. Vervolgens kun je willekeurig een getal toewijzen. De random-functie heeft twee parameters: de laagste en de hoogste waarde die toegewezen mag worden. Aanroepen van de functie ziet er dan als volgt uit: 

	# Imports go at the top
	from maqueen import *
	from random import randint
	
	random_getal = randint(0, 100)

Aan de variabele random_getal wordt nu willekeurig een waarde toegekend tussen de 0 en 100. 

## Opdrachten hoofdstuk 3 

1. Leg uit wat het verschil is tussen integer- en boolvariabelen. 

2. Wat is een void-functie en wanneer gebruik je deze? 

3. Zoek in het `maqueen.py` bestand op wat de standaard meegegeven snelheid van de robot is.  

4. Laat de robot naar links draaien met de linker lamp aan. Doe vervolgens hetzelfde voor de rechter kant. 

5. Laat de robot rijden in een cirkel met een straal van minimaal 20cm (dus niet om zijn eigen as). 

6. Laat de robot vooruitrijden met een snelheid van 10 terwijl hij de lampen aan heeft. Doe dit voor 5 seconde. Zet vervolgens de lampen uit en laat de robot voor nog 5 seconde naar achter rijde.  

7. Schrijf een functie die op de simulator een smiley met een willekeurige gezichtsuitdrukking meegeeft. Gebruik hiervoor de random-functie.  

8. Laat de robot willekeurig rondrijden, dus vooruit, achteruit, en draaien. Gebruik hiervoor de random-functie.