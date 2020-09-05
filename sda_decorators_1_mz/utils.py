def simply_wrapper(func):
    def wrapper():
        print('before')
        result = func()
        print('after')
        return result

    return wrapper


def very_simply_wrapper(func):
    def wrapper():
        print('before')
        return func()

    return wrapper


def my_wrapper(func):
    def wrapper(*args, **kwargs):
        print("before")
        print(f'args = {args}')
        print(f'kwargs = {kwargs}')
        result = func(*args, **kwargs)
        print('after')
        return result

    return wrapper()


# @simply_wrapper
@my_wrapper
def say_hello(a=7, b=3):
    print("Hell World!")
    print(f'a value = {a}')
    print(f'b value = {b}')


def main():
    say_hello(1, 2)


if __name__ == "__main__":
    main()
