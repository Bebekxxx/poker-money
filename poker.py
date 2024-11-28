#Kompletny remake kodu zrobiony na funkcjach i zmiennych globalnych
#Zmieniłem nazwy zmiennych na bardziej czytelne
#Dodałem funkcje, które odpowiadają za różne etapy gry
#Dodałem funkcję main gry, która odpowiada za całą rozgrywkę
#Dodałem funkcję sprawdz_stan_gry, która sprawdza czy gra się skończyła
#Dodałem funkcję akcje_gracza, która odpowiada za akcje gracza
#Dodałem funkcję ustaw_blindy, która ustawia blinde
#Dodałem funkcję dodaj_graczy_i_ustaw_kwoty_startowe, która dodaje graczy i ustawia kwoty startowe
#Dodałem funkcję wprowadz_blindy, która wprowadza wartości blindów
#Dodałem zmienną globalną karty_na_stole, która odpowiada za ilość kart na stole
#Dodałem zmienną globalną big_blind, która odpowiada za wartość dużego blinda
#Dodałem zmienną globalną small_blind, która odpowiada za wartość małego blinda
#Dodałem zmienną globalną pula, która odpowiada za wartość puli
#Dodałem zmienną globalną zaklady, która odpowiada za wartość zakładów
#Dodałem zmienną globalną pieniadze, która odpowiada za wartość pieniędzy graczy
#Dodałem zmienną globalną gracze, która odpowiada za wartość graczy
#Dodałem zmienną globalną ilu_graczy, która odpowiada za ilość graczy
#Dodałem zmienną globalną karty, która odpowiada za wartość kart
#Dodałem zmienną globalną karty_na_stole, która odpowiada za wartość kart na stole


gracze = []
pieniadze = []
zaklady = []
pula = 0
small_blind = 0
big_blind = 0
karty_na_stole = 0
check_counter = 0

def wprowadz_blindy():
    global small_blind, big_blind
    small_blind = int(input("Podaj wartość małego blinda: "))
    big_blind = int(input("Podaj wartość dużego blinda: "))

def dodaj_graczy():
    global gracze, pieniadze, zaklady
    while True:
        imie = input("Podaj nazwę gracza (X aby zakończyć dodawanie graczy): ")
        if imie.lower() == "x":
            break
        gracze.append(imie)
    kasa_na_start = int(input("Podaj kwotę z jaką każdy zaczyna grę: "))
    for _ in gracze:
        pieniadze.append(kasa_na_start)
        zaklady.append(0)

def ustaw_blindy():
    global pula
    if len(gracze) > 1:
        pieniadze[0] -= small_blind
        zaklady[0] += small_blind
        pula += small_blind
        pieniadze[1] -= big_blind
        zaklady[1] += big_blind
        pula += big_blind
        print(f"Gracz {gracze[0]} postawił małego blinda, a gracz {gracze[1]} postawił dużego blinda\n")

def akcje_gracza(id_gracza, passy):
    global pula, check_counter
    print(f"Aktualny gracz to {gracze[id_gracza]} ({pieniadze[id_gracza]})")
    print(f"Aktualna pula: {pula}\n")
    wartosc = int(input(f"Opcje:\n1. Podnieś zakład\n2. Check\n3. Pass\n69. Koniec rundy\n{gracze[id_gracza]} ({pieniadze[id_gracza]}): "))
    if wartosc == 1:
        podbicie = int(input("Podaj o ile podbijasz: "))
        if podbicie <= pieniadze[id_gracza]:
            pieniadze[id_gracza] -= podbicie
            zaklady[id_gracza] += podbicie
            pula += podbicie
            print(f"Podbito o {podbicie} (suma twoich zakładów na stole to {zaklady[id_gracza]})\n")
            check_counter = 0
            for i in range(len(gracze)):
                if i == id_gracza or i in passy:
                    continue
                decyzja = int(input(f"{gracze[i]}({pieniadze[i]})- 1.Wyrównaj 2.Pass: "))
                if decyzja == 1:
                    if podbicie <= pieniadze[i]:
                        pieniadze[i] -= podbicie
                        zaklady[i] += podbicie
                        pula += podbicie
                        print("Wyrównano zakład!\n")
                    else:
                        print(f"Za mało kasy: wchodzisz all in z {pieniadze[i]}\n")
                        zaklady[i] += pieniadze[i]
                        pula += pieniadze[i]
                        pieniadze[i] = 0
                elif decyzja == 2:
                    passy.append(i)
                    print(f"Gracz {gracze[i]} passuje! (cipka)\n")
                else:
                    print("Podano złą opcję!\n")
        else:
            print("Masz zbyt mało środków!")
    elif wartosc == 2:
        print(f"Gracz {gracze[id_gracza]} check\n")
        check_counter += 1
    elif wartosc == 3:
        passy.append(id_gracza)
        print(f"Gracz {gracze[id_gracza]} passuje\n")
        check_counter = 0
    elif wartosc == 69:
        return False
    else:
        print("Podano nieprawidłową opcję!")
    return True

def sprawdz_stan_gry():
    global pula, karty_na_stole, check_counter
    if check_counter == len(gracze):
        print("Wykładaj kolejna karte na stół")
        karty_na_stole += 1
        check_counter = 0
    if karty_na_stole >= 5:
        print("5 kart na stole, czas na pokazanie rąk!")
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
    for i in range(len(zaklady)):
        zaklady[i] = 0
    for i in range(len(pieniadze)):
        if pieniadze[i] == 0:
            print(f"Gracz {gracze[i]} zbankrutował i odpada z gry!")
            gracze.pop(i)
            pieniadze.pop(i)
            zaklady.pop(i)
            break
    if len(gracze) == 1:
        print(f"\n\nGratulacje {gracze[0]}! WYGRAŁEŚ {pieniadze[0]}!!!")
        return False
    return True

def gra():
    dodaj_graczy()
    wprowadz_blindy()
    while True:
        passy = []
        id_gracza = 0
        ustaw_blindy()
        while True:
            if len(passy) == len(gracze) - 1:
                break
            if id_gracza == len(gracze):
                id_gracza = 0
            if id_gracza in passy:
                id_gracza += 1
                continue
            if not akcje_gracza(id_gracza, passy):
                break
            id_gracza += 1
        if not sprawdz_stan_gry():
            break
    if not wybierz_zwyciezce():
        return

if __name__ == "__main__":
    gra()

#Chuje muje dzikie węże siur123