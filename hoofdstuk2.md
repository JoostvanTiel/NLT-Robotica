# Hoofdstuk 2: Kennismaken met de robot

In dit hoofdstuk gaan we aan de slag met de Micro:bit Maqueen. 
Allereerst zullen we hiervoor voorgeprogrammeerde functies importeren 
in het programma. Die zullen je helpen bij het aanroepen van de robot. 
Vervolgens zullen we eerst de Micro:bit aansluiten, om deze vervolgens 
te koppelen aan de Maqueen. Om de Maqueen aan te roepen, zullen we 
verschillende functies bekijken. Aan het einde van dit hoofdstuk kun je 
de robot zelfstandig laten rijden.

## Importeren

Om de voorgeprogrammeerde map te importeren zorg je allereerst dat de 
set-up op de computer is opgeslagen. Deze set-up heeft het bestandstype
.hex. Hierbij krijg je hulp van je docent. Vervolgens ga je naar
“project” en druk je op “open”. Je opent nu het .hex bestand. Dit zal er
ongeveer als volgt uitzien: 

![screenshot imports](/img/h2.1.png)

Met de gegevens in de map “macqueen.py” hoef je in principe niks te doen, tenzij dit expliciet wordt vermeld of tenzij je de gegevens, bijvoorbeeld voor je eindproject, zelf wilt aanpassen. Je eigen code schrijf je dus in de map `main.py`. Hierin staat nu slechts de code die de map `macqueen.py` importeert en een regel die de verbinding met de robot initialiseert. Mocht je op een later moment een eigen functiemap toevoegen, denk er dan ook aan dat je deze importeert bovenaan je `main.py` bestand.  

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

Om de robot aan te sturen, verstuur je een code naar de micro:bit en plug je deze vervolgens in de Maqueen. We laten de motor rijden door middel van de functie `motor_aan()`. 

	# Imports go at the top
	from maqueen import *
	from microbit import *
	
	# Initialiseer de verbinding tussen de micro:bit en alle sensoren van Maqueen
	init_maqueen()
	
	motor_aan()
	

Stop de micro:bit in de Macqueen, zodat de opstelling er als volgt uitziet:

![image maqueen](/img/h2.6.png)

Zorg dat de Maqueen uit staat (met de aanknop op de rechter zijkant, rood omcirkelt in de figuur hierboven) en verbindt de computer door middel van de micro-USB kabel met de micro:bit. Vervolgens verstuur je de code naar de micro:bit. Als dit is gelukt haal je de USB kabel uit de micro:bit en zet je de Maqueen aan. Had je de Maqueen al aanstaan bij het verbinden, of haal je de kabel niet uit de micro:bit, dan gaat de robot rijden met de kabel nog aangesloten. Dit is niet de bedoeling.

## Meer functies

Tot nu toe hebben we enkel de functie `motor_aan()` gebruikt om de Maqueen te besturen. Het is ook fijn als je de motor na enige tijd weer uit kunt zetten. Hiervoor maak je gebruik van de functie `motor_uit()`. Als je de while-loop vervolgens wil stoppen, kun je dit doen door middel van het commando `break`.

	# Imports go at the top
	from maqueen import *
	from microbit import *
	
	# Initialiseer de verbinding tussen de micro:bit en alle sensoren van Maqueen
	init_maqueen()
	
	# Laat de robot 2 seconden rijden en vervolgens stoppen
	while True:
		motor_aan()
		sleep(2000)
		motor_uit()
		break

De functie `motor_aan()` stuurt zowel de motor van het linker als het rechter wiel aan. Als je wil dat de robot een bocht maakt, kan het zijn dat je slechts één van de twee wielen wilt aansturen. Om dit te doen gebruik je de functie `motor_enkel()`. In dit geval moet je wel aangeven welk van de twee motoren je wilt aansturen. Dit zet je tussen de haakjes. Dit ziet er als volgt uit: `motor_enkel(motor_links)`.

## Opdrachten hoofdstuk 2

1. Importeer het set-up bestand “Maqueen setup v3 1.hex”. Verander vervolgens de naam van je project.  

2. Zorg dat de standaard code van hoofdstuk 1 wordt uitgevoerd op de micro:bit.  

3. Schrijf een code die ervoor zorgt dat “A” wordt getoond op het moment dat je toets A indrukt op de micro:bit en “B” als je toets B indrukt. 

4. Laat de Maqueen voor een tijdsduur van 3 seconde naar voren rijden.  

5. Zorg ervoor de de Maqueen rondjes draait om zijn as.  

6. Schrijf een code die ervoor zorgt dat de Maqueen 2 seconde naar rechts draait en en vervolgens voor 2 seconde naar links draait . 

7. Zorg ervoor dat de Maqueen 3 seconde naar voren rijdt, dan een bocht naar links maakt, en vervolgens weer 3 seconde verder rijdt.  