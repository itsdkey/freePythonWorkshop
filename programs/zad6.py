print("########## Punkt 1 ##########")
temp = {'temp': 1, 2: 3, 'klucz': [1, 2, 3], 'slownik': {'temp': 1}}
print(temp)


print("########## Punkt 2 ##########")
temp = {}
for i in range(3):
    key_and_value = input('podaj klucz i wartosc (klucz wartosc): ')
    key, value = key_and_value.split(' ')
    temp[key] = value
print(temp)


print("########## Punkt 3 ##########")
temp = {}
for i in range(3):
    key_and_value = input('podaj klucz i wartosc (klucz wartosc): ')
    key, value = key_and_value.split(' ')
    if key in temp:
        temp[key].append(value)
    else:
        temp[key] = [value]
print(temp)


print("########## Punkt 4 ##########")
print("########## Podpunkt a) ##########")
first = {'temp': 1, 2: 3, 'klucz': 'wartosc'}
second = {'temp': 'test', 33: 'wartosc2'}
third = {**first, **second}
print(third)

print("########## Podpunkt b) ##########")
first = {'temp': 1, 2: 3, 'klucz': 'wartosc'}
second = {'temp': 'test', 33: 'wartosc2'}
third = first
third.update(second)
print(third)

print("########## Podpunkt c) ##########")
first = {'temp': 1, 2: 3, 'klucz': 'wartosc'}
second = {'temp': 'test', 33: 'wartosc2'}
third = first
for key, value in second.items():
    third[key] = value
print(third)


print("########## Punkt 5 ##########")
from datetime import datetime
today = datetime.now()
day = today.weekday()
print(f'{today=}, weekday: {day}')
days = {
    0: 'poniedzialek',
    1: 'wtorek',
    2: 'środa',
    3: 'czwartek',
    4: 'piątek',
    5: 'sobota',
    6: 'niedziela',
}
print(days[day])


print("########## Punkt 6 ##########")
print("########## Sposob 1 ##########")
sentence = 'ala ma kota kot ma ale. Ala ona lorem ipsum Test test test raz dwa trzy mam zajawke na super zdanie'
words = sentence.lower().split(' ')
counts = {}
for word in words:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1

sorted_asc = sorted(counts.items(), key=lambda x: x[1])  # rosnąco
print(sorted_asc)
sorted_desc = sorted(counts.items(), key=lambda x: x[1], reverse=True)  # malejąco
print(sorted_desc)

print("########## Sposob 2 ##########")
from collections import Counter
sentence = 'ala ma kota kot ma ale. Ala ona lorem ipsum Test test test raz dwa trzy mam zajawke na super zdanie'
words = sentence.lower().split(' ')
counts = Counter(words)

sorted_asc = sorted(counts.most_common(), reverse=True)  # rosnąco
print(sorted_asc)
sorted_desc = counts.most_common()  # most_common() domyślnie zwraca w kolejności malejącej
print(sorted_desc)


print("########## Sposob 3 ##########")
from collections import defaultdict
sentence = 'ala ma kota kot ma ale. Ala ona lorem ipsum Test test test raz dwa trzy mam zajawke na super zdanie'
words = sentence.lower().split(' ')
counts = defaultdict(int)  # domyślnie int() zwraca 0. Do defaultdict przekazujemy funkcję, która powinna się wykonać gdy danego klucza nie ma w słowniku
for word in words:
    counts[word] += 1

sorted_asc = sorted(counts.items(), key=lambda x: x[1])  # rosnąco
print(sorted_asc)
sorted_desc = sorted(counts.items(), key=lambda x: x[1], reverse=True)  # malejąco
print(sorted_desc)
