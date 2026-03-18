# Hoofdstuk 3: Sensoren

Robots zijn uitgerust met sensoren zoals afstandssensor, geluidsensor, kleurensensor, bewegingssensor, enzovoort. Via deze sensoren kunnen robots hun omgeving observeren, waardoor een robot autonoom kan functioneren. In dit hoofdstuk behandelen we hoe je de lijnvolgsensoren en de ultrasone afstandssensor van de maqueen kunt gebruiken.

## De lijnvolgsensoren

In de onderstaande figuur zie je de vijf lijnsensoren die op de maqueen aanwezig zijn. Elke sensor heeft een infrarood (IR) zender en een IR ontvanger. De IR zender zend infrarode straling uit. Die straling wordt door een witte ondergrond weerkaatst, maar door een zwarte ondergrond geabsorbeerd. Als de IR ontvanger teruggekaatste straling ontvangt (witte ondergrond), zal deze een hoge waarde terugsturen naar de micro:bit. Als het geen straling ontvangt, stuurt het een lage waarde terug naar de micro:bit.

![lijnvolgsensoren onderaanzicht](/img/h3.1.png)

```{image} /img/h3.2.png
:alt: screenshot microbit verbinden
:width: 200px
:align: right
```

Als de robot over een zwarte lijn rijdt, met aan weerszijden een witte ondergrond, zullen een de lijnvolgsensoren boven de witte ondergrond een hoge waarde terugsturen en de lijnvolgsensoren boven de lijn een lage waarde. Op die manier kan vastgesteld worden waar de lijn zich onder de robot bevindt. Zie ook de figuur hiernaast.

De vijf lijnsensoren van de Maqueen zijn van links naar rechts als volgt genoemd: `l2`, `l1`, `m`, `r1`, `r2`.

De volgende pseudocode omschrijft hoe een lijnvolgprogramma eruit zou kunnen zien:

    # Lees de lijnsensoren uit

    # Als de middelste lijnsensor (m) een lage waarde stuurt:
    	# Rijd vooruit
    # Anders, als linker lijnsensor (l1 of l2) een lage waarde stuurt:
    	# Draai naar links
    # Anders, als rechter lijnsensor (r1 of r2) een lage waarde stuurt:
    	# Draai naar rechts

In de situatie van de bovenstaande afbeelding zal `r1` een lage waarde terugsturen en moet de robot dus naar rechts draaien.

Om de waarde van een lijnvolgsensor te krijgen, kan de volgende functie worden gebruikt:
lees_lijnsensor(sensor) # Op de plaats van sensor moet de naam van de sensor komen te staan (l2, l1, m, r1 of r2)

## De ultrasone afstandssensor

Een andere sensor waarover de Maqueen beschikt, is de ultrasone afstandssensor. Door deze sensor lijkt het net alsof de robot twee ogen heeft. In tegenstelling tot ogen, gebruikt deze sensor geen licht, maar ultrasoon geluid om te bepalen of er zich een voorwerp voor de robot bevindt. Met het linker "oog", de verzender (transmitter - T), verstuurt de sensor een ultrasoon geluidssignaal. Dat signaal beweegt zich met de snelheid van het geluid voort en zal tegen een voorwerp weerkaatsen. Het rechter "oog", de ontvanger (receiver - R), vangt het weerkaatste signaal op. Uit het tijdsverschil en de snelheid van het geluid, kan dan berekend worden op welke afstand het voorwerp zich van de robot bevond. Zie ook de schematische tekening hieronder.

![werking US sensor](/img/h3.3.png)

Om de afstand vanaf de US sensor te krijgen, wordt de functie `afstand_tot_voorwerp()` gebruikt. Deze functie retourneert de afstand in **cm**.

## Opdrachten hoofdstuk 3

1. Schrijf een programma waarbij de waarde van lijnsensor `m` op het scherm van de micro:bit toont. Gebruik de functie `sleep()` om te zorgen dat de waarde niet te snel verandert en gebruik `display.clear()` om het scherm een tijdje leeg te maken, zodat je weet welke getallen bij elkaar horen.
2. Kalibreer de lijnsensoren: onderzoek met behulp van de code van de vorige opdracht welke waardes de lijnsensoren meten als ze boven een wit oppervlakte staan en welke waardes als ze boven een zwart oppervlakte staan. Schrijf deze waardes ergens op, je gaat ze in de volgende hoofdstukken vaak nodig hebben.
3. Klik in het linkermenu op 'Project' en zoek in het bestand `maqueen.py` op wat de snelheid van het geluid is die de Ultrasone Afstandssensor gebruikt om de afstand te berekenen.
4. Schrijf een programma dat de afstand tot de ultrasone afstandssensor op het scherm van de micro:bit toont.
5. Onderzoek met behulp van de vorige opdracht wat de maximale afstand is die de maqueen kan waarnemen met de ultrasone afstandssensor.
