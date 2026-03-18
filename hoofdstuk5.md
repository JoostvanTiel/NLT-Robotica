# Hoofdstuk 5: Functies en variabelen

In de afgelopen twee hoofdstukken zijn we meerdere functies tegengekomen. In dit hoofdstuk gaan we dieper in op wat functies zijn en hoe je ze gebruikt. Hiervoor moeten we weten wat voor soorten functies en wat voor soorten variabelen er zijn. We zullen de belangrijkste in dit hoofdstuk bespreken. Daarna gaan we kijken naar de werking van verschillende functies die je kunt aanroepen om de Maqueen te besturen.

## Functies

In het vorige hoofdstuk zijn we het commando `motor_aan()` tegengekomen. Dit is een voorbeeld van een functie. Je kunt een functie herkennen aan de haakjes die achter het commando staan. Functies gebruik je vooral bij langere codes, omdat die anders snel onoverzichtelijk worden. Je splitst in dit geval je code op in verschillende kleinere programma’s (de functies). Zo kun je complexere programma’s overzichtelijk en makkelijk te begrijpen houden. Verder kunnen functies ook helpen om geheugen te besparen, omdat je een bepaalde functie meerdere keren kunt aanroepen. Je kunt deze functies vergelijken als een functie in de wiskunde. Je stopt er iets in (invoer), de functie verwerkt dat, en je krijgt er weer iets uit (uitvoer).

Naast de functies die we al zijn tegengekomen, en alle functies die in het bestand `maqueen.py` staan, kun je ook je eigen functies schrijven. Een voorbeeld van een simpele functie is:

    def op_lijn(lijnsensor):
        """
            controleert of de doorgegeven lijnsensor de lijn ziet
            parameters:
                lijnsensor - welke sensor je wilt checken (l2, l1, m, r1 of r2)
            returnwaarde: True als de sensor boven de lijn staat, anders False
        """
        drempelwaarde = 150 # De gekalibreerde waarde uit hoofdstuk 2, opdracht 2
        sensorwaarde = lees_lijnsensor(lijnsensor)

        if sensorwaarde < drempelwaarde:
            return True
        else:
            return False

Je ziet dat de code begint met eerst in commentaar uitleggen wat de functie doet, welke waardes hij meekrijgt en wat hij oplevert. Dit moet je er altijd bij schrijven als je een functie maakt. Zo blijft het altijd duidelijk wat welke functie doet. Om de functie te schrijven begin je altijd met def . Hiermee vertel je aan het programma dat je een functie gaat definiëren. Daarna geef je de functie een naam en zet je tussen haakjes de parameters.
Je kunt de bovenstaande functie op de volgende manier gebruiken:
from maqueen import _
from microbit import _

    init_maqueen()

    if op_lijn(m):
        motor_links(aan, snelheid=80)
        motor_rechts(aan, snelheid=80)
    else:
        motor_links(uit)
        motor_rechts(uit)

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

Soms wil je ook functies maken die geen variabele oplevert. In zo’n geval gebruik je een void-functie. Het type void geeft aan dat de functie geen resultaat heeft. We zijn in deze module al veel void-functies tegen gekomen. Bijvoorbeeld de functie `motor_aan()`, maar ook de functie `display.show(Image.HEART)` hebben geen returnwaarde. In het laatste voorbeeld zie je dat ook void-functies parameters kunnen bevatten. Hoewel ze geen returnwaarde hebben, kunnen ze wel een actie in gang zetten.

## Variabelen

In een functie vul je parameters in. Deze parameters zijn variabelen, en kunnen dus verschillende waarden aannemen. Variabelen kunnen van verschillende datatypen zijn. Het is belangrijk dat je variabelen van het correcte datatype meegeeft aan een functie. Probeer een variabele altijd een naam te geven, waaruit je kan opmaken wat er in opgeslagen wordt. Er zijn vier regels voor de naamgeving van een variabele in Python:

1. Er mogen alleen letters, getallen en underscores (\_) gebruikt worden in de naam van de variabele.
2. Een variabelenaam mag **niet** starten met een getal (8eruit mag dus niet)
3. Variabelenamen zijn hoofdlettergevoelig (op_lijn en op_Lijn zijn verschillend)
4. Gereserveerde namen, zoals if, else, def en for zijn verboden.

