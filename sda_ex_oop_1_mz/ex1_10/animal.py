from abc import abstractclassmethod, ABC

class Animal(ABC):

    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name
