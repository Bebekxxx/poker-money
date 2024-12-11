#Witamy W Poker Money App!
#Version 0.7

#Aplikacja sluży do liczenia pieniedzy w grze w poker
#App is used to count money in poker game

#Authors: Mikołaj Dziuba, Sebastian Golwiej (Students @ Lublin University of Technology)
#We are really grateful for sugestions and contributions from our friends: Bolo, Bartek, Hubert, Michu
#Date: 2024-08-12

#I implemented failsave in player actions, so players can't input anything outside of the given options
#I also implemented failsave in player's raise action, so players can't raise with negative value
#AND THE APP ACTUALLY WORKS NOW !!!
#Cheers! MD

import time
from enum import Enum

class wyborGracza(Enum):# Class for player's choices(it was for educational purposes XD)
    RAISE = 1
    CHECK = 2
    FOLD = 3

gracze = [] # Players list
pieniadze = [] # Players' money list
bets = [] # Players' bets list(used in each phase, reseted after each phase in SprawdzStanRundy function)
temp_bets = [] # Temporary bets list(used for current round, so players can check their bets in whole round, not only in current phase)
foldy = [] # List of players who have folded
pula = 0 # Main pot, it's being reset after each round
small_blind = 0
big_blind = 0
cards_on_the_table = 3 # Number of cards on the table(its starts form Flop phase)
check_counter = 0 # Counter for players who have checked in current phase
highets_bet = 0 # Highest bet in current phase(so players can raise or call, based on that information)

def wprowadz_blindy(): #Set values of blind (only used once at the beginning of the game)
    global small_blind, big_blind
    while True:
        try:
            small_blind = int(input("\nPodaj wartość małego blinda: "))
            big_blind = int(input("Podaj wartość dużego blinda: "))
            print("\n")
            break
        except ValueError:
            print("Wprowadź wartość liczbową!")
    print("\n")

def dodaj_graczy(): # Adds players and sets their money
    global gracze, pieniadze, bets
    liczbaGraczy = int(input("Podaj liczbę graczy: "))
    for index in range(liczbaGraczy):
        gracz = input(f"Podaj nazwę gracza {index + 1}: ")
        gracze.append(gracz)
        pieniadze.append(int(input(f"Ile pieniędzy ma {gracz}? ")))
        bets.append(0)
        temp_bets.append(0)
    print(f"Gracze: {gracze}")
    print(f"Pieniądze graczy: {pieniadze}")

def ustaw_blindy(): # Sets blinds (used at the beggining of each round), it always with [0] and [1] indexes because of przesunIndexGraczy function moving indexes
    global pula
    if len(gracze) > 1:
        pieniadze[0] -= small_blind
        pula += small_blind
        pieniadze[1] -= big_blind
        pula += big_blind
        print(f"Gracz {gracze[0]} postawił małego blinda, a gracz {gracze[1]} postawił dużego blinda\n")

def przesunIndexGraczy(): # Moves players' indexes(used at the end of each round)
    gracze.append(gracze.pop(0))
    pieniadze.append(pieniadze.pop(0))
    bets.append(bets.pop(0))
    print("Gracze: ", gracze)
    print("Pieniądze: ", pieniadze)
    print("Bety: ", bets)

def wyrownajZaklad(id_gracza):
    global highets_bet, pula
    betDanegoGracza = bets[id_gracza] # Zmienna pomocnicza, aby nie zmieniać wartości bets[id_gracza]
    print("Bet danego gracza: ", betDanegoGracza)
    if highets_bet < pieniadze[id_gracza]:
        pieniadze[id_gracza] -= (highets_bet - betDanegoGracza)
        bets[id_gracza] += (highets_bet - betDanegoGracza)
        temp_bets[id_gracza] += (highets_bet - betDanegoGracza)
        pula += (highets_bet - betDanegoGracza)
        print(f"Wyrównano zakład! (suma twoich zakładów na stole to {bets[id_gracza]})")
        print("Twoje pieniądze: ", pieniadze[id_gracza])
    else:
        print(f"Wchodzisz all in za {pieniadze[id_gracza]}\n")
        bets[id_gracza] += pieniadze[id_gracza]
        temp_bets[id_gracza] += pieniadze[id_gracza]
        pula += pieniadze[id_gracza]
        pieniadze[id_gracza] = 0

