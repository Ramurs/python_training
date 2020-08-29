class Complex:
    def __init__(self, real: int, unreal=0):
        self._real = real
        self._unreal = unreal

    @@property
    def real(self):
        return real

    @real.setter
    def real(self, value):
        self._real = value


    @property
    def unreal(self):
        return unreal


    @unreal.setter
    def unreal(self, value):
        self._unreal = value

    def show(self):
        print(f'{self._real} + {self._unreal} * i')

    def __str__(self)->str:
        print(f'{self._real} + {self._unreal} * i')

    def is_equal_to (self, real:int, unreal:int)->bool:
        if self._real == real and self._unreal == unreal:
            return True
        else:
            return False

    def __eq__ (self, real:int, unreal:int)->bool:
        if self._real == real and self._unreal == unreal:
            return True
        else:
            return False

    def add_two_complex(self):

