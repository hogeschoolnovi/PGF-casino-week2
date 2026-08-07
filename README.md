# Week 2: Casino de Gouden Driehoek: roulette tafel 

## Inleiding
Vorige week heb je de eerste budgetcheck van Casino de Gouden Driehoek gemaakt. Deze week bouw je daarop verder met een leeftijdscheck en ga je een roulette spel implementeren waarbij de gebruiker meerdere rondes kan spelen.

## Opdracht beschrijving

### Leeftijd check

Als eerst ga je een leeftijdscheck bouwen. Dit doe je nadat je alle input van de gebruiker hebt gevraagd en voordat je de eerste printout doet. Je hebt de geboortedatum van de gebruiker al opgevraagd, deze kun je gemakkelijk opsplitsen in dag, maand en jaar met de `split()` functie. 

```python
birth_day, birth_month, birth_year = birthdate.split("-")
```

Vervolgens gebruik je `birth_year` om de huidige leeftijd te bepalen (dat hoeft niet op de dag of maand nauwkeurig).
Als dat minder dan 18 jaar geleden blijkt te zijn, dan print je een bericht dat de gebruiker geen gebruik mag maken van deze applicatie en sluit je af met de `exit(1)` functie. 
Als de leeftijd hoger dan 18 is, ga je verder met de applicatie en print je de printout van week 1.

**Let op:** 18 is zogenaamd een "magic number". Het is niet direct duidelijk wat dit nummer betekent. Bovendien, als je later besluit dat je toch 21 als grens wilt nemen, zul je alle verwijzingen van 18 in je code moeten opzoeken en wijzigen. Het is daarom handig om een `MIN_AGE` constante bovenaan je code te maken. Zo kun je direct zien wat dit nummer betekent en hoef je het maar op één plek aan te passen.

#### Fun fact
`exit(1)` sluit de applicatie af met "1" als exit code. Exit codes zijn een klassieke methodiek in het programmeren om aan te geven of een applicatie succesvol is uitgevoerd/afgesloten of niet. Elke niet-nul code betekent dat er een probleem was. Het maakt in feite dus niet uit of je `exit(1)` of `exit(666)` doet. Vaak heeft elke code een specifieke betekenis, zo zou "1" kunnen betekenen dat je niet oud genoeg bent, en "2" dat je niet genoeg geld hebt. De betekenis van elke code zou je in de documentatie moeten kunnen terugvinden. 

De exit code vind je uiteindelijk in de terminal, of in PyCharm met een tekst als `Process finished with exit code 1`.

### Roulette

In het tweede deel van deze huiswerkopdracht ga je een roulette spel maken. Zorg er in je code voor dat de speler deze functionaliteit herhaaldelijk kan blijven uitvoeren. De volgende beschrijving geldt zodoende voor elke iteratie van de functionaliteit.

Laat eerst de roulette-opties zien. Er zijn 5 opties: 
- 1 rood
- 2 zwart
- 3 even
- 4 oneven
- 0 stop

De speler kiest één van deze opties. Het is makkelijk om de nummers te laten zien zoals ze hierboven staan, zodat je de gebruiker het bijbehorende nummer kunt laten kiezen. Als de keuze `0` is, mag je meteen de while-loop afsluiten.

Daarna kiest de speler een inzet. Zet dit om naar een `float` en valideer het zodat:
- de inzet niet `0` of lager dan `0` is.
- de inzet niet hoger is dan het bedrag op de rekening van de gebruiker.

Als één van deze condities niet voldaan wordt, mag je de while-loop opnieuw beginnen.
Als beide condities wel voldaan worden, update dan de rekening van de gebruiker.

Voordat we het spel kunnen beginnen, moeten we eerst een semi-random nummer genereren om te bepalen op welk vlak het balletje gaat landen. Je mag hiervoor de `random` module gebruiken, maar aangezien we dat nog niet behandeld hebben doen we het als volgt: 

```python
spin = (round_number * 7) % 37
```

