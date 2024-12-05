# Witaj w No-Limit Texas Hold'em Poker-Money APP!

#Wersja nw jaka
#Program wpada w nieskonczona petle gdy poda sie mu niższe podbicie niż najwyższy zakład/poprzednie podbicie
import time

gracze = []
pieniadze = []
bets = []
temp_bets = []
pula = 0
small_blind = 0
big_blind = 0
karty_na_stole = 3
check_counter = 0
najwyzszyBet = 0

def wprowadz_blindy():
    global small_blind, big_blind
    small_blind = int(input("\nPodaj wartość małego blinda: "))
    big_blind = int(input("Podaj wartość dużego blinda: "))
    print("\n")

def dodaj_graczy():
    global gracze, pieniadze, bets
    liczbaGraczy = int(input("Podaj liczbę graczy: "))
    for gracz in range(liczbaGraczy):
        gracze.append(input(f"Podaj nazwę gracza {gracz + 1}: "))
        pieniadze.append(int(input(f"Ile pieniędzy ma {gracze[gracz]}? ")))
        bets.append(0)
        temp_bets.append(0)

def ustaw_blindy():
    global pula
    if len(gracze) > 1:
        pieniadze[0] -= small_blind
        # bets[0] += small_blind
        pula += small_blind
        pieniadze[1] -= big_blind
        # bets[1] += big_blind
        pula += big_blind
        print(f"Gracz {gracze[0]} postawił małego blinda, a gracz {gracze[1]} postawił dużego blinda\n")

def przesunIndexGraczy():
    pierwszyElemnt = gracze.pop(0)
    gracze.append(pierwszyElemnt)
    print("Gracze: ", gracze)

def wyrownajZaklad(id_gracza): # Oddzielna funkcja wywoływana gdy chcesz wyrownac ale nie przbijac zakladu
    global najwyzszyBet,pula
    if najwyzszyBet < pieniadze[id_gracza]:
        pieniadze[id_gracza] -= najwyzszyBet
        bets[id_gracza] += najwyzszyBet
        temp_bets[id_gracza] += najwyzszyBet
        pula += najwyzszyBet
        print(f"Wyrównano zakład! (suma twoich zakładów na stole to {bets[id_gracza]})\n")
    else:
        print(f"Wchodzisz all in z {pieniadze[id_gracza]}\n")
        bets[id_gracza] += pieniadze[id_gracza]
        temp_bets[id_gracza] += najwyzszyBet
        pula += pieniadze[id_gracza]
        pieniadze[id_gracza] = 0

def podbijZaklad(id_gracza, podbicie): # Oddzielna funkcja wywoływana gdy chcesz podbic zaklad
    global najwyzszyBet,pula,check_counter
    print(f"Przed wykonaniem funkcji najwyzszyBet: {najwyzszyBet}")
    if najwyzszyBet == 0:
        najwyzszyBet = podbicie
    else:
        najwyzszyBet += podbicie
    print(f"Po wykonaniu funkcji najwyzszyBet: {najwyzszyBet}")

    print(f"Najwyższy zakład wynosi: {najwyzszyBet}")

    if najwyzszyBet == pieniadze[id_gracza]:
        print(f"Gracz {gracze[id_gracza]} wchodzi all in za {pieniadze[id_gracza]}")
    if najwyzszyBet <= pieniadze[id_gracza]:
        pieniadze[id_gracza] -= najwyzszyBet
        bets[id_gracza] += najwyzszyBet
        temp_bets[id_gracza] += najwyzszyBet
        pula += najwyzszyBet
        print(f"Podbito o {najwyzszyBet} (suma twoich zakładów na stole to {bets[id_gracza]})\n")
        check_counter = 0

def check(id_gracza):
    global check_counter
    print(f"Gracz {gracze[id_gracza]} checkuje")
    check_counter += 1
    print(f"check_counter:{check_counter} \n")

def fold(id_gracza, passy):
    passy.append(id_gracza)
    print(f"Gracz {gracze[id_gracza]} passuje\n")

