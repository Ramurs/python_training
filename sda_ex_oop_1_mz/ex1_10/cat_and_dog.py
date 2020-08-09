from sda_ex_oop_1_mz.ex1_10.cat import Cat
from sda_ex_oop_1_mz.ex1_10.dog import Dog

def animals_creator() -> list:
    animals = []
    animal1 = Cat("Cat1")
    animal2 = Cat("Cat2")
    animal3 = Dog("Dog1")
    animal4 = Dog("Dog2")
    animals.extend([animal1, animal2, animal3, animal4])
    return animals

def main():
    animals = animals_creator()
    for animal in animals:
        print(animal.make_sound())

if __name__ == "__main__":
    main()


