class MyComplex:
    def __init__(self, real: int, unreal=0):
        self.real = real
        self.unreal = unreal

    def show(self):
        print(f'{self.real} + {self.unreal} i')

    def __str__(self):
        return f'{self.real} + {self.unreal} i'

    def is_equal_to(self, other_complex: 'MyComplex') -> bool:
        if self.real == other_complex.real and \
                self.unreal == other_complex.unreal:
            return True
        return False

    def __eq__(self, other) -> bool:
        if isinstance(other, MyComplex):
            if self.real == other.real and \
                    self.unreal == other.unreal:
                return True
        return False

    @classmethod
    def add_two_complex(cls, one: 'MyComplex', two: 'MyComplex'):
        return cls(one.real + two.real, one.unreal + two.unreal)

    @classmethod
    def add_three_complex(cls, one: 'MyComplex', two: 'MyComplex', three: 'MyComplex'):
        return cls(one.real + two.real + three.real, one.unreal + two.unreal + three.unreal)

    @classmethod
    def add_many_value(cls, complex_values: list) -> 'MyComplex':
        real = 0
        unreal = 0
        for value in complex_values:
            real += value.real
            unreal += value.unreal

        return cls(real, unreal)

    def add_to_this_complex(self, new_complex: 'MyComplex'):
        self.real += new_complex.real
        self.unreal += new_complex.unreal
        return self

    def add_to_this_complex_by_value(self, real: int, unreal: int):
        self.real += real
        self.unreal += unreal
        return self


def main():
    my_complex = MyComplex(1, 2)
    # my_complex.show()
    print(my_complex)

    other_complex = MyComplex(1, 2)
    # print(my_complex.is_equal_to(other_complex))
    # print(my_complex == other_complex)
    # new_complex = MyComplex.add_two_complex(my_complex, other_complex)
    # print(new_complex)

    # print(my_complex.add_to_this_complex(other_complex))
    # print(my_complex.add_to_this_complex_by_value(5, 5))

    print(MyComplex.add_three_complex(my_complex, other_complex, MyComplex(1, 1)))

    print(MyComplex.add_many_value([my_complex, other_complex, MyComplex(1, 1), MyComplex(2, 2)]))


if __name__ == "__main__":
    main()