Daarbij is `round_number` een variabele die je vóór de while-loop hebt gedefinieerd en een waarde van `1` hebt gegeven. Vergeet niet om deze waarde elke iteratie van de while-loop te verhogen.

### De spelregels

De logica van het spel is afhankelijk van de `spin` variabele en de `choice` die de gebruiker heeft gemaakt. 
Je houdt verder nog twee variabelen bij: `color` en `odd_even`.
Als de `spin` variabele lager is dan of gelijk is aan 18, wordt de `color` bij een even spin zwart en bij een oneven spin rood. Is de spin echter hoger dan 18, dan wordt de `color` bij een even spin rood en bij een oneven spin zwart.

Vervolgens bepaal je of de speler heeft gewonnen of niet. Als de speler heeft gewonnen, krijgt deze speler de inzet dubbel uitgekeerd (de inleg + de winst). Heeft de speler verloren, dan krijgt de speler niks uitgekeerd.

Zorg dat je de speler laat weten of en hoeveel deze heeft gewonnen.
Je kunt de output bijvoorbeeld zo opbouwen:

```text
Wat is je naam? Jansen
Wat is je geboortedatum? (dd-mm-yyyy) 14-03-1984
Wat is je gender? (m/v/x) m
Hoeveel geld neem je mee naar Casino de Gouden Driehoek? € 100

Casino de Gouden Driehoek
-----------------------------------
Welkom, meneer Jansen

Startbudget:    € 100.00
Vaste kosten:   € 16.50
Saldo:          € 83.50

Je hebt nog genoeg budget voor toegang tot het casino.
Kies één van de volgende opties:
1. Rood
2. Zwart
3. Even
4. Oneven
0. Stop

Kies je gok (0 om te stoppen): 1
Hoeveel wil je inzetten? € 30
De bal valt op rood (7).
Je wint € 30.00
Nieuw saldo: € 113.50
```

## Randvoorwaarden
- Je stopt direct als de speler jonger is dan 18.
- Je gebruikt een `while`-lus zodat de speler meerdere roulette-rondes kan spelen.
- Je gebruikt een `if`/`elif`/`else`-structuur om gok keuzes en uitkomsten te bepalen in het roulettespel.
- Je gebruikt minimaal 1 `break` en minimaal 1 `continue`.
- Je vraagt een inzet van de gebruiker met `input()`.
- Je toont bij elke ronde of de speler wint of verliest en houdt het saldo up-to-date.
- Je laat aan het einde het saldo zien.

## Stappenplan
**Let op:** probeer deze opdracht eerst zelf op te lossen. Pas als dat niet lukt, mag je het stappenplan gebruiken.

