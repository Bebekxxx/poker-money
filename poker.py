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
