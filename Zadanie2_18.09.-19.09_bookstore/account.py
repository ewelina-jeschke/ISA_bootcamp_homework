class Account:
    next_number = 1
    ### w programowaniu liczymy od zera :)

    def __init__(self, owner, pin, balance=0):
        self.id = self.next_number
        self.owner = owner
        self.pin = pin
        self.balance = balance
        Account.next_number += 1