1. Neem het startbudget en de persoonsgegevens van week 1 mee en laat de speler persoonlijk begroeten.
2. Gebruik de geboortedatum uit week 1 om de leeftijd van de speler te bepalen. Splits de geboortedatum op in dag, maand en jaar met `birth_day, birth_month, birth_year = birthdate.split("-")`. Vervolgens bereken je de leeftijd door bijvoorbeeld `2026 - int(birth_year)` te doen. Als laatste check je met `if age < 18` of de leeftijd onder de 18 is. Als dat het geval is print je een bericht waardoor de gebruiker weet dat deze geen gebruik mag maken van de applicatie en sluit je met `exit(1)` de applicatie af. 
3. Als de speler oud genoeg is, ga je verder met de applicatie en print je de tekst die je in week 1 ook geprint hebt. 
4. Voor je met het roulette spel begint, maar je eerst de variabele `round_number = 1`. Deze is belangrijk om straks te kunnen berekenen waar het balletje beland.
5. Gebruik een `while True`-lus zodat de speler meerdere rondes achter elkaar kan spelen. Alle volgende stappen komen in die lus (dus met een inspringing ervoor).
6. Print de opties die de gebruiker kan kiezen `1 rood, 2 zwart, 3 even, 4 oneven, 0 stop`. 
7. Laat de speler met `choice = int(input("Kies je gok (0 om te stoppen): "))` een gok kiezen en zet die keuze om naar een integer. 
8. Als die keuze `0` is, dan wil de gebruiker afsluiten. Doe dat met een `if` statement en een `break` statement. Een afscheidsbericht is op deze plek niet nodig. Wel mag je op het einde van het script, buiten de while-loop (zonder inspringing) het eindsaldo printen.
9. Vraag vervolgens met `input` en `float` hoeveel geld de gebruiker wil inzetten en sla dat op in een `stake` variabele.
10. Gebruik een `if`-statement om te checken of deze `stake` kleiner is dan of gelijk is aan `0`. Als dat zo is, mag je naar de gebruiker communiceren dat dit niet mag en gebruik je `continue` om het spel opnieuw te beginnen.
11. Gebruik ook een `if`-statement om te kijken of `stake` niet groter is dan de `balance` van de gebruiker. Als dat zo is, communiceer dan ook dat dit niet mag en gebruik `continue` om het spel opnieuw te beginnen.
12. Haal de inzet van het saldo af met `balance -= stake`.
13. Bepaal met `if`/`elif`/`else` wat de uitkomst van de ronde is en werk daarbij de spelregels van de roulette-tafel uit in code. Gebruik dit stroomschema daarbij als handleiding: 
```
Spin
├── Is 0?
│   ├── Ja
│   │   ├── Kleur: groen
│   │   └── Even/oneven: geen
│   └── Nee
│       └── Is kleiner dan of gelijk aan 18?
│           ├── Ja
│           │   └── Is even?
│           │       ├── Ja
│           │       │   ├── Kleur: zwart
│           │       │   └── Even/oneven: even
│           │       └── Nee
│           │           ├── Kleur: rood
│           │           └── Even/oneven: oneven
│           └── Nee
│               └── Is even?
│                   ├── Ja
│                   │   ├── Kleur: rood
│                   │   └── Even/oneven: even
│                   └── Nee
│                       ├── Kleur: zwart
│                       └── Even/oneven: oneven
```
14. Gebruik `if/elif` om te bepalen of de gebruiker gewonnen heeft. Als je begint met `win = False`, dan heb je geen `else` nodig. Gebruik het volgende waarheidstabel om je `if/elif` statements op te bouwen: 

| Keuze  | Spin                 | Win         |
|--------|----------------------|-------------|
| 1      | kleur = rood         | win = True  |
| 2      | kleur = zwart        | win = True  |
| 3      | even/oneven = even   | win = True  |
| 4      | even/oneven = oneven | win = True  |
| Anders | —                    | win = False |
15. Als de gebruiker heeft gewonnen (`if`-statement), dan tel je 2 keer de inzet bij de rekening van de gebruiker op en print je "Je wint {stake}".
16. Als de gebruiker heeft verloren (`else`), dan print je "Je verliest {stake}". 
17. Vergeet vooral niet om `round_number += 1` te doen. Dit doe je IN de while-loop. Als je dit niet doet, is elk spelletje hetzelfde.
18. Als laatste print je het eindsaldo en print je eventueel nog een afscheidsgroet. Dit doe je buiten de while-loop, dus zonder inspringing.

## Bonus
1. Wat gebeurt er als de gebruiker in het roulettespel niet 1, 2, 3, 4 of 0 kiest, maar 7? Los dit probleem op door te valideren dat de gebruiker een geldige keuze heeft gemaakt (tussen 0 en 4, incl.). Zo niet, dan begin je de while-loop opnieuw.
2. Bedenk een complexere puntentelling. We geven nu 2 keer de inzet terug, of je nou op kleur of op even/oneven inzet. Je kunt daar verschil in maken. Je kunt ook nog bepalen wat er gebeurt als je op groen inzet. En wat als je op een specifiek getal inzet? Wees hier lekker creatief mee!
3. We hebben nu een schijn-willekeur geïmplementeerd aan de hand van het ronde nummer. Probeer een echte (niet echt, maar daar hebben we het nu niet over) willekeur te implementeren door `random` te gebruiken.