#bankomat

def bankomat():

    karty = {1: {'pin': 1234, 'saldo': 1234}, 2: {'pin': 345, 'saldo': 543}}
    numer = int(input('podaj numer konta: '))

    while True:
        if numer in karty:
            pin = int(input('podaj pin: '))
            if karty[numer]['pin'] == pin:
                print('co chciałbyś zrobić: ')
                print('1.odczytaj saldo')
                print('2.wpłać pieniądze')
                print('3.wypłać pieniądze')
                print('4.zmien pin: ')
                print('0.Wyjdź z programu')
                option = input("podaj numer opcji: ")
                if option == "1":
                    print(karty[numer]['saldo'])
                    input('nacisnij enter, aby wrocic do głównego menu')
                elif option == "2":
                    wplata = int(input('podaj ile chcesz wplacic: '))
                    saldo = (karty[numer]['saldo']) + wplata
                    print(f'Twoje nowe saldo wynosi: {saldo}')
                    input('nacisnij enter, aby wrocic do głównego menu')
                elif option == "3":
                    wyplata = int(input('podaj ile chcesz wyplacic: '))
                    if wyplata > (karty[numer]['saldo']):
                        print('nie masz tyle pieniędzy')
                        input('nacisnij enter, aby wrocic do głównego menu')
                    else:
                        saldo = (karty[numer]['saldo']) - wyplata
                        print(f'Twoje nowe saldo wynosi: {saldo}')
                        input('nacisnij enter, aby wrocic do głównego menu')
                elif option == "4":
                    nowy_pin = int(input('podaj nowy pin: '))
                    karty[numer]['pin'] = nowy_pin
                    print(f'Twoj PIN zostal zmieniony na {nowy_pin}')
                    input('nacisnij enter, aby wrocic do głównego menu')
                elif option == "0":
                    break

                else:
                    print('wybierz poprawną opcję')
                    input('nacisnij enter, aby wrocic do głównego menu')
            else:
                print('pin niezgodny')
                input('nacisnij enter, aby wrocic do głównego menu')

        else:
            print('nie ma takiego numeru konta')

bankomat()
