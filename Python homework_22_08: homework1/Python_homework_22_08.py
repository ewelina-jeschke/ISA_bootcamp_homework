while True:
    print('1: Oblicz średnią arytmetyczną')
    print('2: Podnieś do potęgi')
    print('3: Porównaj liczby')
    print('4: Wyjdź')
    decyzja = input('Podaj opcję, którą chcesz wybrać: ')

    if decyzja == '1':
        liczba_1 = int(input("podaj pierwszą liczbę: "))
        liczba_2 = int(input("podaj drugą liczbę: "))
        print((liczba_1 + liczba_2) / 2)
    elif decyzja == '2':
        liczba_1 = int(input("podaj podstawę, czyli liczbę, którą chcesz podnieść do potęgi "))
        liczba_2 = int(input("podaj wykładnik "))
        print(liczba_1 ** liczba_2)
    elif decyzja == '3':
        liczba_1 = int(input("podaj pierwszę liczbę: "))
        liczba_2 = int(input("podaj drugą liczbę: "))
        if liczba_1 > liczba_2:
            print(liczba_1)
        elif liczba_1 < liczba_2:
            print(liczba_2)
        else:
            print("obie liczby są takie same")
    elif decyzja == '4':
        quit()

    else:
        print("Wprowadź poprawną wartość")
                       
