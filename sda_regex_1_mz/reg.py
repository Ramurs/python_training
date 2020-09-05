import re


def reg_ex1():
    value = input('Write number ')
    expression ='[0-9]+'
    if re.match(expression,value):
        if int(value) % 2 == 0:
            print('Even number')
        else:
            print('Odd')
    else:
        print('Incorrect number')

def reg_ex2():
    postal_code = input('Write postal code ')
    expression = '[0-9]{2}\\-[0-9]{3}'
    if re.match(expression, postal_code):
        print('It is fine')
    else:
        print('It is not fine')

def main():
    # reg_ex1()
    reg_ex2()

if __name__ == '__main__':
    main()
