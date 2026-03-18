# Hoofdstuk 7: Eindopdracht - Doolhofchallenge

In de vorige hoofdstukken heb je stap voor stap geleerd hoe je de Maqueen bestuurt met:

- motorfuncties;
- sensoren (`lees_lijnsensor(...)` en `afstand_tot_voorwerp()`);
- condities;
- functies;
- loops.

In dit hoofdstuk combineer je alles in een eindopdracht: een doolhof met bochten, kruispunten en doodlopende wegen.

## Doel van de eindopdracht

Je maakt een programma dat:

1. binnen de lijnen van het doolhof blijft;
2. kruispunten en doodlopende wegen herkent;
3. met eigen logica keuzes maakt;
4. meerdere gemarkeerde vakken in het doolhof vindt.

Belangrijk: je krijgt hieronder geen complete kant-en-klare oplossing. Je werkt er in stappen naartoe en bedenkt zelf de strategie.

## Opstelling van het doolhof

Maak met je groep een doolhof op een wit A2- of groter vel met zwarte tape.

Gebruik minimaal:

- 1 startvak;
- 1 eindvak;
- 3 gemarkeerde vakken (bijvoorbeeld met kleursticker);
- 2 kruispunten;
- 2 doodlopende wegen.

Zorg dat de lijnen breed genoeg zijn voor betrouwbare detectie met de lijnsensoren.

## Nieuwe situaties in het doolhof

### Doodlopende weg

Een doodlopende weg is een pad waar je niet verder kunt zonder terug te gaan.

Denkvraag:

- Hoe kun je met lijnsensoren en/of afstandssensor herkennen dat je vastloopt?
- Welke manoeuvre heb je nodig om netjes terug te keren naar de vorige splitsing?

### Kruispunt

Een kruispunt is een plek waar meerdere richtingen mogelijk zijn.

Denkvraag:

- Wanneer noem je iets een kruispunt in sensorwaarden?
- Welke keuzevolgorde gebruik je (bijvoorbeeld links-eerst, rechts-eerst, of iets anders)?
- Hoe voorkom je dat je eindeloos blijft rondjes rijden?

## Van idee naar logica

Voordat je code schrijft, maak eerst een overzicht van alle mogelijke situaties die de robot tegen kan komen. Maak vervolgens een beslisboom op papier en zet die beslisboom om in pseudocode.

Voorbeeld van een beslisboom:

```text
[Start loop]
   |
   v
[Obstakel dichtbij?] -- ja --> [Stop of ontwijk] --> [Terug naar start loop]
   |
    nee
   v
[Kruispunt?] --------- ja --> [Kies richting volgens jouw regel] --> [Terug naar start loop]
   |
    nee
   v
[Doodlopende weg?] --- ja --> [Keer om] --> [Terug naar start loop]
   |
    nee
   v
[Volg de lijn] -------------------------------> [Terug naar start loop]
```

Tip: bouw dit op met kleine hulpfuncties, bijvoorbeeld:

- `op_lijn()`;
- `is_kruispunt()`;
- `is_doodlopend()`;
- `kies_richting()`.

## Opdrachten hoofdstuk 7

Werk deze opdrachten in volgorde uit. Stop pas met een opdracht als deze stabiel werkt.

1. Basiscontrole
   - Laat de robot een rechte lijn en een enkele bocht betrouwbaar volgen.
   - Gebruik jouw gekalibreerde drempelwaarde uit hoofdstuk 3.

2. Kruispunt detecteren
   - Schrijf code die een kruispunt herkent.
   - Laat op de micro:bit zien wanneer een kruispunt gedetecteerd is (bijvoorbeeld met een icoon of letter).

3. Doodlopende weg detecteren
   - Schrijf code die een doodlopende weg herkent.
   - Laat de robot omkeren en terugrijden tot het vorige keuzepunt.

4. Keuzelogica ontwerpen
   - Kies een vaste strategie (bijvoorbeeld links-eerst of rechts-eerst).
   - Leg in 4-6 regels uit waarom je voor deze strategie kiest.

5. Keuzelogica programmeren
   - Programmeer je strategie op kruispunten.
   - Zorg dat de robot na een keuze weer netjes op de lijn komt.

6. Geheugen toevoegen
   - Gebruik minstens 1 variabele om bij te houden wat de robot al gedaan heeft.
   - Voorbeelden: aantal kruispunten, aantal omkeringen, gevonden vakken.

7. Gemarkeerde vakken vinden
   - Laat de robot detecteren wanneer een gemarkeerd vak bereikt is.
   - Tel op hoeveel vakken gevonden zijn.

8. Stopvoorwaarde
   - Stop het programma pas als alle 3 de gemarkeerde vakken gevonden zijn.
   - Geef dit duidelijk aan (bijvoorbeeld met tekst, icoon, lampen of pieptoon).

9. Robuustheidstest
   - Laat het programma 3 keer achter elkaar starten vanuit hetzelfde startpunt.
   - Noteer per run wat goed ging en wat nog fout ging.

10. Verbeterronde
    - Verbeter je code op basis van je testresultaten.
    - Beschrijf minimaal 2 concrete verbeteringen die je hebt gedaan.

## Eindopdracht

Laat je robot zelfstandig door het doolhof rijden en de 3 gemarkeerde vakken vinden.

Voorwaarden:

- De robot blijft binnen het doolhof.
- De robot kan omgaan met kruispunten.
- De robot kan uit doodlopende wegen terugkomen.
- De robot stopt wanneer alle 3 vakken gevonden zijn.

## Beoordelingsrubric

| Onderdeel                     | Onvoldoende                                                                                                                         | Voldoende                                                                                                   | Goed                                                                                               | Score                  |
| :---------------------------- | :---------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------- | :--------------------- |
| Voldoen aan minimale opdracht | Rijdt het veld in en blijft binnen de lijnen.                                                                                       | Vindt de gekleurde vakken en stopt wanneer alle drie de vakken gevonden zijn. Ook brandt er dan een lampje. | Print een boodschap naar het scherm en laat een pieptoon horen wanneer alle kleuren gevonden zijn. |                        |
| Kwaliteit software            | Gebruikt `#define`-achtige vaste waarden. Gebruikt commentaar. Nette inspringing.                                                   | Zinvol gebruik van `if/while/until/repeat`. Zinvol gebruik van variabelen. Gebruikt functies.               | Zinvol gebruik van meerdere functies.                                                              |                        |
| Extra opdracht                | Zinvol gebruik van US-sensor. Zinvol gebruik van druksensor.                                                                        | Communicatie tussen twee robots. Oppakken van voorwerpen.                                                   | Eigen initiatief.                                                                                  |                        |
| Proces en eigen inzicht       | **Onvoldoende (max -1p):** verstoort het onderwijsproces, oneigenlijk gebruik van laptop/pc, storend gebruik mobiele telefoon, etc. | **Voldoende (0p):** actieve participatie, eigen inzicht.                                                    | **Goed (1p):** opmerkelijke groei, sterk eigen inzicht.                                            |                        |
| Totaal                        |                                                                                                                                     |                                                                                                             |                                                                                                    | Cijfer = aantal punten |
