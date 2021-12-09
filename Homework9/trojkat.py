import math

def Trojkat():

    while True:
        try:
            bok1 = int(input("podaj dlugość boku nr 1: "))
            bok2 = int(input("podaj długość boku nr 2: "))

            bok3 = math.sqrt(bok1 ** 2 + bok2 ** 2)
            print(f'Długość trzeciego boku wynosi {bok3}')
            break

        except ValueError:
            print('Nie wpisałeś liczby. Podaj ponownie długość boku trójkąta.')

Trojkat()