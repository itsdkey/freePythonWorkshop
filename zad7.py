"""
Zadanie 7: funkcje

Stwórz program wykonujący następujące zadanie:

1. Poproś użytkownika o podanie rozmiaru listy liczb całkowitych (nazwijmy tą zmienną SIZE)
2. Poproś użytkownika o podanie SIZE elementów, które wypełnią tą listę (niech to będą liczby całkowite)
2.1 Uwaga: jeśli podana wartość nie jest liczbą całkowitą poproś użytkownika o podanie kolejnej wartości
3. Po wypełnieniu listy poproś użytkownika o wybranie jednej z dwóch opcji: 1 - wyszukanie liczb parzystych, 2 - wyszukanie liczb nieparzystych
3.1 Uwaga: jeśli użytkownik podał inną liczbę niż z dostępnych opcji, poproś go o podanie poprawnej
4. Wyświetl listę i wynik działania:
a) jeśli wybrał 1: wyświetl wszystkie liczby parzyste z listy (bez powtórzeń)
b) jeśli wybrał 2: wyświetl wszystkie liczby nieparzystych z listy (z powtórzeniami)

Przykład:
Podaj rozmiar listy: 5  (size = 5)
Podaj liczbę całkowitą: 5
Podaj liczbę całkowitą: 2
Podaj liczbę całkowitą: 3.5
Podana liczba nie jest liczbą całkowitą, podaj inną
Podaj liczbę całkowitą: 5
Podaj liczbę całkowitą: 4
Podaj liczbę całkowitą: 2
Wybierz jedną z dostępnych opcji
1: wyszukanie liczb parzystych
2: wyszukanie liczb nieparzystych
opcja: 0                                               |   opcja: 1
Wybrałeś nieprawidłową opcję, wybierz ponownie         |   wybrałeś opcję: wyszukanie liczb nieparzystych
opcja: 1                                               |   lista: [5, 2, 5, 4, 2]
Wybrałeś opcję: wyszukanie liczb parzystych            |   wynik: [5, 5]
lista: [5, 2, 5, 4, 2]                                 |
wynik: [2, 4]                                          |
"""
