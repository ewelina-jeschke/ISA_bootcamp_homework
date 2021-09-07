'''Stwórz funkcję nazwaną dodajListy() która zwróci nową listę sumując ze sobą
elementy na tych samych indeksach  . Możesz przypuścić,
że jako parametry do funkcji podawane są zawsze listy zawierające tylko liczby.
Jeżeli listy są różnej długości, funkcja powinna wyświetlić napis
Podane listy muszą być tej samej długości'''

def Dodaj_Listy():
    lista1 = [1,3,4]
    lista2 = [4,5,6]
    lista3 = []

    if len(lista1) != len(lista2):
        print("listy muszą być tej samej długości")
    else:
        for n in range(len(lista1)):
            wynik = lista1[n] + lista2[n]
            lista3.append(wynik)
    return lista3

print(Dodaj_Listy())

"""Stwórz funkcję nazwaną zbadajTrojkat() 
która przyjmie jako argumenty długości boków trójkąta. 
Funkcja powinna zwrócić, czy trójkąt jest prostokątny, równoramienny, 
równoboczny, różnoboczny lub nieprawidłowy """

def Zbadaj_Trojkat():
    bok1 = int(input("podaj dlugość boku nr 1: "))
    bok2 = int(input("podaj długość boku nr 2: "))
    bok3 = int(input("podaj długość boku nr 3: "))

    if (bok1+bok2 > bok3) and (bok1+bok3 > bok2) and (bok2+bok3 > bok1):
        if bok1 == bok2 and bok2 == bok3:
            print("trójkąt jest równoboczny")
        elif bok1 == bok2 or bok2 == bok3 or bok1 == bok3:
            print("trójkąt jest równoramienny")
        elif (bok1 ** 2 + bok2 ** 2 == bok3 ** 2) or (bok1 ** 2 + bok3 ** 2 == bok2 ** 2) or (bok2 ** 2 + bok3 ** 2 == bok1 ** 2):
            print("trójkąt jest prostokątny")
        elif bok1 != bok2 and bok2 != bok3 and bok3 !=bok1:
            print("trójkąt jest różnoboczny")
    else:
        print("trójkąt jest nieprawidłowy")

Zbadaj_Trojkat()



