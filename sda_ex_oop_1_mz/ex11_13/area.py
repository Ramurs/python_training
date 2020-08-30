from sda_ex_oop_1_mz.ex11_13.figures import Figures
from math import pi as PI

class Rectangle(Figures):

    def __init__(self, height: float, witdth: float):
        self.height = height
        self.witdth = witdth

    def get_area(self) -> float:
        return self.height * self.witdth

class Circle(Figures):
    def __init__(self, radius: float):
        self.radius = radius

    def get_area(self) -> float:
        return PI * self.radius * self.radius

class Triangle(Figures):
    def __init__(self, height: float, base: float):
        self.height = height
        self.base = base

    def get_area(self) -> float:
        return 0.5 * self.height * self.base

def main():
    rectangle1 = Rectangle(5, 4)
    circle1 = Circle(5)
    triangle1 = Triangle(5, 4)
    area_sum : float = rectangle1.get_area() + circle1.get_area() + triangle1.get_area()
    print(f'Suma pol figur to: {area_sum}')

    x = float(input("Podaj wartosc x "))
    if x >= area_sum:
        print("Można pomalowac wszystkie podane figury")
    else:
        print("Nie mozna pomalowac")

if __name__ == "__main__":
    main()

'''
Rozwiązanie z zajęć:
from oop_training_1.car import MyCar
from oop_training_1.my_cat import MyCat
from oop_training_1.my_dog import MyDog
from oop_training_1.my_vet import MyVet
from oop_training_1.oop_figure_11_13.area_checker import AreaChecker
from oop_training_1.oop_figure_11_13.figures import Rectangle, Circle, Triangle
from oop_training_1.oop_figure_11_13.utils import figures_sum


def cat_creator() -> list:
    cats = []
    cat1 = Cat("Panda")
    cat2 = Cat("Filemon")
    cat1.eat_mouse()
    cats.append(cat1)
    cats.append(cat2)
    return cats


def animal_creator() -> list:
    animals = []
    cat1 = MyCat("Panda")
    cat2 = MyCat("Filemon")
    dog1 = MyDog("Ronie")
    dog2 = MyDog("Lucy")
    animals.append(cat1)
    animals.append(cat2)
    animals.append(dog1)
    animals.append(dog2)
    return animals


def main():
    # cat = Cat("Mruczek")
    # print(cat.make_sound())
    # cats = cat_creator()
    # for cat in cats:
    #     print(cat.make_sound())
    #     cat.eat_mouse()
    # wersja zajec
    cat = MyCat("Mruczek")
    print(cat.name)
    # cat.name = "Patus"
    cat.make_sound()
    print(cat.age)
    # cat.age = 2
    cat.age2(2)
    print(cat.age)
    # print("Ex2")
    # make_cat_list()
    print("Ex3")
    cat.eat_mouse()
    cat.eat_mouse()
    cat.eat_mouse()
    dog = MyDog("Ronie")
    dog.make_sound()
    animals = animal_creator()
    for animal in animals:
        animal.make_sound()

    car = MyCar()
    car.move()

    cat.move()
    print("Ex 8")

    MyVet.say_cat_hello(cat)
    MyVet.say_dog_hello(dog)
    MyVet.say_hello(cat)

    print("Ex 11-13")
    rectangle = Rectangle(10.0, 12.0)
    r_area = rectangle.get_area()
    print(r_area)

    circle = Circle(3.4)
    c_area = circle.get_area()
    print(c_area)

    triangle = Triangle(10.0, 12.0)
    t_area = triangle.get_area()
    print(t_area)

    figures_list = [rectangle, circle, triangle]
    sum_figures_are = figures_sum(figures_list)
    print(sum_figures_are)

    print("Ex 13")
    enough = AreaChecker.check_area(220.0, figures_list)
    print(enough)

if __name__ == "__main__":
    main()
'''