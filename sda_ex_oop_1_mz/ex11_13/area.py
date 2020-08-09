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