"""
Zadanie 6: operacje na słownikach


1. Stwórz słownik i go wyświetl


2. Stwórz słownik z trzech par (klucz wartość) podanych przez użytkonika i wyświetl wynik
Uwaga: jeśli użytkownik poda ten sam klucz wyświetl najnowszą wartość dla tego klucza

Przykłady:
pierwszy 3
drugi test
trzeci 4.5
wynik: {'pierwszy': '3', 'drugi': 'test', 'trzeci': '4.5'}

pierwszy 3
drugi test
pierwszy 55
wynik {'pierwszy': '55', 'drugi': 'test'}


3. Stwórz słownik z trzech par (klucz wartość) podanych przez użytkonika i wyświetl wynik
Uwaga: jeśli użytkownik poda ten sam klucz dodaj kolejną wartość do listy pod tym kluczem

Przykład:
pierwszy 3
drugi test
pierwszy 55
wynik {'pierwszy': ['3', '55'], 'drugi': ['test']}


4. Stwórz dwa słowniki i je scal
Uwaga: jeśli klucze się pokrywają, zatrzymaj wartości z drugiego słownika

Przykład:
pierwszy = {'test': 1, 'klucz': 'wartosc'}
drugi = {33: 1, 'klucz': 40}
wynik: {'test': 1, 33: 1, 'klucz': 40}


5. Stworz zmienną datetime z dzisiejszą datą i wyświetl słownie dzień tygodnia

przykład:
from datetime import datetime
today = datetime.now()
today.weekday() -> 4
4 -> czwartek
"""