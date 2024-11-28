# Poker Money

## Opis projektu

**Poker Money** to minimalistyczny program do zarządzania wirtualnymi funduszami w pokerze, napisana w Pythonie w ramach spontanicznego pomysłu podczas wieczoru z przyjaciółmi. Projekt pozwala śledzić saldo graczy, prowadzić zakłady oraz zarządzać rundami gry bez potrzeby fizycznych żetonów.

## Funkcjonalności

- Dodawanie dowolnej liczby graczy.
- Automatyczne zarządzanie pulą zakładów.
- Obsługa podstawowych akcji pokerowych: **podbijanie**, **sprawdzanie** i **pasowanie**.
- Obsługa sytuacji "all-in", gdy gracz nie ma wystarczającej ilości środków na podbicie.
- Eliminowanie graczy, którzy zbankrutowali.
- Zakończenie gry, gdy pozostanie jeden zwycięzca.

## Uruchamianie

1. **Uruchom grę** w terminalu:

    ```bash
    python poker.py
    ```

2. Postępuj zgodnie z instrukcjami w grze:
    - Dodaj graczy.
    - Ustal początkową kwotę dla każdego z nich.
    - Rozpocznij rundę i wykonuj kolejne akcje: podbijaj, sprawdzaj lub pasuj.

## Przykładowy przebieg gry

1. **Dodawanie graczy**:  
   Podaj nazwy graczy (wpisz `X`, aby zakończyć dodawanie).

2. **Podaj kwotę startową**:  
   Wszyscy gracze rozpoczynają grę z tą samą sumą pieniędzy.

3. **W trakcie gry**:  
   - Każdy gracz wykonuje swoją turę, podnosząc zakład, sprawdzając lub pasując.
   - Gracze bez środków przechodzą automatycznie w tryb "all-in".
   - Gra kończy się eliminacją kolejnych graczy, aż do wyłonienia zwycięzcy.

## Przykładowe akcje w grze

- **Opcje w turze gracza**:
    ```text
    Opcje:
    1. Podnieś zakład
    2. Check
    3. Pass
    69. Koniec rundy

    Aktualna pula: 100
    Janek (200): 
    ```

- **Podbijanie i decyzje innych graczy**:
    ```text
    Podaj o ile podbijasz: 50
    Janek podbił zakład o 50 (łącznie 50)

    Marek (150) - 1. Podbijam  2. Pass:
    ```

- **Eliminacja graczy**:
    ```text
    Gracz Marek zbankrutował i odpada z gry!
    ```

- **Ogłoszenie zwycięzcy**:
    ```text
    Gratulacje Janek! WYGRAŁEŚ 500!!!
    ```

## Wymagania

- Python 3.x
- Brak dodatkowych bibliotek (działa w czystym Pythonie).

## Plany na przyszłość

- **Dodanie GUI**: interfejs graficzny, aby gra była bardziej intuicyjna.
- Możliwość **zapisu stanu gry** i kontynuowania jej później.
- **Rozbudowanie logiki gry**

## Jak możesz pomóc?

Jeśli masz pomysły na ulepszenia lub chcesz wnieść swój wkład, zapraszam do zgłaszania sugestii i otwierania pull requestów. Każdy wkład jest mile widziany!

---

Dzięki za zainteresowanie projektem! 🃏💸
