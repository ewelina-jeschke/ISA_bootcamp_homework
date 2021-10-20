import json


user_database = {}

def store_user_data():

    first_name = input('Podaj imię: ')
    last_name = input('Podaj nazwisko: ')
    while True:
        try:
            phone_no = input('Podaj 9-cyfrowy numer telefonu: ')
            user_database['imie'] = first_name
            user_database['nazwisko'] = last_name
            user_database['telefon'] = phone_no

            phone_no = phone_no.replace(" ", "").replace("-", "")
            if len(str(phone_no)) == 9:
                print('Numer telefonu jest prawidłowy, dane użytkownika zostały zapisane.')
                break

            else:
                print('Podany numer telefonu jest nieprawidłowy. Spróbuj ponownie.')


        except ValueError:
            print('Podany numer telefonu jest nieprawidłowy.')

        finally:
            with open('user_database.json', 'w') as database_file:
                json.dump(user_database, database_file)

store_user_data()
