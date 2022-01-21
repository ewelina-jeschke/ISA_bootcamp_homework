import logging


def kalkulator():
    logger = logging.getLogger(__name__)

    logging.basicConfig(level=logging.DEBUG)

    try:
        liczba1 = int(input("podaj pierwszą liczbę: "))
        liczba2 = int(input("podaj drugą liczbę: "))

        print('Wybierz opcję')
        print('1: Dodaj liczby')
        print('2: Odejmij liczby')
        print('3: Pomnóż liczby')
        print('4: Podziel liczby')
        print('5: Wyjdź')
        decyzja = input('Podaj opcję, którą chcesz wybrać: ')

        if decyzja == '1':
            wynik = liczba1 + liczba2
            print(wynik)
        elif decyzja == '2':
            wynik = liczba1 - liczba2
            print(wynik)
        elif decyzja == '3':
            wynik = liczba1 * liczba2
            print(wynik)
        elif decyzja == '4':
            wynik = liczba1 / liczba2
            print(wynik)
        elif decyzja == '5':
            quit()

    except ValueError:
        logger.warning('nie wpisałeś liczby')

    except ZeroDivisionError:
        logger.error('nie dziel przez 0')

    else:
        logger.info('dane wejściowe zostały poprawnie zapisane')


kalkulator()