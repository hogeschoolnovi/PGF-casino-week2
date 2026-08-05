# Week 2 oplossing: Casino de Gouden Driehoek roulette tafel met spelregels

# We bouwen verder op het startbudget en de persoonsgegevens uit week 1. Deze variabelen heb je als het goed is al staan.
TICKET_PRICE = 10.00
CONSUMPTION_PRICE = 4.50
GAMBLING_TAX = 2.00
MIN_AGE = 18

name = input("Wat is je naam? ").capitalize()
birthdate = input("Wat is je geboortedatum? (dd-mm-yyyy) ")
gender = input("Wat is je gender? (m/v/x) ").strip().lower()
startbudget = float(input("Hoeveel geld neem je mee naar Casino de Gouden Driehoek? € "))
salutation = f"meneer {name}" if gender == "m" else f"mevrouw {name}" if gender == "v" else f"speler {name}"

total = TICKET_PRICE + CONSUMPTION_PRICE + GAMBLING_TAX
balance = startbudget - total
has_budget = total <= balance
conclusie = "Je hebt nog genoeg budget voor toegang tot het casino." if has_budget else "Je hebt niet voldoende budget voor toegang tot het casino."


# Leeftijdscontrole op basis van de geboortedatum uit week 1.
birth_day, birth_month, birth_year = birthdate.split("-")
age = 2026 - int(birth_year)
if age < MIN_AGE:
    print(f"\nSorry {salutation}, je moet 18 jaar of ouder zijn om deze applicatie te gebruiken.")
    exit(1)

# Deze printout is gelijk aan de printout van vorige week
print("\nCasino de Gouden Driehoek")
print("-" * 35)
print(f"Welkom, {salutation}")
print()
print(f"Startbudget:    € {startbudget:.2f}")
print(f"Vaste kosten:   € {total:.2f}")
print(f"Saldo:          € {balance:.2f}")
print()
print(conclusie)





# Nu volgt de logica voor het gok spel

# De roulette logica, zonder "random", in een loop.
# Round_number is belangrijk voor de wilekeur
round_number = 1
while True:
    # Als eerst toon je de gokopties. Uitgecommentarieerd zie je de uitwerking in een lus, daaronder zie je de simpele uitwerking.

    print("Kies één van de volgende opties:")

    # index = 1
    # while index < 5:
    #     if index == 1:
    #         option = "Rood"
    #     elif index == 2:
    #         option = "Zwart"
    #     elif index == 3:
    #         option = "Even"
    #     else:
    #         option = "Oneven"
    #     print(f"{index}. {option}")
    #     index += 1
    # print("0. Stop")

    print("1. Rood")
    print("2. Zwart")
    print("3. Even")
    print("4. Oneven")
    print("0. Stop")

    print()

    choice = int(input("Kies je gok (0 om te stoppen): "))

    if choice == 0:
        break

    # BONUS: valideer of de gebruiker een geldige invoer heeft gegeven.
    if choice < 1 or choice > 4:
        print("Ongeldige keuze, probeer opnieuw.\n")
        continue

    # Vraag hoeveel de gebruiker wil inzetten en check of dat valide is
    stake = float(input("Hoeveel wil je inzetten? € "))
    if stake <= 0:
        print("De inzet moet groter zijn dan 0.\n")
        continue
    if stake > balance:
        print("Je hebt niet genoeg saldo voor deze inzet.\n")
        continue
    # Als de inzet valide is, haal dit dan van de balance af.
    balance -= stake

    spin = (round_number * 7) % 37

    # Bepaal de kleur
    if spin == 0:
        color = "groen"
        odd_even = "geen"
    elif spin <= 18:
        if spin % 2 == 0:
            color = "zwart"
            odd_even = "even"
        else:
            color = "rood"
            odd_even = "oneven"
    else:
        if spin % 2 == 0:
            color = "rood"
            odd_even = "even"
        else:
            color = "zwart"
            odd_even = "oneven"

    # Bereken of de gebruiker gewonnen of verloren heeft
    win = False
    if choice == 1 and color == "rood":
        win = True
    elif choice == 2 and color == "zwart":
        win = True
    elif choice == 3 and odd_even == "even":
        win = True
    elif choice == 4 and odd_even == "oneven":
        win = True

    # Nu volgt de printout of de gebruiker gewonnen of verloren heeft.
    print(f"De bal valt op {color} ({spin}).")
    if win:
        balance += stake * 2
        print(f"Je wint € {stake:.2f}")
    else:
        print(f"Je verliest € {stake:.2f}")

    print(f"Nieuw saldo: € {balance:.2f}\n")

    # Vergeet niet om het rondenummer op te tellen, anders speel je elke ronde hetzelfde spel.
    round_number += 1

# Als laatste print je het eindsaldo van de gebruiker
print(f"Eindsaldo: € {balance:.2f}")
