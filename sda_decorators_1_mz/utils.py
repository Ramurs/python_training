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
        #   def wrapper():
        print('before')
        print(f'args = {args}')
        print(f'kwargs = {kwargs}')
        result = func(*args, **kwargs)
        #       result = func()
        print(' after')
        return result

    return wrapper


# @simply_wrapper
@my_wrapper
def say_hello(a, b):
    print('hello world!')
    print(f" a value ={a}")
    print(f" b value = {b}")


def main():
    say_hello(a=1, b=2)


if __name__ == '__main__':
    main()
