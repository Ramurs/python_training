from contextlib import contextmanager


@contextmanager
def open_file(path: str):
    print("opening file")
    fd = open(path, 'a')
    yield fd
    fd.close()
    print("closing file")


class OpenFileManager:
    def __init__(self, path=''):
        self.__source = path

    @property
    def source(self) -> str:
        return self.__source

    def __enter__(self):
        print('Opeining file')
        self.__file_descriptor = open(self.__source, 'a')
        return self.__file_descriptor

    def __exit__(self, *args):
        self.__file_descriptor.close()
        print('Closing file')


def main():
    # try:
    #     with open_file(path='./test_writtingfle') as fd:
    #         fd.write('ala ma kota')
    # except IOError as e:
    #     print(f" IOError found -more {e.args}")

    try:
        with OpenFileManager(path='./test_writtingfle') as fd:
            fd.write('ala ma kota')
            print('Zaraz konczy sie with')
    except IOError as e:
        print(f" IOError found -more {e.args}")


if __name__ == "__main__":
    main()
