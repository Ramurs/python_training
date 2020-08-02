class Cat:
    def __init__(self, name: str):
        self.name = name

    def make_sound(self) -> str:
        return f'{self.name} miau'

    def eat_mouse(self) -> None:
        self.eat_mouse += 1
        print(f'{self.name} zjadł {self.eat} myszy')

