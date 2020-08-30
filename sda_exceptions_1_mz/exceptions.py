# ex1
def ex1():
    nums = [1, 2, 3, 4, 5]

    # Pierwszy sposób
    # try:
    #     print(nums[5])
    # except IndexError as ie:
    #     print(f'Index exceptions info: {ie.args}')
    # except BaseException as be:
    #     print(f'Base Exception info: {be.args}')

    # Drugi sposób
    try:
        print(nums[5])
    except (IndexError, BaseException) as e:
        print(f'Index Exception cached info: {e.args} ')


# ex2
def ex2(name: str):
    try:
        if not name:
            raise ValueError("Empty string")
        print(f'Value: {name}')
    except ValueError as e:
        print(f'Empty string, more info {e.args}')


# ex3
def ex3(value1: int, value2: int):
    result = 0
    try:
        result = value1 / value2
    except ZeroDivisionError as e:
        print(f'Zero Division Error, more info: {e.args}')
    return result


# ex4
def ex4(my_dict: dict):
    key = "items"
    try:
        items = my_dict[key]
        for item in items:
            print(item)
    except KeyError as e:
        print(f'Key Error, more info: {e.args}')


def ex4_v2(my_dict: dict):
    key = "items"
    items = my_dict.get(key, [])
    for item in items:
        print(item)


# ex5
class OrderItemError(ValueError):
    pass


class OrderItem:
    def is_correct(self):
        raise OrderItemError("Zamówienie niepoprawne")


# ex6
def ex6():
    raise NotImplementedError()


# ex7
def ex7():
    fd = None
    try:
        fd = open("test.txt")
    except IOError as e:
        print(f"Exception cached while opening file, more info {e.args}")
    finally:
        if fd:
            fd.close()
def ex7_v2():
    try:
        with open("test.txt") as fd:
            print("File opened")
    except IOError as e:
        print(f"Exception cached while opening file, more info {e.args}")


def main():
    # ex1
    ex1()

    # ex2
    ex2("")
    ex2("mk")

    # ex3
    ex3(10, 0)
    ex3(10, 2)

    # ex4
    ex4({"Other": ["radio", "camera"]})
    ex4({"devices": ["camera", "radio"]})
    ex4_v2({"items": ["camera", "radio"]})
    ex4_v2({"devices": ["camera", "radio"]})

    # ex5
    order_item = OrderItem()
    try:
        order_item.is_correct()
    except (OrderItemError, Exception) as oie:
        print(f'Złapany mój błąd {oie.args}')

    #ex7
    ex7()
    ex7_v2()

if __name__ == "__main__":
    main()
