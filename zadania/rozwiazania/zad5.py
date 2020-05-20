print("########## Punkt 1 ##########")
temp = [1, 2, 3]
print(temp)


print("########## Punkt 2 ##########")
temp = [1, 2, 3]
index = 0
for value in temp:  # enumerate
    print(f'{index}: {value}')
    index += 1


print("########## Punkt 3 ##########")
first = [1, 2, 3, 4]
second = [1, 5, 6, 7]
result = first + second
print(result)


print("########## Punkt 4 ##########")
temp = [i for i in range(10)]
print(f'a) {temp[2]}, {temp[3]}, {temp[6]}')
print(f'b) {temp[:3]}')
print(f'c) {temp[3:8]}')
print(f'd) {temp[7:]}')  # print(f'd) {temp[-3:]}')
print(f'e) {temp[::2]}')


print("########## Punkt 5 ##########")
size = input('podaj wielkosc listy: ')
size = int(size)
my_list = []
for i in range(size):
    value = input('podaj jakas wartosc: ')
    my_list.append(value)
print(my_list)
print(my_list[-3:])


print("########## Punkt 6 ##########")
"""
Aby wykonać zadanie są dwie opcję:
a) zrobić nową listę i dodawać do niej elementy z pierwszej listy, których nie ma w drugiej (za pomocą operacji .append())
b) chytrze zrobić kopie pierwszej listy za pomocą [:], po której będizemy przechodzić podczas pętli for

Opcja B jest trudniejsza ze względu, że trzeba wiedzieć ciut więcej:
    - podczas przechodzenia po liście 'first' i usuwaniu z niej elementów zmienia się także jej struktura,
      bo zabieramy elementy lecz 'index' kolejnego obrotu nadal zostaje zwiększony o 1. Taki przykład:
      my_list = [1,2,3]
      for value in my_list:
          my_list.remove(value)
      print(my_list) < --- wypisze nam [2], ponieważ '2' "ukryła się" przed przejściem. Podczas pierwszej pętli usuneliśmy
                           pierwszy element, co skutkuje iż my_list = [2,3]. Kolejnym elementem podczas następnego obrotu
                           będzie element pod index'em 1, czyli '3'.
    - w związku z tym, musimy do pętli przekazać kopię listy 'first'. Która będzie przechodzić po kolejnych elementach 
      'w normalny sposób' a z prawdziwej listy 'first' będziemy usuwać elementy.
"""
first = [1, 2, 33, 48, 22, 4, 5, 6, 100, 1, 2, 44, 44]
second = [1, 2, 3]
result = []
for value in first[:]:  # [:] - stworzy nam się 'ukryta' kopia listy 'first' i będziemy mogli z niej usuwać elementy
    print(f'{value=}')
    if value in second:
        first.remove(value)
print(first)


print("########## Punkt 7 ##########")
import random
print('#### punkt a ####')
lotto = []
for i in range(10):
    lotto.append(random.randint(1, 64))
print(f'{lotto=}')

print('#### punkt b ####')
lotto = []
how_many_numbers = 10
while len(lotto) < how_many_numbers:
    value = random.randint(1, 64)
    if value not in lotto:
        lotto.append(value)
print(f'{lotto=}')


print("########## Punkt 8 ##########")
numbers = []
while len(numbers) < 10:
    value = int(input('podaj liczbe: '))
    value = int(value)
    if value in numbers:
        print(f'liczba {value} jest już w liście. {numbers=}')
    else:
        numbers.append(value)
print(numbers)


print("########## Punkt 9 ##########")
"""
Te zadanie można zrobić na 2 sposoby (według treści):
a) za pomocą dwóch pętli for - musimy wpierw zebrać liczba a póżniej każdy element z listy do siebie dodać
b) za pomocą 1 pętli for i wbudowanej funkcji 'sum':
    Funkcja sum - sumuje wartości w kolekcji (np. liście). link: https://docs.python.org/3/library/functions.html#sum
"""
numbers = []
for i in range(5):
    number = input('podaj liczbe: ')
    number = int(number)
    numbers.append(number)

print('#### sposób z dwoma pętlami ####')
result = 0
for number in numbers:
    result += number  # result = result + number
print(result)

print('#### sposób z sum ###')
result = sum(numbers)
print(result)
