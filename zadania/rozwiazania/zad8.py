"""
        Zadania

1. Stwórz tuple i ją wyświetl
"""
my_tuple = (1, 'test', {'key': 123})
print(my_tuple)


"""
2. Stwórz funkcję, która przyjmie parametr N.
    Funkcja powinna zwrócić:
        2x powielone N jeśli N jest podzielne przez 2,
        3x powielone N jeśli N jest podzielne przez 5,
        5x powielone N jeśli N jest podzielne przez 10,
Przykłady:
N = 4
wynik: 4, 4
N = 15
wynik: 15, 15, 15
N = 20
wynik: 20, 20, 20, 20, 20
"""


def dummy_function(n):
    if n % 10 == 0:
        return (n,) * 5
    elif n % 2 == 0:
        return (n,) * 2
    elif n % 5 == 0:
        return (n,) * 3


print(dummy_function(4))
print(dummy_function(15))
print(dummy_function(20))

"""
3. Stwórz tuple i wyświetl tuple składającą się z elementów 
    pod nieparzystymi indexami
Przykład:
my_tuple = (1, 10, 23, 'test', {'test': 'value'}, 'to jest przyklad zdania')
wynik: (10, 'test', 'to jest przykład zdania')
"""
from random import randint
my_tuple = tuple(randint(10, 333) for i in range(10))
print(my_tuple)
print(my_tuple[1::2])

"""
4. Stwórz 3-elementową tuple i funkcję która przyjme 3 parametry.
    Następnie przekaż te elementy do funkcji za pomocą operacji unpacking
"""


def dummy_function_with_three_parameters(a, b, c):
    print(f'{c=}, {b=} {a=}')


my_tuple = ('test', [1234, 123, 1], 10)
dummy_function_with_three_parameters(*my_tuple)


"""
5. Stwórz funkcję która przyjmie nieznaną liczbę parametrów pozycyjnych
    i wypisze:
        'nieparzysta liczba parametrów' jeśli podana liczba parametrów
            jest nieparzysta
        'parzysta liczba parametrów' jeśli podana liczba parametrów
            jest parzysta
"""


def check_if_even(*args):
    if len(args) % 2 == 0:
        return 'parzysta liczba parametrów'
    else:
        return 'nieparzysta liczba parametrów'


print(check_if_even(1, 2, 3, 4, 5, 6))
print(check_if_even('test', {(1, 2): 123}))
print(check_if_even('', None, 123))

"""
6. Stwórz funkcję która przyjmuje następujące parametry:
    a - tuple z elementami
    b - index
    Następnie zwróc element pod danym indexem
"""


def return_value(local_tuple, index):
    return local_tuple[index]


print(return_value((None, {(1, 2): 'test'}, 'temp', 123), 0))
print(return_value((None, {(1, 2): 'test'}, 'temp', 123), 1))
print(return_value((None, {(1, 2): 'test'}, 'temp', 123), 2))
print(return_value((None, {(1, 2): 'test'}, 'temp', 123), 3))
"""
7. Stwórz tuple na podstawie danych podanych przez użytkownika oddzielonych 
    spacjami. Następnie przyjmij paramtr od użytkownika i sprawdz czy podana
    wartość jest w tupli. Wyświetl 'jest' jeśli jest, a 'nie ma' jeśli wartość
    nie została znaleziona.
"""


def search_for_value(values, value):
    if value in values:
        return 'jest'
    return 'nie ma'


values = input('Podaj elementy oddzielone spacjami: ')
values = values.split(' ')
value = input('Czego szukamy? ')
print(search_for_value(values, value))