def akcje_gracza(id_gracza, passy):
    global najwyzszyBet, pula
    print(f"Aktualny gracz to {gracze[id_gracza]}")
    print(f"Aktualna pula na stole wynosi: {pula}")
    if najwyzszyBet == 0 or bets[id_gracza] == najwyzszyBet:
        wartosc = int(input(f"Twoje opcje to:\n"
                            f"1. Podnieś zakład(raise), 2. Sprawdz(check), 3. Pass(fold)\n"
                            f"Twoj zakład na stole wynosi: {temp_bets[id_gracza]}\n"
                            f"{gracze[id_gracza]} ({pieniadze[id_gracza]}): "))
        while wartosc not in [1, 2, 3]:
            print("Podano nieprawidłową opcję!")
            wartosc = int(input(f"{gracze[id_gracza]} ({pieniadze[id_gracza]}): "))
        if wartosc == 1:
            podbicie = int(input("Podaj o ile podbijasz: "))
            while podbicie > pieniadze[id_gracza]:
                print(f"Masz za mało pieniędzy na podbicie! Twoje pieniądze: {pieniadze[id_gracza]}")
                podbicie = int(input("Podaj o ile podbijasz: "))
            podbijZaklad(id_gracza,podbicie)
        elif wartosc == 2:
            check(id_gracza)
        elif wartosc == 3:
            fold(id_gracza, passy)

    elif bets[id_gracza] < najwyzszyBet:
        wartosc = int(input(f"Twoje opcje to:\n"
                            f"1. Podnieś zakład(raise), 2. Wyrownaj zakład(call), 3. Pass(fold)\n"
                            f"Aktualny najwyższy zakład to: {najwyzszyBet}\n"
                            f"Twój zakład na stole to: {temp_bets[id_gracza]}\n"
                            f"{gracze[id_gracza]} ({pieniadze[id_gracza]}): "))
        while wartosc not in [1, 2, 3]:
            print("Podano nieprawidłową opcję!")
            wartosc = int(input(f"{gracze[id_gracza]} ({pieniadze[id_gracza]}): "))
        if wartosc == 1:
            podbicie = int(input("Podaj o ile podbijasz: "))
            while podbicie > pieniadze[id_gracza]:
                print(f"Masz za mało pieniędzy na podbicie! Twoje pieniądze: {pieniadze[id_gracza]}")
                podbicie = int(input("Podaj o ile podbijasz: "))
                while podbicie < najwyzszyBet:
                    print(f"Podbicie musi być większe niż {najwyzszyBet}!")
                    podbicie = int(input("Podaj o ile podbijasz: "))
            podbijZaklad(id_gracza, podbicie)
        elif wartosc == 2:
            if pieniadze[id_gracza] < najwyzszyBet:
                print(f"Masz tylko {pieniadze[id_gracza]} żetonow. Czy chcesz wejsc all in?\n")
                czyWchodziszAllIn = int(input("1.Tak 2.Nie: "))
                while czyWchodziszAllIn not in [1, 2]:
                    print("Podano nieprawidłową opcję!")
                    czyWchodziszAllIn = int(input("1.Tak 2.Nie(Jesli nie wchodzisz all in to pasujesz): "))
                if czyWchodziszAllIn == 1:
                    wyrownajZaklad(id_gracza)
                elif czyWchodziszAllIn == 2:
                    fold(id_gracza, passy)
            else:
                wyrownajZaklad(id_gracza)
                check(id_gracza)
        elif wartosc == 3:
            fold(id_gracza, passy)
    else:
        print("Coś poszło nie tak")
        print(f"Twoje zakłady: {bets[id_gracza]}")
        print(bets)
        print(najwyzszyBet)
        print(pieniadze)
        print("\n")
        time.sleep(1000)

def sprawdzStanRundy():
    global pula, karty_na_stole, check_counter, najwyzszyBet
    if check_counter == len(gracze):
        print("Wykładaj kolejna karte na stół")
        karty_na_stole += 1
        check_counter = 0
        najwyzszyBet = 0
        for element in bets:
            element = 0
            print("Bety zostały wyzerowane")
    if karty_na_stole >= 5:
        print("5 kart na stole, czas na pokazanie rąk!")
        #twmp bwt zerowanie
        for element in temp_bets:
            element = 0
            print("Temp_Bety zostały wyzerowane")
        karty_na_stole = 3
        return False
    return True

def wybierz_zwyciezce():
    global pula
    print("Kto wygrał?")
    for i, zjeb in enumerate(gracze):
        print(f"{i+1}. {zjeb}")
    winner = int(input("\nZwycięzca: ")) - 1
    pieniadze[winner] += pula
    pula = 0
    for i in range(len(bets)):
        bets[i] = 0
    for i in range(len(pieniadze)):
        if pieniadze[i] == 0:
            print(f"Gracz {gracze[i]} zbankrutował i odpada z gry!")
            gracze.pop(i)
            pieniadze.pop(i)
            bets.pop(i)
            break

def gra():
    dodaj_graczy()
    wprowadz_blindy()
    while True:
        passy = []
        id_gracza = -1
        ustaw_blindy()
        while True:
            if len(passy) == len(gracze) - 1:
                break
            id_gracza += 1
            if id_gracza == len(gracze):
                id_gracza = 0
            if id_gracza in passy:
                id_gracza += 1
                continue
            akcje_gracza(id_gracza, passy)
            if not sprawdzStanRundy():
                break
            print(f"aktualne id gracza {id_gracza}")
        wybierz_zwyciezce()
        przesunIndexGraczy()
        if len(gracze) == 1:
            print(f"\n\nGratulacje {gracze[0]}! WYGRAŁEŚ {pieniadze[0]}!!!")
            break

if __name__ == "__main__":
    gra()