In Python krijgt een variabele automatisch het datatype van hetgeen je hem meegeeft. Je kent iets toe aan een variabele door het gebruik van één `=` teken. Dit betekent “krijgt de waarde”. Een dubbel `==` teken is een vergelijking. Er wordt dan nagegaan of voor en na de `==` hetzelfde staat. De meeste gebruikte datatypen zijn

    integer	# een geheel getal
    bool	# True of False
    float	# decimaal getal
    string	# tekst

### integer

De integer variabele gebruik je om gehele getallen in op te slaan. Je kan er bijvoorbeeld mee bijhouden hoe vaak je een object hebt gezien. Een voorbeeld van een toekenning is

    aantal_objecten = 5

Als je de variabele wilt gebruiken kun je de variabele aanroepen door de naam te gebruiken. In dit geval is dat ‘x’. Je kunt de variabele als volgt gebruiken:

    x = 5 * 2
    x = x * 2

Bij de tweede regel gebruik je de oude waarde van x, om de nieuwe waarde te berekenen. In de eerste regel heeft x de waarde 10. In de tweede regel wordt dus 10 ingevuld voor x. Zo komt er te staan: x = 10 \* 2. De waarde van x wordt dan 20. De functie Oppervlakte is een voorbeeld van een functie met parameters van datatype integer.

### bool

Bool is de afkorting van boolean. Boolean betekent dat het maar 2 waardes kan hebben, waar of niet waar. In een programmeertaal wordt daarvoor `true` en `false` gebruikt. De bool variabele gebruik je bijvoorbeeld om op te slaan of je iets al gedaan of gezien hebt. We zijn hem al vaker tegengekomen in de vorm `while True`. Je kunt hem bijvoorbeeld gebruiken om aan te geven dat je iets al een keer bent tegengekomen. Zo kun je de while-loop afbreken die we in eerdere hoofdstukken gezien hebben. Een voorbeeld hiervan is:

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

In een float-variabele kun je een decimaal opslaan. Dit kan handig zijn als je waardes nauwkeurig wilt bepalen. Als je getallen gebruikt van het type integer voor een berekening, wordt de waarde namelijk afgerond op gehele getallen. Om dit te voorkomen gebruiken we het type float. Dit doe je door een decimaal getal in te vullen. Met een float kun je verder dezelfde dingen doen als met een int-variabele.
Pas op! Je moet hier een punt gebruiken en geen komma. Anders zul je een error te zien krijgen. `pi=3,1415` is dus fout en moet worden: `pi = 3.1415`.

### string

In een string-variabele kun je een woord of hele zin opslaan. Een string kun je bijvoorbeeld gebruiken om een zin op het schermpje van de robot te zetten. We hebben deze bijvoorbeeld eerder gezien in de vorm `Display.scroll("Hello")`. Een string zet je altijd tussen aanhalingstekens. De functie `Display.scroll()` kan dus alleen parameters verwerken met datatype string.

## Extra functies van de robot

Naast de functies van de motoren en het uitlezen van de lijnsensoren en de ultrasone afstandssensor, bestaan er nog een paar functies om de robot extra leuke dingen te laten doen.

## Lampen

Met de functie `koplampen()` kun je de lampen van de robot besturen. De functie heeft twee parameters: de lamp (led_links, led_rechts of led_beide) en de staat (aan of uit). Om het commando te geven dat beide lampen aan moeten, roep je de functie dus aan via headlights(led_beide, aan).

## Underglow

Je kunt een mooi effect creëeren door de underglow van de robot te gebruiken. Hiervoor gebruik je de functie `set_underglow()`. In deze functie moet de kleur van de underglow als parameter worden doorgegeven. In `maqueen.py` staan een aantal kleuren gedefinieerd als variabelen, maar het is ook mogelijk om zelf een kleur te definiëren.
De kleuren van de underglow maken gebruik van de hexadecimale getallencode voor kleuren. Om een kleur te definiëren type je eerst `0x`. Daarachter komen zes tekens, waarbij de eerste twee tekens staan voor de hoeveelheid rood in de kleur, de volgende twee tekens staan voor de hoeveelheid groen en de laatste twee tekens staan voor de hoeveelheid blauw.