def podbijZaklad(id_gracza, podbicie):
    global highets_bet, pula, check_counter
    # tempHighetsBet = highets_bet
    highets_bet += (podbicie - bets[id_gracza])
    if highets_bet == pieniadze[id_gracza]:
        print(f"\nWchodzisz all in za {pieniadze[id_gracza]}")
    if highets_bet <= pieniadze[id_gracza]:
        pieniadze[id_gracza] -= highets_bet
        bets[id_gracza] += highets_bet
        temp_bets[id_gracza] += highets_bet
        pula += highets_bet
        print(f"Podbito o {highets_bet} [suma twoich zakładów na stole(w tej fazie) to {bets[id_gracza]}]")
        print("Twoje pieniądze: ", pieniadze[id_gracza])
        check_counter = 0

def check(id_gracza):
    global check_counter
    print(f"Gracz {gracze[id_gracza]} sprawdza (check)")
    check_counter += 1

def fold(id_gracza):
    foldy.append(id_gracza)
    print(f"Gracz {gracze[id_gracza]} passuje\n")

def akcje_gracza(id_gracza):
    global highets_bet, pula
    print(f"\nAktualny gracz to '{gracze[id_gracza]}'")
    print(f"Aktualna pula na stole wynosi: {pula}")
    if highets_bet == 0 or bets[id_gracza] == highets_bet:
        print(f"Twoje opcje to:\n"
              f"1. Podnieś zakład (raise), 2. Sprawdź (check), 3. Pass (fold)\n"
              f"Twój zakład na stole(w tej rundzie) to: {temp_bets[id_gracza]}\n"
              f"Aktualny najwyższy zakład(w tej fazie) to: {highets_bet}\n"
              f"Twój zakład na stole(w tej fazie) to: {bets[id_gracza]}\n")
        while True:
            try:
                wartosc = int(input(f"{gracze[id_gracza]} ({pieniadze[id_gracza]}): ").strip())
                if wartosc not in [action.value for action in wyborGracza]:
                    raise ValueError
                break
            except ValueError:
                print("Podano nieprawidłową opcję!")

        if wartosc == wyborGracza.RAISE.value:
            while True:
                try:
                    podbicie = int(input("Podaj o ile podbijasz: "))
                    if podbicie <= 0:
                        print("Bruh nie mozesz podbic o ujemna wartosc")
                        continue
                    if podbicie > pieniadze[id_gracza]:
                        print(f"Masz za mało pieniędzy na podbicie! Twoje pieniądze: {pieniadze[id_gracza]}")
                        continue
                    break
                except ValueError:
                    print("Podano nieprawidłową wartość!")
            podbijZaklad(id_gracza, podbicie)
        elif wartosc == wyborGracza.CHECK.value:
            check(id_gracza)
        elif wartosc == wyborGracza.FOLD.value:
            fold(id_gracza)
    elif bets[id_gracza] < highets_bet:
        print(f"Twoje opcje to:\n"
              f"1. Podnieś zakład (raise), 2. Wyrownaj zakład (call), 3. Pass (fold)\n"
              f"Twój zakład na stole(w tej rundzie) to: {temp_bets[id_gracza]}\n"
              f"Aktualny najwyższy zakład(w tej fazie) to: {highets_bet}\n"
              f"Twój zakład na stole(w tej fazie) to: {bets[id_gracza]}\n")
        while True:
            try:
                wartosc = int(input(f"{gracze[id_gracza]} ({pieniadze[id_gracza]}): ").strip())
                if wartosc not in [action.value for action in wyborGracza]:
                    raise ValueError
                break
            except ValueError:
                print("Podano nieprawidłową opcję!")

        if wartosc == wyborGracza.RAISE.value:
            while True:
                try:
                    podbicie = int(input("Podaj o ile podbijasz: "))
                    if podbicie <= 0:
                        print("Bruh nie mozesz podbic o ujemna wartosc")
                        continue
                    break
                except ValueError:
                    print("Podano nieprawidłową wartość!")
            while (podbicie + highets_bet) > pieniadze[id_gracza]:
                print(f"Masz za mało pieniędzy na podbicie! Twoje pieniądze: {pieniadze[id_gracza]}")
                podbicie = int(input("Podaj o ile podbijasz: "))
            podbijZaklad(id_gracza, podbicie)
        elif wartosc == wyborGracza.CHECK.value:
            if pieniadze[id_gracza] < highets_bet:
                print(f"Masz tylko {pieniadze[id_gracza]} żetonów. Czy chcesz wejść all in?\n")
                czyWchodziszAllIn = int(input("1. Tak 2. Nie(jesli nie wchodzisz all in to pasujesz): "))
                if czyWchodziszAllIn == 1:
                    wyrownajZaklad(id_gracza)
                else:
                    fold(id_gracza)
            else:
                wyrownajZaklad(id_gracza)
                check(id_gracza)
        elif wartosc == wyborGracza.FOLD.value:
            fold(id_gracza)
    else: #Left here for debugging purposes, if something goes wrong write to us(include all the details, how the game went, what you did before; screenshots are welcome)
        print("Coś poszło nie tak")
        print(f"Twoje zakłady: {bets[id_gracza]}")
        print("bets", bets)
        print("najwyzszy bet", highets_bet)
        print("pieniadze", pieniadze)
        print("\n")
        time.sleep(1000)

