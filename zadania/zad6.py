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
'dict_view' - jest to tak zwany widok - przechowuje aktualny stan słownika
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
my_dictionary['temp'] = 2
print(my_dictionary)


"""
Scalanie (łączenie) słowników.
Można to zrobić na dwa sposoby:
    1.  W związku z tym, że słowniki póki co nie wspierają operacji 'a + b' to należy to robić w inny sposób.
        c = {**a, **b}
        Powyższa operacja tworzy nowy słownik (widzimy zadeklarowane '{ ... }'). Do nowego słownika trafiąją wpierw dane
        ze słownika 'a' poprzez ROZPAKOWANIE go za pomocą podwójnych gwiazdek '**'. Następnie do tego słownika trafiają dane
        ze słownika 'b' w ten sam sposób. W związku z tym, że w nowym słowniku już były dane ze słownika 'a' to nowsze dane mogą
        nadpisać te dane (w taki sam sposób jakbyśmy próbowali nadpisać wartość dla konkretnego klucza).
        Operacja rozłożona na czynniki pierwsze:
        a = {'temp': 1, 'test2': 22}
        b = {'temp': 2, 'other': 'value'}  <--- powtarza się klucz 'temp'
        c = {**a, **b}
           # pod maską:
           1. c = {'temp': 1, 'test2': 22}
           2. for key, value in b.items():
                  c[key] = value
              print(c)  <--- {'temp': 2, 'test2': 22, 'other': 'value}
    2. Poprzez wykorzystanie operacji '.update()', którą dostarcza słownik. UWAGA! z tym sposobem trzeba uważać by przez
       przypadek nie zaaktualizować poprzedniego słownika jeśli tego nie chcemy (zależy od sytuacji)
       przykład:
            a = {'temp': 1, 'test2': 22}
            b = {'temp': 2, 'other': 'value'}  <--- powtarza się klucz 'temp'
            c = a   <--- przypisujemy ten sam słownik pod inną zmienną
            c.update(b)  <--- aktualizujemy słownik 'c' danymi ze słownika 'b'
            print(c)  <--- {'temp': 2, 'test2': 22, 'other': 'value}
"""


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
a) za pomocą rozpakowywania słowników, czyli operacji **slownik
b) za pomocą operacji .update()
c) za pomocą zwykłej pętli for

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


"""
6. Zlicz słowa występnujące w podanym zdaniu i wyświetl je w kolejności:
6.1) ilość wystąpień rosnąco
6.2) ilość wystąpień malejąco

Te zadanie wykonaj na dwa sposoby:
a) za pomocą zwykłych pętli for
b) za pomocą klasy Counter.
    Link: https://docs.python.org/3/library/collections.html#collections.Counter
c*) za pomocą zwykłych pętli for i innego typu słownika - defaultdict.
    Link: https://docs.python.org/3/library/collections.html#collections.defaultdict 

Do sortowania wykorzystaj wbudowaną funkcję 'sorted' oraz funkcję 'lambda'.
Linki:
    sorted: https://docs.python.org/3/library/functions.html#sorted
    sortowanie, podstawy: https://docs.python.org/3/howto/sorting.html#sorting-basics 

Lambdę wykorzystamy do wyboru po czym mamy tak na prawdę sortować w funkcji sorted
sorted(
    <nasza kolekcja>,
    key=<funkcja która zwróci wartość po której sortować>,
    reverse=True/False  # czy sortwać malejąco czy rosnąco
)

pod argument key musimy przekazać funkcję. Możemy do tego celu stworzyć krótką jawną funkcję (z nazwą) bądź funkcję
anonimową, czyli funkcję lambda. Funkcje lambda mogą wykonać tylko jedno wyrażenie (ograniczenie narzucone z góry).

w naszym wypadku będzie to:
key=lambda x: x[1] 
"""