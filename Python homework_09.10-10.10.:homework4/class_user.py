from datetime import date, datetime

from class_human import Human


class User(Human):
    def __init__(self, first_name, last_name, date_of_birth, age=0):
        super().__init__(self, first_name, last_name, date_of_birth)
#         self.age = age
### Nie ma sensu dawać możliwości ustawiania tego ręcznie

    @property
    def age(self):
        today = date.today()
#         date_of_birth = datetime.date(2015, 3, 12)
#         self.age = today.year - date_of_birth.year

        ### załóżmy że self.datetime == '11-05-1994'
        birth = datetime.strptime(self.date_of_birth, '%d-%m-%Y')
# Ta odpowiedź jest bardzo mało dokładna bo nie uwzględnia lat przestępnych ani miesięcy ale do nauki wystarczy
        return today.year - birth.year


### setter nie jest potrzebny jeśli ma być to tylko wartość obliczana na bieżąco
#     @age.setter
#     def age(self, value):
#         self.age = value

