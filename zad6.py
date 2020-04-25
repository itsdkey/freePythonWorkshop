"""
        Temat 6: operacje na słownikach

Przykłady
1. Stworzenie słownika i jego wyświetlenie
"""
my_dictionary = {'temp': 1, 'klucz': 'wartość'}
print(my_dictionary)


"""
2. Iteracja po słowniku za pomocą 'view' zwracanego przez metodę .items()
'view' (pol. widok) jest to obiekt pythonowy który jest zwracany przez metody:
.items()
.keys()
.values()
Jest on odzwierciedleniem aktualnego stanu słownika to znaczy, że jeśli słownik zmieni się w trakcie programu
zmieni się także jego widok, np. usunięto bądź dodano nowy klucz do słownika, lub podmieniono wartość istniejącego
klucza.
"""
my_dictionary = {'temp': 1, 'klucz': 'wartość'}
for key, value in my_dictionary.items():
    print(key, value)


"""
3. Wyświetlenie tylko kluczy słownika:
a) za pomocą zwykłej pętli for
b) za pomocą 'dict_view' - .keys() 
'dict_view' - jest to tak zwany widok
"""
my_dictionary = {'temp': 1, 'klucz': 'wartość'}
for key in my_dictionary:
    print(key)

keys = my_dictionary.keys()
for key in keys:
    print(key)


"""
4. Wyświetlenie tylko wartości słownika:
Należy do tego wykorzystać 'dict_view' - .values()
Z uwagi na to, że .values() tak jak .keys() zwraca 'widok' to należy po nim przeiterować lub zmienić na listę
"""
my_dictionary = {'temp': 1, 'klucz': 'wartość'}
for value in my_dictionary.values():
    print(value)


"""
Podmiana wartości klucza w słowniku
"""
my_dictionary = {'temp': 1, 'klucz': 'wartość'}
my_dictionary['tem['] = 2
print(my_dictionary)


"""
        Zadania

1. Stwórz słownik i go wyświetl
"""


"""
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
"""


"""
3. Stwórz słownik z trzech par (klucz wartość) podanych przez użytkonika i wyświetl wynik
Uwaga: jeśli użytkownik poda ten sam klucz dodaj kolejną wartość do listy pod tym kluczem

Przykład:
pierwszy 3
drugi test
pierwszy 55
wynik {'pierwszy': ['3', '55'], 'drugi': ['test']}
"""


"""
4. Stwórz dwa słowniki i je scal
Uwaga: jeśli klucze się pokrywają, zatrzymaj wartości z drugiego słownika

Przykład:
pierwszy = {'test': 1, 'klucz': 'wartosc'}
drugi = {33: 1, 'klucz': 40}
wynik: {'test': 1, 33: 1, 'klucz': 40}
"""


"""
5. Stworz zmienną datetime z dzisiejszą datą i wyświetl słownie dzień tygodnia

przykład:
from datetime import datetime
today = datetime.now()
today.weekday() -> 4
4 -> czwartek
"""
