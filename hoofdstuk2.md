# Hoofdstuk 2: Kennismaken met de robot

In dit hoofdstuk gaan we aan de slag met de Micro:bit Maqueen. Allereerst zullen we hiervoor voorgeprogrammeerde functies importeren in het programma. Die zullen je helpen bij het aanroepen van de robot. Vervolgens zullen we eerst de Micro:bit aansluiten, om deze vervolgens te koppelen aan de Maqueen. Om de Maqueen aan te roepen, zullen we verschillende functies bekijken. Aan het einde van dit hoofdstuk kun je de robot zelfstandig laten rijden.

## Importeren

Om de voorgeprogrammeerde functies van de maqueen te gebruiken, heb je het bestand `maqueen.hex`nodig.
Download het bestand hier: {download}`maqueen.hex <maqueen.hex>`

Om dit bestand te openen ga je in het linkermenu naar “project” en druk je op “open”. Je opent nu het .hex bestand. Dit zal er ongeveer als volgt uitzien:

![screenshot imports](/img/h2.1.png)

Met de gegevens in het bestand `maqueen.py` hoef je in principe niks te doen, tenzij dit expliciet wordt vermeld of tenzij je de gegevens, bijvoorbeeld voor je eindproject, zelf wilt aanpassen. Je eigen code schrijf je dus in de map `main.py`. Hierin staat nu slechts de code die de map `macqueen.py` importeert en een regel die de verbinding met de robot initialiseert. Mocht je op een later moment een eigen functiemap toevoegen, denk er dan ook aan dat je deze importeert bovenaan je `main.py` bestand.

    # Imports go at the top
    from maqueen import *

    # Initialiseer de vebinding tussen de micro:bit en alle sensoren van Maqueen
    init_maqueen()

## De micro:bit

```{image} /img/h2.3.png
:alt: image micro:bit
:width: 250px
:align: right
```

Nu gaan we de computer aansluiten op de micro:bit. De micro:bit is een programmeerbaar computertje. Zie de afbeelding hiernaast.

We sluiten de micro:bit aan door middel van de micro-USB kabel. De micro:bit ziet er hetzelfde uit als de simulator. We kunnen dus gelijke codes gebruiken om de simulator en de micro:bit aan te sturen. Als je de code klaar hebt druk je op “Send to micro:bit”. Vervolgens krijg je twee schermen waarbij je beide op “next” drukt. Je selecteert vervolgens de micro:bit en klikt op “verbinding maken”. Je code wordt uitgevoerd op de micro:bit. Let op: dit werkt alleen in de browsers "[Chrome](https://www.google.com/chrome/)", "[Opera](https://www.opera.com/)" of "Edge".

```{image} /img/h2.4.png
:alt: screenshot microbit verbinden
:width: 400px
:align: center
```

## De robot Maqueen

Om de robot aan te sturen, verstuur je een code naar de micro:bit en plug je deze vervolgens in de Maqueen. We laten de motoren rijden door middel van de functies `motor_links(aan)` en `motor_rechts(aan)`.

    # Imports go at the top
    from maqueen import *
    from microbit import *

    # Initialiseer de verbinding tussen de micro:bit en alle sensoren van Maqueen
    init_maqueen()

    motor_links(aan)
    motor_rechts(aan)

Stop de micro:bit in de Macqueen, zodat de opstelling er als volgt uitziet:

![image maqueen](/img/h2.6.png)

Zorg dat de Maqueen uit staat (met de aanknop op de rechter zijkant, rood omcirkelt in de figuur hierboven) en verbindt de computer door middel van de micro-USB kabel met de micro:bit. Vervolgens verstuur je de code naar de micro:bit. Als dit is gelukt haal je de USB kabel uit de micro:bit en zet je de Maqueen aan. Had je de Maqueen al aanstaan bij het verbinden, of haal je de kabel niet uit de micro:bit, dan gaat de robot rijden met de kabel nog aangesloten. Dit is niet de bedoeling.

## De motor functies

De commando's `motor_links()` en `motor_rechts()` noemen we **functies**, dit kun je herkennen aan het haakje openen en sluiten achter het commando. Tussen de haakjes kun je meer informatie doorgeven met behulp van zogenaamde **parameters**.
Voor de functies `motor_links()` en `motor_rechts()` kunnen drie parameters doorgegeven kunnen worden:

1. De staat van de motor. Deze is verplicht om mee te geven. De staat kan `aan` of `uit` zijn. Bijvoorbeeld: `motor_links(aan)` om de linkermotor aan te zetten.
2. De snelheid van de motor. Deze waarde moet tussen de 0 en 255 liggen. Het doorgeven van de snelheid is optioneel. Als je niets doorgeeft, zoals bij het voorbeeld in het vorige punt, wordt de standaardwaarde 50 meegegeven. Als je de snelheid wel doorgeeft, moet deze ná de staat komen. Bijvoorbeeld: `motor_rechts(aan, snelheid=125)` om de rechtermotor aan te zetten met een snelheid van 125.
3. De richting waarin de motor draait. Hier kun je de richting op `vooruit` of `achteruit` zetten. Standaard staat deze waarde op `vooruit`. Als je de motor achteruit wil laten draaien, specificeer je de richting nadat je de snelheid hebt gespecificeerd. Bijvoorbeeld: `motor_links(aan, snelheid=75, richting=achteruit)`.

Er bestaan nog veel meer standaard functies om de maqueen aan te sturen en je kunt zelfs je eigen functies schrijven. Je leert hier meer over in [hoofdstuk 5](hoofdstuk5.md).

Als je de while-loop vervolgens wil stoppen, kun je dit doen door middel van het commando `break`. Je stopt dan het 'hoofdprogramma' op de robot.

    # Imports go at the top
    from maqueen import *
    from microbit import *

    # Initialiseer de verbinding tussen de micro:bit en alle sensoren van Maqueen
    init_maqueen()

    # Laat de robot 2 seconden rijden en vervolgens stoppen
    while True:
    	motor_links(aan)
        motor_rechts(aan)
    	sleep(2000)
    	motor_links(uit)
        motor_rechts(uit)
    	break

In deze code rijdt de robot een eindje rechtdoor. Als je wil dat de robot een bocht maakt, wil je dat slechts één van de twee wielen vooruit draait.

## Opdrachten hoofdstuk 2

1. Importeer het set-up bestand “maqueen.hex”. Verander vervolgens de naam van je project.
2. Zorg dat de code van opdracht 7 uit hoofdstuk 1 wordt uitgevoerd op de micro:bit.
3. Laat de Maqueen voor een tijdsduur van 3 seconde naar voren rijden.
4. Schrijf een code die ervoor zorgt dat de Maqueen 2 seconde naar rechts draait en en vervolgens voor 2 seconde naar links draait .
5. Zorg ervoor dat de Maqueen 3 seconde naar voren rijdt, dan een bocht naar links maakt, en vervolgens weer 3 seconde verder rijdt.
6. Zorg er op drie verschillende manier voor dat de Maqueen een rondje draait om zijn as (dus 360 graden).
   1. Door beide wielen vooruit te laten draaien, maar op een andere snelheid.
   2. Door één van de wielen aan te zetten.
   3. Door één van de wielen vooruit te laten draaien en de ander achteruit te laten draaien.
