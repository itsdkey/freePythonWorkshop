def fill_list(size):
    """Wypełnij listę o SIZE elementów.

    :param size: rozmiar listy
    :returns: wypełniona SIZE-elementowa lista
    """
    result = []
    iterator = 0
    while iterator < size:
        value = input('Podaj liczbę całkowitą: ')
        try:
            value = int(value)
        except ValueError:
            print('Podana liczba nie jest liczbą całkowitą, podaj inną')
        else:
            result.append(value)
            iterator += 1
    return result


def choose_option(inner_list):
    """Wyświetlenie i wybór dostępnych opcji.

    :param inner_list: lista z liczbami całkowitymi
    """
    options = {
        1: 'wyszukanie liczb parzystych',
        2: 'wyszukanie liczb nieparzystych',
    }
    print('Wybierz jedną z dostępnych opcji')
    for key in options:
        print(f'{key}: {options[key]}')

    while True:
        option = input('opcja: ')
        option = int(option)
        if option not in options:
            print('Wybrałeś nieprawidłową opcję, wybierz ponownie')
        else:
            break

    print(f'Wybrałeś opcję: {options[option]}')
    if option == 1:
        find_even(inner_list)
    else:
        find_odd(inner_list)


def find_even(values):
    """Wyszukaj liczby parzyste.

    :param values: lista z liczbami calkowitymi
    :returns: lista ze znalezionymi liczbami parzystymi bez powtorzeń.
    """
    result = []
    print(f'lista: {values}')
    for value in values:
        if value % 2 == 0 and value not in result:
            result.append(value)
    print(f'wynik: {result}')


def find_odd(values):
    """Wyszukiwanie liczb nieparzystych.

    :param values: lista z liczbami całkowitymi
    :returns: lista ze znalezionymi liczbami nieparzystymi z powtórzeniami.
    """
    result = []
    print(f'lista: {values}')
    for value in values:
        if value % 2 != 0:
            result.append(value)
    print(f'wynik: {result}')


if __name__ == '__main__':
    size = input('Podaj rozmiar listy: ')
    size = int(size)
    my_list = fill_list(size)
    choose_option(my_list)
