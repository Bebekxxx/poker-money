import time

gracze = []
pieniadze = []
bets = []
temp_bets = []
passy = []
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
    print("\nBlindy zostały ustawione!\n")

def dodaj_graczy():
    global gracze, pieniadze, bets, temp_bets
    liczbaGraczy = int(input("Podaj liczbę graczy: "))
    for gracz in range(liczbaGraczy):
        gracze.append(input(f"Podaj nazwę gracza {gracz + 1}: "))
        pieniadze.append(int(input(f"Ile pieniędzy ma {gracze[gracz]}? ")))
        bets.append(0)
        temp_bets.append(0)

def ustaw_blindy():
    global pula, bets, najwyzszyBet
    if len(gracze) > 1:
        pieniadze[0] -= small_blind
        pula += small_blind

        pieniadze[1] -= big_blind
        pula += big_blind

        print(f"\nGracz {gracze[0]} postawił małego blinda ({small_blind}), a gracz {gracze[1]} postawił dużego blinda ({big_blind}).")
        print(f"Aktualna pula wynosi: {pula}\n")

def przesunIndexGraczy():
    global gracze, pieniadze, bets, temp_bets
    gracze.append(gracze.pop(0))
    pieniadze.append(pieniadze.pop(0))
    bets.append(bets.pop(0))
    temp_bets.append(temp_bets.pop(0))
    print("Nowa kolejność graczy:", gracze)

def wyrownajZaklad(id_gracza):
    global najwyzszyBet, pula
    kwota_do_wyrownania = najwyzszyBet - temp_bets[id_gracza]
    if kwota_do_wyrownania <= pieniadze[id_gracza]:
        pieniadze[id_gracza] -= kwota_do_wyrownania
        bets[id_gracza] += kwota_do_wyrownania
        temp_bets[id_gracza] += kwota_do_wyrownania
        pula += kwota_do_wyrownania
        print(f"Gracz {gracze[id_gracza]} wyrównał zakład o {kwota_do_wyrownania}!")
    else:
        print(f"Gracz {gracze[id_gracza]} wchodzi all-in z {pieniadze[id_gracza]}.")
        bets[id_gracza] += pieniadze[id_gracza]
        temp_bets[id_gracza] += pieniadze[id_gracza]
        pula += pieniadze[id_gracza]
        pieniadze[id_gracza] = 0

def podbijZaklad(id_gracza, podbicie):
    global najwyzszyBet, pula, check_counter
    kwota_do_wyrownania = najwyzszyBet - temp_bets[id_gracza]
    calkowita_kwota = kwota_do_wyrownania + podbicie
    pieniadze[id_gracza] -= calkowita_kwota
    bets[id_gracza] += calkowita_kwota
    temp_bets[id_gracza] += calkowita_kwota
    pula += calkowita_kwota
    najwyzszyBet += podbicie
    print(f"Gracz {gracze[id_gracza]} podbija zakład do {najwyzszyBet}.")
    check_counter = 0

def check(id_gracza):
    global check_counter
    print(f"Gracz {gracze[id_gracza]} checkuje.")
    check_counter += 1

def fold(id_gracza):
    global passy
    passy.append(id_gracza)
    print(f"Gracz {gracze[id_gracza]} passuje.\n")

def akcje_gracza(id_gracza):
    global najwyzszyBet, pula
    print(f"\n--- Tura gracza {gracze[id_gracza]} ---")
    print(f"Twoje pieniądze: {pieniadze[id_gracza]}")
    print(f"Aktualna pula: {pula}")
    print(f"Twój zakład na stole: {temp_bets[id_gracza]}")
    print(f"Najwyższy zakład wynosi: {najwyzszyBet}\n")

    if temp_bets[id_gracza] < najwyzszyBet:
        wartosc = int(input(f"Twoje opcje: 1. Raise  2. Call  3. Fold\nTwój wybór: "))
        if wartosc == 1:
            podbicie = int(input("Podaj o ile podbijasz: "))
            podbijZaklad(id_gracza, podbicie)
        elif wartosc == 2:
            wyrownajZaklad(id_gracza)
        elif wartosc == 3:
            fold(id_gracza)
    else:
        wartosc = int(input(f"Twoje opcje: 1. Raise  2. Check  3. Fold\nTwój wybór: "))
        if wartosc == 1:
            podbicie = int(input("Podaj o ile podbijasz: "))
            podbijZaklad(id_gracza, podbicie)
        elif wartosc == 2:
            check(id_gracza)
        elif wartosc == 3:
            fold(id_gracza)

def sprawdzStanRundy():
    global check_counter, karty_na_stole, bets, najwyzszyBet, temp_bets
    if check_counter >= len(gracze) - len(passy):
        print("\nWszyscy sprawdzili - koniec rundy.")
        check_counter = 0
        najwyzszyBet = 0
        karty_na_stole += 1
        bets = [0] * len(gracze)
        temp_bets = [0] * len(gracze)
    if karty_na_stole >= 5:
        return False
    return True

def wybierz_zwyciezce():
    global pula, passy
    print("Kto wygrał?")
    for i, gracz in enumerate(gracze):
        print(f"{i + 1}. {gracz}")
    winner = int(input("Wybierz zwycięzcę: ")) - 1
    pieniadze[winner] += pula
    pula = 0
    print(f"Gratulacje dla {gracze[winner]}! Wygrywasz {pula}.\n")
    passy.clear()

def gra():
    global passy, karty_na_stole
    dodaj_graczy()
    wprowadz_blindy()
    while len(gracze) > 1:
        ustaw_blindy()
        id_gracza = 0
        while True:
            if len(passy) >= len(gracze) - 1:
                break
            while id_gracza in passy:
                id_gracza += 1
                if id_gracza >= len(gracze):
                    id_gracza = 0
            akcje_gracza(id_gracza)
            if not sprawdzStanRundy():
                karty_na_stole = 3
                break
            id_gracza += 1
            if id_gracza >= len(gracze):
                id_gracza = 0
        wybierz_zwyciezce()
        przesunIndexGraczy()

if __name__ == "__main__":
    gra()
