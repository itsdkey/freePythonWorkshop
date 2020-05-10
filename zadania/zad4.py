"""
Zadanie 4: instrukcje warunkowe

1. Poproś użytkownika o podanie liczby całkowitej i wyświetl następujący tekst
a) "to jest liczba parzysta" - gdy liczba jest podzielna przez 2
b) "to jest liczba nieparzysta" - gdy liczba nie jest podzielna przez 2


2. Poproś użytkownika o podanie dwóch liczb całkowitych (na potrzeby zadania nazwijmy je: A i B) i wyświetl:
a) "liczba A jest podzielna przez B" - gdy liczba A jest podzielna przez B (w miejsce A i B wstaw odpowiednie wartości)
b) "liczba B jest podzielna przez A" - gdy liczba B jest podzielna przez A (w miejsce A i B wstaw odpowiednie wartości)
b) "liczby nie są przez siebie podzielne" - gdy liczby nie są podzielne przez siebie


3. Stworz zmienną datetime z dzisiejszą datą i wyświetl słownie dzień tygodnia

przykład:
from datetime import datetime
today = datetime.now()
today.weekday() -> 3
3 -> czwartek


4. Poproś użytkownika o poadanie liczby całkowitej i wyświetl:
a) "liczba jest podzielna przez 3 i 5" - jeśli liczba jest podzielna przez 3 i 5
b) "liczba jest podzielna 2 lub 7" - jeśli liczba jest podzielna przez 2 lub 7


5. Poproś użytkownika o podanie trzech liczb całkowitych (na potrzeby zadania nazwijmy je: A, B, C) i wyświetl:
a) "liczba A jest podzielna przez B" - gdy liczba A jest podzielna przez B
b) "liczba A jest podzielna przez C" - gdy liczba A jest podzielna przez C
c) "liczba A jest podzielna przez B i C" - gdy liczba jest podzielna przez B i C
d) "liczba A nie jest podzielna ani przez B ani przez C" - gdy liczba nie jest podzielna ani przez B ani przez C

Przykłady:
A = 15
B = 3
C = 5
wynik: liczba 15 jest podzielna przez 3 i 5

A = 12
B = 6
C = 11
wynik: liczba 12 jest podzielna przez 6

A = 20
B = 3
C = 10
wynik: liczba 20 jest podzielna przez 10

A = 11
B = 2
C = 3
wynik: liczba 11 nie jest podzielna przez ani przez 2 ani przez 3


6. Poproś użytkownika o podanie ciągu znaków (przykładowe zdanie) i wyrazu, którego należy wyszukać a następnie:
a) wyświetl "zdanie zawiera '...' - gdy zdanie zawiera szukany wyraz (w miejsce ... wstaw wyraz)
b) wyświetl "zdnie nie zawiera '...' - gdy zdanie nie zawiera szukanego wyrazu (w miejsce ... wstaw wyraz)

Przykład:
zdanie: ala ma kota
szukane: ala
wynik: zdanie zawiera 'ala'

zdanie: ala ma kota
szukane: psa
wynik: zdanie nie zawiera 'psa'

"""
