from sda_ex_oop_2_mz.person import Person
from datetime import date

class Employee(Person):
    def __init__(self, name: str, surname: str, birthday: date, salary=1000.0):
        birthday = self.check_date(birthday)
        super().__init__(name, surname, birthday)
        self._salary = salary

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        value = self.check_date(value)
        self._birthday = value

    @staticmethod
    def check_date(value: date) -> date:
        if value > date(2020, 12, 31) or value < date(1900, 1, 1):
            value = date(0, 0, 0)
        return value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    def who_am_i(self):
        print(f' nazywam sie {self.name} {self.surname} i zarabiam {self.salary} zl')
