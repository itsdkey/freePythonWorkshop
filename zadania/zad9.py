"""
    Temat: Klasy

Przykłady
    1. Stwórz klasę Player, która będzie posiadać atrybut klasowy health odpowiadający za stan życia.
    Następnie stwórz metodę "upgrade", która będzie zwiększać życie o 10 punktów.
    Stwórz teraz dwie instancje klasy Player.
    Dla piewszej instancji zwiększ życie o 10 punktów
    Wyświetl stan życia stworzonych graczy
    Spróbuj teraz większyć globalnie życie dla dwóch graczy.
"""


class Player:
    health = 100

    def upgrade(self):
        """Upgrade player's health bar."""
        self.health += 10  # self.health = self.health + 10


p1, p2 = Player(), Player()
p1.upgrade()
print(f'{p1.health=}, {p2.health=}')
Player.health += 20
print(f'{p1.health=}, {p2.health=}')


"""
    Zadania

    1. Stwórz klasę Stos, która będzie posiadać:
        a) atrybut klasowy: stack - lista, która będzie używana w ramach stosu
        b) atrybut instancyjny: name, który będziemy używać by określać jaki to jest stos
        c) metodę "add", która będzie dodawać element na szczyt stosu,
        d) metodę "pop", która usunie i wyświetli element ze szczytu stosu,
        e) metodę "length", która wyświetli aktualną wielkość stosu
        f) metodę "clear", która będzie zdejmować kolejne elementy ze stosu aż do jej   
    1.1 Stwórz dwie instancje typu Stos
    1.2 Dodaj 3 elementy do pierwszego stosu, wyświetl dwa stosy
    1.3. Wykorzystaj atrybut instancyjny by naprawić błąd związany z punktem 1.2
"""


"""
    2. Stwórz listę Stosów
"""


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