def sprawdzAllIn(id_gracza):
    if pieniadze[id_gracza] == 0:
        return True
    return False

def sprawdzStanRundy():
    global pula, cards_on_the_table, check_counter, highets_bet
    if check_counter == len(gracze) - len(foldy):
        cards_on_the_table += 1
        if cards_on_the_table > 5:
            print("Koniec rundy, czas na pokazanie waszych kart!")
            cards_on_the_table = 3
            for i in range(len(bets)):
                bets[i] = 0
            return False
        print("\n=======UWAGA========")
        print("Wykładaj kolejna karte na stół")
        print(f"Liczba kart na stole powinna wynosić {cards_on_the_table}")
        check_counter = 0
        highets_bet = 0
        for i in range(len(bets)):
            bets[i] = 0
    return True

def sprawdzBankrut():
    for i in range(len(pieniadze)):
        if pieniadze[i] == 0:
            print(f"Gracz {gracze[i]} zbankrutował i odpada z gry!")
            gracze.pop(i)
            pieniadze.pop(i)
            bets.pop(i)
            break

def wybierz_zwyciezce():
    global pula
    print("Kto wygrał?")
    for i, gracz in enumerate(gracze):
        if i not in foldy:
            print(f"{i+1}. {gracz}")
    while True:
        try:
            winner = int(input("\nZwycięzca: ")) - 1
            break
        except ValueError:
            print("Podaj prawidłową wartość!")

    # Check if winner went all-in, then calculate the winnings so winner is capped at his all-in bet
    if pieniadze[winner] == 0:  # Player went all-in
        all_in_bet = temp_bets[winner]
        total_won = 0
        for i in range(len(gracze)):
            if i != winner:
                bet_to_win = min(all_in_bet, temp_bets[i])
                pieniadze[i] += (temp_bets[i] - bet_to_win)
                total_won += bet_to_win
        pieniadze[winner] += total_won
    else:
        pieniadze[winner] += pula

    pula = 0
    foldy.clear()

    for i in range(len(temp_bets)):
        temp_bets[i] = 0

def gra(): # Main Game Function
    global check_counter
    dodaj_graczy() # Add players
    wprowadz_blindy() # Input blinds
    while True: # Round Loop
        id_gracza = 0 # Start with first player
        ustaw_blindy() # Set blinds
        while True:  # Phase Loop
            if id_gracza >= len(gracze):  # Check if all players have made their moves
                id_gracza = 0  # Start from the first player
            if id_gracza not in foldy:  # Skip player if he has folded
                if sprawdzAllIn(id_gracza):  # Check if player went all-in
                    print(f"\nGracz {gracze[id_gracza]} wszedł all in za {temp_bets[id_gracza]}")
                    print("Immediate check")
                    check(id_gracza)
                else:
                    akcje_gracza(id_gracza)  # Player's turn
            id_gracza += 1  # Next player
            if not sprawdzStanRundy():  # Check if round is over
                break

        wybierz_zwyciezce() # Choose the winner
        przesunIndexGraczy()  # Move players' indexes
        sprawdzBankrut() # Check if any player has gone bankrupt

        if len(gracze) == 1: # Check if there is only one player left and declare him the winner
            print(f"\n\nGratulacje {gracze[0]}! WYGRAŁEŚ {pieniadze[0]}!!!")
            break

if __name__ == "__main__":
    gra()