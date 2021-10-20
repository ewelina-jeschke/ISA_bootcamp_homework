from datetime import date, datetime

from class_human import Human


class User(Human):
    def __init__(self, first_name, last_name, date_of_birth, age=0):
        super().__init__(self, first_name, last_name, date_of_birth)
        self.age = age


    @property
    def age(self):
        today = date.today()
        date_of_birth = datetime.date(2015, 3, 12)
        self.age = today.year - date_of_birth.year
        return self.age



    @age.setter
    def age(self, value):
        self.age = value

