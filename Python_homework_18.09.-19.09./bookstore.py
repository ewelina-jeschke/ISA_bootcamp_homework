from client import Client
from books import Books
from account import Account


class Bookstore:
    client_list = []
    book_list = []
    account_list = []

    def __init__(self):
        self.main()

    def print_menu(self):
        print('wybierz opcje: ')
        print(10 * '*')
        print('1. Załóż konto klienta')
        print('2. Pokaż konta klientów')
        print('3. Wprowadź kartę płatniczą klienta')
        print('4. Ustaw bilans na karcie klienta')
        print('5. Sprawdź ile klient zakupił książek i czy otrzyma gratis')
        print('6. Ustaw listę dostępnych książek')
        print('7. Ustaw stany magazynowe książki')
        print('8. Pokaż listę książek')
        print('9. Sprzedaj książki klientowi i pokaż kwotę do zapłaty po uwzględnieniu promocji')
        print('0. Wyjdź z programu')

    def set_client_account(self):
        name = input('Podaj imię klienta: ')
        surname = input('Podaj nazwisko: ')
        age = int(input('Podaj wiek: '))
        client = Client(name, surname, age)
        Bookstore.client_list.append(client)


    def show_client_accounts(self):
        for client in Bookstore.client_list:
            print(vars(client))

    def set_client_bank_card(self):
        def check_if_client_exists(client_id):
            for client in Bookstore.client_list:
                if client.id == client_id:
                    return client
                else:
                    continue
            return False

        client_id = int(input('Podaj id klienta: '))
        client = check_if_client_exists(client_id)
        if client:
            owner = input('Podaj imię i nazwisko właściciela: ')
            pin = int(input('Podaj PIN: '))
            account = Account(owner, pin)
            Bookstore.account_list.append(account)
            print(vars(account))
        else:
            print('Nie ma takiego klienta')

    def set_balance_on_client_bank_card(self):
        def check_if_client_exists(client_id):
            for client in Bookstore.client_list:
                if client.id == client_id:
                    return client
                else:
                    continue
            return False

        client_id = int(input('Podaj id klienta: '))
        client = check_if_client_exists(client_id)
        if client:
            def check_if_client_bank_card_exists(account_id):
                for account in Bookstore.account_list:
                    if account.id == account_id:
                        return account
                    else:
                        continue
                return False

            account_id = int(input('Podaj id karty klienta: '))
            account = check_if_client_bank_card_exists(account_id)
            if account:
                new_balance = int(input('Podaj nowy bilans na karcie klienta: '))
                account.balance += new_balance
                print(f'Nowy bilans na karcie klienta wynosi {account.balance} zł.')
                print(vars(account))
            else:
                print('Wybrana karta klienta nie istnieje')
        else:
            print('Nie ma takiego klienta')

    def bought_books(self):
        def check_if_account_exists(client_id):
            for client in Bookstore.client_list:
                if client.id == client_id:
                    return client
                else:
                    continue
            return False

        client_id = int(input('Podaj id klienta: '))
        client = check_if_account_exists(client_id)
        if client:
            print(f'Klient zakupił {client.num_of_books} książek')
            if client.num_of_books >= 10:
                print('Klient otrzymuje gratis')
            else:
                print('Klient nie otrzymuje gratisu')
        else:
            print('Wybrane konto nie istnieje')


    def set_books(self):
        title = input('Podaj tytuł książki: ')
        author_name = input('Podaj nazwisko autora: ')
        publication_year = int(input('Podaj rok publikacji: '))
        price = int(input('Podaj cenę książki: '))
        book = Books(title, author_name, publication_year, price)
        Bookstore.book_list.append(book)
        print(vars(book))


    def set_stock_levels_of_books(self):
        def check_if_book_exists(book_id):
            for book in Bookstore.book_list:
                if book.id == book_id:
                    return book
                else:
                    continue
            return False

        book_id = int(input('Podaj id książki do ustawienia stanu magazynowego: '))
        book = check_if_book_exists(book_id)
        if book:
            copies = int(input('Podaj ilość stanu magazynowego '))
            book.num_of_copies += copies
            print(f'Dla ksiazki {book.title} mamy dostępnych {book.num_of_copies} egzemplarzy')
            print(vars(book))
        else:
            print('Wybrana książka nie istnieje')

    def show_books(self):
        for element in Bookstore.book_list:
            print(vars(element))


    def sell_book(self):
        def check_if_book_exists(book_id):
            for book in Bookstore.book_list:
                if book.id == book_id:
                    return book
                else:
                    continue
            return False

        def check_if_client_exists(client_id):
            for client in Bookstore.client_list:
                if client.id == client_id:
                    return client
                else:
                    continue
            return False

        def check_if_account_exists(account_id):
            for account in Bookstore.account_list:
                if account.id == account_id:
                    return account
                else:
                    continue
            return False

        book_id = int(input('Podaj id książki, którą chce kupić klient: '))
        book = check_if_book_exists(book_id)
        if book:

            new_num_of_copies = int(input('Podaj ile egzemplarzy klient chce kupić: '))
            if book.num_of_copies >= new_num_of_copies:
                print(f'Książka dostępna w cenie {book.price}')
                client_id = int(input('Podaj id klienta, który chce kupić książkę: '))
                client = check_if_client_exists(client_id)

                if client:
                    account_id = int(input('Podaj id karty klienta, z którego ma być dokonana zapłata: '))
                    account = check_if_account_exists(account_id)

                    if account:
                        pay_amount = book.price * new_num_of_copies
                        if account.balance >= pay_amount:
                            client.num_of_books += new_num_of_copies
                            book.num_of_copies -= new_num_of_copies
                            print(f'Książka sprzedana, klient ma {client.num_of_books} zakupionych książek.')
                            if pay_amount <= 100:
                                account.balance -= pay_amount
                                print(f'Klient ma do zapłaty {pay_amount} zl.')
                                print(f'Nowy bilans na karcie klienta to {account.balance} zl.')
                            else:
                                pay_amount *= 0.9
                                account.balance -= pay_amount
                                print(f'Klient uzyskał 10% rabatu za zakupy powyżej 100 zł, klient ma do zapłaty {pay_amount} zł.')
                                print(f'Nowy bilans na karcie klienta to {account.balance} zl.')
                        else:
                            print(f'Klient nie ma tyle pieniędzy, klient ma {account.balance} zł na koncie, a rachunek wynosi {pay_amount} zł.')
                    else:
                        print('Podana karta klienta nie istnieje')
                else:
                    print('Nie ma takiego klienta')

            else:
              print(f'Książka niedostępna, mamy jedynie {book.num_of_copies} egzemplarzy')
        else:
            print('Wybrana książka nie istnieje')

    def main(self):
        while True:
            self.print_menu()
            option = input('Podaj opcję: ')
            if option == '1':
                self.set_client_account()
                input('Naciśnij enter, aby wrocic do głównego menu ')
            elif option == '2':
                self.show_client_accounts()
                input('Naciśnij enter, aby wrocic do głównego menu ')
            elif option == '3':
                self.set_client_bank_card()
                input('Naciśnij enter, aby wrocic do głównego menu ')
            elif option == '4':
                self.set_balance_on_client_bank_card()
                input('Naciśnij enter, aby wrocic do głównego menu ')
            elif option == '5':
                self.bought_books()
                input('Naciśnij enter, aby wrocic do głównego menu ')
            elif option == '6':
                self.set_books()
                input('Naciśnij enter, aby wrocic do głównego menu ')
            elif option == '7':
                self.set_stock_levels_of_books()
                input('Naciśnij enter, aby wrocic do głównego menu ')
            elif option == '8':
                self.show_books()
                input('Naciśnij enter, aby wrocic do głównego menu ')
            elif option == '9':
                self.sell_book()
                input('Naciśnij enter, aby wrocic do głównego menu ')
            elif option == '0':
                break


Bookstore()
