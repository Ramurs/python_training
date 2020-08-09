from sda_ex_oop_1_mz.ex1_10.cat import Cat
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
