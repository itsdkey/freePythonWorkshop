"""
    Zadania

    1. Stwórz klasę Stos, która będzie posiadać:
        a) atrybut klasowy: stack - lista, która będzie używana w ramach stosu
        b) atrybut: name, który będzie używany by określać jaki to jest stos
        c) metodę "add", która będzie dodawać element na początek listy,
        d) metodę "pop", która usunie i wyświetli pierwszy element z listy,
        e) metodę "length", która zwróci aktualną wielkość stosu
        f) metodę "clear", która będzie zdejmować kolejne elementy z listy aż do jej wyczyszczenia
    1.1 Stwórz dwie instancje typu Stos
    1.2 Dodaj 3 elementy do pierwszego stosu, wyświetl dwa stosy
    1.3. Wykorzystaj atrybut instancyjny by naprawić błąd związany z punktem 1.2
"""


class Stack:
    stack = []

    def __init__(self, name):
        self.name = name

    def add(self, element):
        self.stack.insert(0, element)

    def pop(self):
        element = self.stack.pop()
        print(f'zdjęty element to: {element=}')

    def length(self):
        return len(self.stack)

    def clear(self):
        while self.stack:
            self.pop()


first_name = 'first'
second_name = 'second'
s1, s2 = Stack(first_name), Stack(second_name)
for i in range(3):
    s1.add(i)

print(s1.stack, s2.stack)


from random import randint


class GoodStack:

    def __init__(self, name):
        self.name = name
        self.stack = []

    def add(self, element):
        self.stack.insert(0, element)

    def pop(self):
        element = self.stack.pop()
        print(f'zdjęty element to: {element=}')

    def length(self):
        return len(self.stack)

    def clear(self):
        while self.stack:
            self.pop()


third_name = 'third'
forth_name = 'forth'
s3, s4 = GoodStack(third_name), GoodStack(forth_name)
for i in range(3):
    s3.add(randint(16, 2048))

print(s1.stack, s2.stack)

"""
    2. Stwórz listę tych Stosów, pomieszaj jej kolejnosc i wyswietl stan stosu o nazwie 'third'
"""
from random import shuffle
stacks = [s1, s2, s3, s4]
shuffle(stacks)
for stack in stacks:
    if stack.name == third_name:
        print(f'{stack.stack=}')

"""
    3. Stwórz grę 'race'. Gra polega na rzucaniu kostką przez kolejnych graczy.
    Po każdym rzucie należy sumować ilość oczek na konto gracza.
    Gracz który jako pierwszy osiągnie ustalony wynik (meta) wygrywa.
    Do realizacji zadania będą potrzebne dwie klasy: Game oraz Player
    Klasa Game powinna odpowiadać za przebieg gry:
        1. Ustalenie mety,
        2. Stworzeniu graczy
        3. Kolejnych rundach gry i ustaleniu zwycieżcy
    Klasa Player powinna odpowaidać za:
        1. Określenie, kto jest graczem,
        2. Rzucie kostką
        3. Przechowywaniu swojego wyniku
"""
from random import randint, shuffle


class Player:
    """Class representing a player."""

    def __init__(self, name):
        self.name = name
        self.points = 0

    def roll(self):
        points = randint(1, 6)
        print(f'rzuciłem: {points}')
        self.points += points


class Game:
    """Class representing a 'race' game."""

    def __init__(self, max_points, max_number_of_players):
        self.max_points = max_points
        self.max_number_of_players = max_number_of_players
        self.players = []
        self.number_of_players = 0

    def create_player(self, name):
        if len(self.players) < self.max_number_of_players:
            self.players.append(Player(name))
            self.number_of_players += 1
        else:
            print('osiągnięto limit graczy!')

    def play(self):
        shuffle(self.players)
        index = 0
        while True:
            player = self.players[index]
            print(f'Kolej gracza {player.name}')
            player.roll()
            if player.points >= self.max_points:
                print(f'Wygrał gracz {player.name}!')
                break
            index += 1
            index %= self.number_of_players


number_of_players = input('Ile chcesz dodać graczy? ')
number_of_players = int(number_of_players)

max_points = input('Do ilu gramy? ')
max_points = int(max_points)
game = Game(max_points, number_of_players)

for i in range(number_of_players):
    name = input('podaj imie gracza: ')
    game.create_player(name)

game.play()