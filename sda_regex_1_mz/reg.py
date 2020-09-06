import re


def reg_ex1():
    value = input("write number >>> ")
    expression = '[0-9]+'
    if re.match(expression, value):
        if int(value) % 2 == 0:
            print('even number')
        else:
            print('odd')
    else:
        print("Incorrect number")


def reg_ex2():
    post_code = input("post code >>> ")
    expression = '[0-9]{2}\\-[0-9]{3}'
    if re.match(expression, post_code):
        print("It's fine")
    else:
        print("it's not fine :D")


def reg_ex3():
    login = input("Login: ")
    # right_login = r'[[A-Z]+[a-z]+[0-9]]+{8,16}'
    if re.match(r'[A-Za-z0-9]{8,16}', login):
        print("Congrats! Good login!")
        print(len(login))
    else:
        print("Find out better login")
        print(len(login))


def reg_ex4():
    write_for_ala = input("Write, please: ")
    # print(re.match(r"[\S\s]ala", write_for_ala))
    if re.match(r'.*ala.*', write_for_ala):
        print("Congrats! Good login!")
        print(len(write_for_ala))
    else:
        print("Find out better login")
        print(len(write_for_ala))


def reg_ex5():
    write_string = input("Write something, please: ")
    if re.match(r'([0-9]{2}\.){2}[0-9]{4}r\.', write_string):
        print("data is correct")
    else:
        print("data is incorrect")


# VSD43281fA.
def reg_ex6():
    write_string = input("Write something, please: ")
    if re.match(r'[A-Z]{3}[0-9]{5}[a-z]{1}[A-Z]{1}', write_string):
        print('Log in')
    else:
        print("Wrong pass")


# Numer seryjny oprogramowania ma postać "CFG&Y-TYH67-GH56T-UIO99-RY4RT",
# gdzie każdy blok może składać się z dużych liter lub cyfr. Bloki oddzielone są
# myślnikami "-". W numerze występuje dokładnie 5 bloków z wartościami. Przygotuj
# wyrażenie regularne sprawdzające numer seryjny
def reg_ex7():
    number = input("Write Number: ")
    # expression = '([A-Z0-9!@#\\$%\\^&\\*]{5}\\-){4}[A-Z0-9!@#\\$%\\^&\\*]'
    # ([A-Z0-9&]{5}\\-){4}[A-Z0-9&]{5}
    if re.match('([A-Z0-9!@#\\$%\\^&\\*]{5}\\-){4}[A-Z0-9!@#\\$%\\^&\\*]{5}', number):
        print('Log in')
    else:
        print("Wrong pass")


def reg_ex8():
    fva = input("Write FV no: ")
    if re.match(r'FV/1[0-9]{3}/[0-9]{2}/[0-9]{4}', fva):
        print('Good fv no')
    else:
        print("Wrong fv no")


# Do testów użyj podanego zdania:
# "Drogi Marszałku, Wysoka Izbo. PKB rośnie. Z pełną odpowiedzialnością mogę stwierdzić iż realizacja określonych zadań stanowionych przez organizację. Dalszy rozwój jest ważne zadanie w większym stopniu tworzenie odpowiednich warunków aktywizacji. Często niezauważanym szczegółem jest to, że zakres i rozwijanie struktur pociąga za najważniejszy punkt naszych działań obierzemy praktykę, nie zaś teorię, okazuje się jasne."
def reg_ex9():
    text = input("Your text")
    regex = ' '
    result = re.split(regex, text)
    print(result)
    print(f"ilość słów: {len(result)}")
    print(f"ilość znaków: {len(text)}")
    longest_word = ''
    shortest_word = result[0]
    sum_of_chars = 0
    for word in result:
        if len(longest_word) < len(word):
            longest_word = word
        if len(shortest_word) > len(word):
            shortest_word = word
        sum_of_chars += len(word)
    print(f"najdłuższe słowo: {longest_word}")
    print(f"najkrótsze słowo: {shortest_word}")
    average = sum_of_chars / len(result)
    print(f"średnia słowa: {average}")


# Drogi Marszałku, Wysoka Izbo. PKB rośnie. Z pełną odpowiedzialnością mogę stwierdzić iż realizacja określonych zadań stanowionych przez organizację. Dalszy rozwój jest ważne zadanie w większym stopniu tworzenie odpowiednich warunków aktywizacji. Często niezauważanym szczegółem jest to, że zakres i rozwijanie struktur pociąga za najważniejszy punkt naszych działań obierzemy praktykę, nie zaś teorię, okazuje się jasne.
def main():
    reg_ex9()
    # reg_ex7()
    # reg_ex6()
    # reg_ex1()
    # reg_ex2()
    # reg_ex3()
    # reg_ex4()
    # reg_ex5()


if __name__ == "__main__":
    main()
