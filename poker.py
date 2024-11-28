gracze = []
pieniadze = []
zaklady = []
pula = 0

#Dodawanie graczy
while True:
    imie = input("Podaj nazwę gracza (X aby zakończyć dodawanie graczy): ")
    if imie == "X":
        break
    gracze.append(imie)

kasa_na_start = int(input("Podaj kwotę z jaką każdy zaczyna grę: "))
ilu_graczy = 0
for x in gracze:
    pieniadze.append(kasa_na_start)
    zaklady.append(0)
    ilu_graczy += 1

#pętla gry
while True:
    passy = []
    id_gracza = 0
    while True:
        if len(passy) == len(gracze) - 1:
            break
        if id_gracza == ilu_graczy:
            id_gracza = 0
        if id_gracza in passy:
            id_gracza += 1
            continue
        wartosc = int(input("Opcje:\n1. Podnieś zakład\n2. Check\n3. Pass\n69. Koniec rundy\n\nAktualna pula: {}\n{} ({}): ".format(pula, gracze[id_gracza], pieniadze[id_gracza])))
        if wartosc == 1:
            podbicie = int(input("Podaj o ile podbijasz: "))
            if podbicie <= pieniadze[id_gracza]:
                pieniadze[id_gracza] -= podbicie
                zaklady[id_gracza] += podbicie
                pula += podbicie
                print("Podbito o {} (łącznie {})\n".format(podbicie, zaklady[id_gracza]))
                i = 0
                while i < ilu_graczy:
                    if i == id_gracza or i in passy:
                        i += 1
                        continue
                    else:
                        decyzja = int(input("{}({})- 1.Podbijam 2.Pass: ".format(gracze[i], pieniadze[i])))
                        if decyzja == 1:
                            if podbicie <= pieniadze[i]:
                                pieniadze[i] -= podbicie
                                zaklady[i] += podbicie
                                pula += podbicie
                                print("Podbito!\n")
                            else:
                                print("Za mało kasy: wchodzisz all in z {}\n".format(pieniadze[i]))
                                zaklady[i] += pieniadze[i]
                                pula += pieniadze[i]
                                pieniadze[i] = 0
                            i += 1
                        elif decyzja == 2:
                            passy.append(i)
                            print("Gracz {} passuje! (cipka)\n".format(gracze[i]))
                            i += 1
                        else:
                            print("Podano złą opcję!\n")
                id_gracza += 1
            else:
                print("Masz zbyt mało środków!")
        elif wartosc == 2:
            print("Gracz {} check\n".format(gracze[id_gracza]))
            id_gracza += 1
        elif wartosc == 3:
            passy.append(id_gracza)
            print("Gracz {} passuje\n".format(gracze[id_gracza]))
            id_gracza += 1
        elif wartosc == 69:
            break
        else:
            print("Podano nieprawidłową opcję!")
    print("Kto wygrał?")
    i = 0
    for zjeb in gracze:
        print("{}. {}".format(i+1, zjeb))
        i += 1
    winner = int(input("\nZwycięzca: "))-1
    pieniadze[winner] += pula
    pula = 0
    for sumka in zaklady:
        sumka = 0
    for bankrut in pieniadze:
        if bankrut == 0:
            y = pieniadze.index(bankrut)
            print("Gracz {} zbankrutował i odpada z gry!".format(gracze[y]))
            gracze.pop(y)
            pieniadze.pop(y)
            zaklady.pop(y)
            ilu_graczy -= 1
    if len(gracze) == 1:
        print("\n\nGratulacje {}! WYGRAŁEŚ {}!!!".format(gracze[0], pieniadze[0]))
        break

