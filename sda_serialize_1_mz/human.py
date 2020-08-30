import json


class Human:
    def __init__(self, age: int, name: str, surname: str):
        self.age = age
        self.name = name
        self.surname = surname

    def __str__(self) -> str:
        return f'Name: {self.name}, Surname: {self.surname}, Age: {self.age}'

    def convert_to_dict(self):
        return self.__dict__

    @classmethod
    def convert_from_dict(cls, params: dict):
        name = params.get('name', '-')
        surname = params.get('surname', '-')
        age = params.get('age', 0)
        return cls(age, name, surname)

    @staticmethod
    def write_humans_to_file(humans: []):
        humans_serialized = []
        for human in humans:
            human_dict: dict = human.convert_to_dict()
            print(f'Human dict: {human_dict}')
            human_json: str = json.dumps(human_dict)
            print(f'Added {human_json}')
            humans_serialized.append(human_json)

        print(humans_serialized)
        try:
            with open('./human.json', 'w') as fd:
                json.dump(humans_serialized, fd)
        except(IOError, BaseException) as e:
            print(f'Error {e.args}')

    @staticmethod
    def read_humans_from_file() -> list:
        humans_serialized = []
        try:
            with open('./human.json', 'r') as fd:
                humans_serialized: list = json.load(fd)
        except(IOError, BaseException) as e:
            print(f'Error {e.args}')
        humans = []
        for human_str in humans_serialized:
            human_json: dict = json.loads(human_str)
            human = Human.convert_from_dict(human_json)
            humans.append(human)
        return humans


def main():
    hu1 = Human(28, 'Adam', 'Nowak')
    print(hu1)
    hu2 = Human(31, 'Zdzichu', 'Zdzichowy')
    humans = [hu1, hu2]
    Human.write_humans_to_file(humans)
    returned_humans = Human.read_humans_from_file()
    for returned_human in returned_humans:
        print(returned_human)


if __name__ == '__main__':
    main()
