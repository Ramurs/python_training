'''from sda_ex_oop_1_mz.ex1_10.cat import Cat
from sda_ex_oop_1_mz.ex1_10.dog import Dog
from sda_ex_oop_1_mz.ex1_10.animal import Animal

class Vet:

    @staticmethod
    def say_cat_hello(cat: Cat):
        print(f'Hello {cat.name}')

    @staticmethod
    def say_dog_hello(dog: Dog):
        print(f'Hello {dog.name}')

    @staticmethod
    def say_animal_hello(animal: Animal):
        print(f'Hello {animal.name}')
'''
from sda_ex_oop_1_mz.ex1_10.cat import Cat
from sda_ex_oop_1_mz.ex1_10.dog import Dog


class Vet:
    def __init__(self, cat_name, dog_name):
        self.cat = Cat(
            cat_name)  # tutaj wołasz konstruktor kota więc tworzysz kota nie jego imie, do tego "name" jest puste w Cat(name) musisz je podać wczesniej np. w metodzie init
        self.dog = Dog(dog_name)  # tutaj analogicznie

    def say_cat_hello(self):
        return (
            f'Witaj {self.cat.name}')  # tutaj wskazujesz obiet self.cat a potem jego pole po kropce .name czyli imie zawierajace sie w srodku kota

    def say_dog_hello(self):
        print(f'Witaj {self.dog.name}')  # analogicznie


def main():
    vet1 = Vet("burek",
               "reksio")  # Vet("imie kota do podania", "imie psa do podania") jest wolany poprzez metode  __init__(self, cat_name, dog_name):
    print(f'{vet1.say_cat_hello()}')


if __name__ == "__main__":
    main()
