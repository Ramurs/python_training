import json


def write_json_file():
    input_json = [
        {'imie': 'Antek'},
        {'imie': 'Marek'}
    ]
    try:
        with open("./text.json", "w") as file_descriptor:
            json.dump(input_json, file_descriptor)

    except (IOError, BaseException) as e:
        print(f"Masz blad i wiecej info {e.args}")


def read_json_file():
    output_json = []
    try:
        with open("./text.json", "r") as file_descriptor:
            output_json = json.load(file_descriptor)
            print(output_json)
    except (IOError, json.JSONDecodeError, BaseException) as e:
        print(f"Masz blad i wiecej info {e.args}")


def main():
    write_json_file()
    read_json_file()

if __name__ == "__main__":
    main()
