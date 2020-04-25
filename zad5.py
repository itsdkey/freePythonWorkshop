"""
        Temat 5: operacje na listach

Przykłady iteracji po zbiorach (listach)
1. Przykład wyświetlenia zawartości listy
a) za pomocą pętli for
b) za pomocą pętli while
"""
print('### wyświetlenie zawartości list ###')
print('### petla for ###')
my_list = [10, 100, 1000, 10000]
for value in my_list:
    print(value)

print("### petla while ###")
my_list = [20, 200, 2000, 20000]
index = 0
list_length = len(my_list)  # funkcja len() - zwraca długość zbioru
while index < list_length:
    print(my_list[index])
    index += 1


"""
2. Sumowanie zawartości listy
"""
print('### sumowanie zwartości listy ###')
print('### petla for ###')
my_list = [1, 3, 5, 8, 16]
list_sum = 0
for value in my_list:
    list_sum += value

print(list_sum)

print('### petle while ###')
my_list = [2, 4, 8, 16, 32, 64]
list_sum = 0
index = 0
while index < len(my_list):
    list_sum += my_list[index]
    index += 1

print(list_sum)

"""
3. Operacja dodawania elementu do list - methoda append
"""
my_list = []
my_list.append(1)
print(my_list)


"""
4. Pętle nieskończone z warunkiem przerwania
W tym przykładzie jeśli w lisćie nie będzie elementu o wartości 5
to będą wyświetlane elementy listy w kółko za pomocą operacji 'modulo' -> %
'index % list_length' zapewni nam że nie wyjdziemy za zakres listy mimo, że index będzie inkrementowany (zwiększany o 1)
Aby to sprawdzić wystraczy usunąć '5' z listy i odpalić program
Do jego przerwania zastosuj skrót: CTRL + c
"""
my_list = [1, 2, 3, 5, 10, 11]
index = 0
list_length = len(my_list)
while True:
    value = my_list[index % list_length]
    print(value)
    if value == 5:
        break
    else:
        index += 1

"""
Innym przykładem może być sumowanie wartości podane przez użytkownika.
W tym przykładzie sumujemy liczby dopóki możemy. Jeśli użytkownik nie podał liczby to przerywamy sumowanie.
Wynik wyświetlamy.
"""
my_sum = 0
while True:
    value = input('podaj liczbe: ')
    try:
        value = int(value)
    except ValueError:
        # warunek try-except zapewnia nam, iż wartość podana przez użytkownika można zmienić na liczbę całkowitą.
        # ValueError - wyjątek wystąpi, gdy podana wartość nie może być zmieniona na liczbę całkowitą. W takiej sytuacji
        # przerywamy pętlę while za pomocą 'break'
        break
    else:
        my_sum += value
print(my_sum)


"""
        Zadania


1. Stwórz listę liczb całkowitych i wyświetl jej zawartość w postaci: [...]
"""



"""
2. Stwórz listę zawierającą 5 elementów i wyświetl jej zawartość w kolejnych wierszach w postaci (index: wartość)

przykład: [10, None, Decimal('2.5'), 'to jest super tekst', {'a': 33}]
wynik:
0: 10
1: None
2: Decimal('2.5')
3: 'to jest super tekst'
4: {'a': 33}
"""



"""
3. Stwórz dwie listy i dodaj je do siebie
"""



"""
4. Stwórz listę 10-cio elementową, wypełnij ją i:
a) wyświetl elementy o indeksach 2,3,6
b) wyświetl pierwsze 3 elementy
c) wyświetl elementy o indeksach 3,4,5,6,7
d) wyświetl 3 ostatnie elementy
e) wyświetl co drugi element
"""



"""
5. Wykonaj następujące działania:
a) Poproś użytkownika o podanie liczby, która będzie oznaczać pojemność listy (nazwijmy ją SIZE)
b) Następnie poproś użytkownika o podanie SIZE elementów i zapisz je do listy
c) Wyświetl otrzymaną listę w dowolny sposób
d) Wyświetl ostatnie 3 elementy

Przykład:
Size = 3
1
Temp
2.5
wynik: ['1', 'Temp', '2.5']
"""



"""
6. Stwórz dwie listy. Z pierwsze usuń elementy, które pojawiły się w drugiej i wyświetl wynik.

Przykład:
first = [1, 23, 4, 5, 6, 1, 25, 3, 3, 3]
second = [1, 4, 23]
wynik: [5, 6, 25, 3, 3, 3]
"""


"""
7. Stwórz maszynę losującą typu lotek. Wylosuj 10 liczb całkowitych i wyświetl zawartość:
a) mogą być powtórzenia
b) bez powtórzeń *
Uwaga: skorzystaj z modułu "random"
https://docs.python.org/3/library/random.html
import random
losowa_liczba = random.randint(1, 100)
"""



"""
8.* Poproś użytkownika o podanie 10ciu różnych liczb całkowitych i zapisz je do listy:
Uwaga: jeśli użytkownik poda liczbę, która jest już w liście, wyświetl: ta liczba jest już w liście

Przykład:
podaj liczbe: 10
podaj liczbe: 9
podaj liczbe: 10
ta liczba jest już w liście
podaj liczbe: 8
podaj liczbe 245
...
wynik: [10, 9, 8, 245, ... ] <- w liście ma być 10 elementów
"""



"""
9.* Poproś użytkownika o podanie 5ciu liczb i zapisz je do listy. następnie zsumuj te liczby

Przykład:
podaj liczbe: 1
podaj liczbe: 2
podaj liczbe: 3
podaj liczbe: 100
podaj liczbe: 22
wynik: 128
"""
