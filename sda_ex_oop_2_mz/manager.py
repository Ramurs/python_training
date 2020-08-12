from datetime import date
from sda_ex_oop_2_mz.employee import Employee
class Manager(Employee):

    def __init__(self, name: str, surname: str, birthday: date, salary=1000.0):
        salary = 1.1 * salary
        super().__init__(name, surname, birthday, salary)


    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value: float):
        value = self._salary * 1.1
        self._salary = value

    def who_am_i(self):
        print(f'Nazywam się {self.name} {self.surname} i zarabiam {self.salary} zl')