Kies hieronder een kleur en lees de hexadecimale waarde af:

<label for="kleurkiezer"><strong>Kleur:</strong></label>
<input id="kleurkiezer" type="color" value="#00ffcc" oninput="document.getElementById('hexwaarde').value = this.value.toUpperCase();">
<label for="hexwaarde"><strong>Hex:</strong></label>
<input id="hexwaarde" type="text" value="#00FFCC" readonly style="width: 110px;">

Voor de Maqueen gebruik je dezelfde kleur dan als `0x00FFCC` (dus met `0x` in plaats van `#`).

Werkt de picker niet goed in je browser? Gebruik dan deze website:
[W3Schools Color Picker](https://www.w3schools.com/colors/colors_picker.asp)

## Random getallen

Soms is het handig als de robot willekeurig een bepaalde actie doet. Dit maakt de robot minder voorspelbaar, waardoor hij sneller intelligenter overkomt. Om random getallen te gebruiken kun je een variabele maken die je random een getal toewijst. Hiervoor moet je eerst de bijbehorende package importeren. Vervolgens kun je willekeurig een getal toewijzen. De random-functie heeft twee parameters: de laagste en de hoogste waarde die toegewezen mag worden. Aanroepen van de functie ziet er dan als volgt uit:

    # Imports go at the top
    from maqueen import *
    from random import randint

    random_getal = randint(0, 100)

Aan de variabele random_getal wordt nu willekeurig een waarde toegekend tussen de 0 en 100.

## Opdrachten hoofdstuk 5

1.  Leg in je eigen woorden uit:
    - wat een functie is;
    - wat een parameter is;
    - wat een returnwaarde is.

2.  Geef van elk datatype een voorbeeldvariabele en waarde:
    - integer;
    - bool;
    - float;
    - string.

3.  Wat is het datatype van de returnwaarde van `lees_lijnsensor(m)`? Leg kort uit hoe je dat weet.

4.  Bekijk de functie hieronder:

          def blokkade():
                if afstand_tot_voorwerp() < 15:
                     return True
                else:
                     return False

    - Welk datatype wordt teruggegeven?
    - Schrijf een kort programma dat deze functie gebruikt om de robot te laten stoppen of rijden.

5.  Schrijf een eigen functie `rij_rechtdoor(snelheid, tijd_ms)` die:
    - beide motoren vooruit laat rijden op de opgegeven snelheid;
    - na `tijd_ms` milliseconden stopt.

6.  Schrijf een void-functie `draai_links(snelheid, tijd_ms)` en een void-functie `draai_rechts(snelheid, tijd_ms)`.
    - Laat daarna de robot het volgende patroon rijden door deze functies slim te combineren.
      ![Patroon](/img/h5.1.png)

7.  Schrijf een functie `veilig_rijden(snelheid)` die alleen rijdt als de afstand groter is dan 20 cm.
    - Gebruik `afstand_tot_voorwerp()`.
    - Laat de functie `True` teruggeven als er gereden wordt, anders `False`.

8.  Gebruik de functie `koplampen()`:
    - laat de robot 2 seconden naar links draaien met de linker lamp aan;
    - laat daarna 2 seconden naar rechts draaien met de rechter lamp aan;
    - zet daarna beide lampen uit.

9.  Gebruik `set_underglow()`:
    - kies drie verschillende kleuren;
    - toon elke kleur 1 seconde;
    - eindig met onderglow uit.

10. Maak op het A2 vel van jou en je partner een bocht (hoek van ongeveer 90 graden) naar links, laat die weg een stukje doorlopen en maak vervolgens een bocht naar rechts. Schrijf een programma dat de robot een bocht laat nemen als hij deze tegenkomt.

11. Extra: schrijf een functie `willekeurige_actie()` die een getal kiest tussen 1 en 4 en dan:
    - vooruit rijdt;
    - achteruit rijdt;
    - links draait;
    - rechts draait.
