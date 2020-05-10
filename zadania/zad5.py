# """
#         Temat 5: operacje na listach

# Przykłady iteracji po zbiorach (listach)
# 1. Przykład wyświetlenia zawartości listy
# a) za pomocą pętli for
# b) za pomocą pętli while
# """
# print('### wyświetlenie zawartości list ###')
# print('### petla for ###')
# my_list = [10, 100, 1000, 10000]
# for value in my_list:
#     print(value)
# print("### petla while ###")
# my_list = [20, 200, 2000, 20000]
# index = 0
# list_length = len(my_list)  # funkcja len() - zwraca długość zbioru
# while index < list_length:
#     print(my_list[index])
#     index += 1   # index = index + 1


# """
# 2. Sumowanie zawartości listy
# """
# print('### sumowanie zwartości listy ###')
# print('### petla for ###')
# my_list = [1, 3, 5, 8, 16]
# list_sum = 0
# for value in my_list:
#     list_sum += value  # list_sum = list_sum + value
#     print(f'aktualna suma={list_sum}')

# print(list_sum)

# print('### petle while ###')
# my_list = [2, 4, 8, 16, 32, 64]
# list_sum = 0
# index = 0
# while index < len(my_list):
#     list_sum += my_list[index]
#     index += 1

# print(list_sum)

# """
# 3. Operacja dodawania elementu do list - methoda append
# """
# my_list = []
# my_list.append(1)
# print(my_list)
# my_list.append(2)
# print(my_list)

# my_list = [10, 20, 30, 40]
# copy_my_list = []
# for value in my_list[2:4]:
#   copy_my_list.append(value)
# print(copy_my_list)


# """
# 4. Pętle nieskończone z warunkiem przerwania
# W tym przykładzie jeśli w lisćie nie będzie elementu o wartości 5
# to będą wyświetlane elementy listy w kółko za pomocą operacji 'modulo' -> %
# 'index % list_length' zapewni nam że nie wyjdziemy za zakres listy mimo, że index będzie inkrementowany (zwiększany o 1)
# Aby to sprawdzić wystraczy usunąć '5' z listy i odpalić program
# Do jego przerwania zastosuj skrót: CTRL + c
# """
# my_list = [1, 2, 3, 10, 5, 11]
# index = 0
# list_length = len(my_list)
# while True:
#     value = my_list[index % list_length]
#     print(value)
#     if value == 5:
#         break
#     else:
#         index += 1

# """
# Innym przykładem może być sumowanie wartości podane przez użytkownika.
# W tym przykładzie sumujemy liczby dopóki możemy. Jeśli użytkownik nie podał liczby to przerywamy sumowanie.
# Wynik wyświetlamy.
# """
# my_sum = 0
# while True:
#     value = input('podaj liczbe: ')
#     try:
#         value = int(value)
#     except ValueError:
#         # warunek try-except zapewnia nam, iż wartość podana przez użytkownika można zmienić na liczbę całkowitą.
#         # ValueError - wyjątek wystąpi, gdy podana wartość nie może być zmieniona na liczbę całkowitą. W takiej sytuacji
#         # przerywamy pętlę while za pomocą 'break'
#         break
#     else:
#         my_sum += value
# print(my_sum)


"""
        Zadania


1. Stwórz listę liczb całkowitych i wyświetl jej zawartość w postaci: [...]
"""
Agnes_list = [ 2, 5, 130, 1403]
print(Agnes_list)
my_list = [12, 1, 13, 5]
print(my_list)


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
itsdkey_list = ['wow', 45, None, 2, 'ala']
index = 0
for value in itsdkey_list:
  print(f'{index}: {value}')
  index += 1

print('#######')
itsdkey_list = ['wow', 45, None, 2, 'ala', 6, 7]
        # indexy: 0     1   2    3    4    5  6
index = 0
while index <= len(itsdkey_list) -1:
  print(f'{index}: {itsdkey_list[index]}')
  index +=1

"""
3. Stwórz dwie listy i dodaj je do siebie
"""
Agnes_list = [ 123, 1, 2, 3]
itsdkey_list = [ 'eloo', 'ziomki']
c = Agnes_list + itsdkey_list
print(Agnes_list + itsdkey_list) #ok

for value in itsdkey_list:
  Agnes_list.append(value)
print(Agnes_list)

Agnes_list.extend(itsdkey_list)  # agnes_list rozszerz o itsdkey_list
print(Agnes_list)




"""
4. Stwórz listę 10-cio elementową, wypełnij ją i:
a) wyświetl elementy o indeksach 2,3,6
b) wyświetl pierwsze 3 elementy
c) wyświetl elementy o indeksach 3,4,5,6,7
d) wyświetl 3 ostatnie elementy
e) wyświetl co drugi element
"""
my_list = [i for i in range(10)] # [0, 1, 2, ... , 9]
print('### punkt 4.a)')
print(my_list[2])
print(my_list[3])
print(my_list[6])
print('### punkt 4.b)')
print(my_list[0:3])
print('### punkt 4.c)')
print(my_list[3:8])  # <3: 8)
print('### punkt 4.d)')   # <7:10)
print(my_list[7:10])   # <start;end)
print(my_list[7:])   # <start;end)
print(my_list[-3:])   # <start;end)
print('### punkt 4.e)')
print(my_list[::2])   # <start;end)  # parzyste indexy
print(my_list[1::2])   # <start;end) # niepatrzyste indexy

# <start;end) i inc(co który element) -> [start:end:inc]
"""
5. Wykonaj następujące działania:
a) Poproś użytkownika o podanie liczby, która będzie oznaczać pojemność listy (nazwijmy ją SIZE)
b) Następnie poproś użytkownika o podanie SIZE elementów i zapisz je do listy
c) Wyświetl otrzymaną listę w dowolny sposób

range (start, end) - funkcja zwraca liste z wartosciami <start;end), np. range(2) -> [0, 1], range(1,4) -> [1,2,3]
Przykład:
Size = 3
1
Temp
2.5
wynik: ['1', 'Temp', '2.5']
"""
my_list = []
size = input('podaj wielkosc listy: ')
size = int(size)
inc = 0
while inc < size:
  a = input('podaj element ')
  my_list.append(a)
  inc +=1
print(my_list)#moze zapropunojue moim kolegom


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
liczba 10 jest już w liście. numbers=[10, 9]
podaj liczbe: 8
podaj liczbe 245
...
wynik: [10, 9, 8, 245, ... ] <- w liście ma być 10 elementów
"""



"""
9.* Poproś użytkownika o podanie 5ciu liczb i zapisz je do listy. następnie zsumuj te liczby

Zadanie zrealizuj za pomocą dwóch pętli for lub wbudowanej funkcji 'sum'.

Przykład:
podaj liczbe: 1
podaj liczbe: 2
podaj liczbe: 3
podaj liczbe: 100
podaj liczbe: 22
wynik: 128
"""
