import math


def trojkat(bok1: int, bok2: int):

        try:
            bok3 = math.sqrt(bok1 ** 2 + bok2 ** 2)
            return bok3

        except TypeError:
            raise TypeError('Nie wpisałeś liczby. Podaj ponownie długość boku trójkąta.')

trojkat(3,4)