"""
Zadanie 7: funkcje

Stwórz program wykonujący następujące zadanie:

1. Poproś użytkownika o podanie rozmiaru listy liczb całkowitych (nazwijmy tą zmienną SIZE)
2. Poproś użytkownika o podanie SIZE elementów, które wypełnią tą listę (niech to będą liczby całkowite)
2.1 Uwaga: jeśli podana wartość nie jest liczbą całkowitą poproś użytkownika o podanie kolejnej wartości
3. Po wypełnieniu listy poproś użytkownika o wybranie jednej z dwóch opcji: 1 - wyszukanie liczb parzystych, 2 - wyszukanie liczb podzielnych przez 5
3.1 Uwaga: jeśli użytkownik podał inną liczbę niż z dostępnych opcji, poproś go o podanie poprawnej
4. Wyświetl listę i wynik działania:
a) jeśli wybrał 1: wyświetl wszystkie liczby parzyste z listy (bez powtórzeń)
b) jeśli wybrał 2: wyświetl wszystkie liczby podzielne przez 5 z listy (z powtórzeniami)

Przykład:
Podaj rozmiar listy: 5  (size = 5)
Podaj liczbę całkowitą: 5
Podaj liczbę całkowitą: 2
Podaj liczbę całkowitą: 3.5
Podana liczba nie jest liczbą całkowitą, podaj inną: 5
Podaj liczbę całkowitą: 4
Podaj liczbę całkowitą: 2
Wybierz jedną z dostępnych opcji
1: wyszukanie liczb parzystych
2: wyszukanie liczb podzielnych przez 5
opcja: 0                                               |   opcja: 1
wybrałeś nieprawidłową opcję, wybierz ponownie: 1      |   wybrałeś opcję: wyszukanie liczb podzielnych przez 5
wybrałeś opcję: wyszukanie liczb parzystych            |   lista: [5, 2, 5, 4, 2]
lista: [5, 2, 5, 4, 2]                                 |   wynik: [5, 5]
wynik: [2, 4]                                          |

"""