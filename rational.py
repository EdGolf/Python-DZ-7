import rational as op
import sys

def x():
    firstnum = float(input('Выберите первое число c запятой: ').replace(',', '.'))
    return firstnum

def y():
    secondnum = float(input('Выберите второе число с запятой: ').replace(',', '.'))
    return secondnum

def selectoperation():
    global operation
    operation = (input(f'Выберите операцию: +, -, *, /: '))
    if operation == '+' or '-' or '/' or '*':
        return operation
    else:
        print('Invalid syntax')

def res(firstnum, secondnum):
    if  operation == '+':
        res = firstnum + secondnum
        result = round(res, 3)
        return result
    elif operation == '-':
        res = firstnum - secondnum
        result = round(res, 3)
        return result
    elif operation == '*':
        res = firstnum * secondnum
        result = round(res, 3)
        return result
    elif operation == '/':
        res = firstnum / secondnum
        result = round(res, 3)
        return result
    else:
        print('invalid syntax')

def mainterminal():
    global file
    x = op.x()
    while True:
        y = op.y()
        oper = op.selectoperation()
        res = op.res(x, y)
        file = 'results.txt'
        with open('results.txt', 'a') as data:
            data.write(f'The result of {x} {oper} {y} = {res}\n')
        print(f'Результат {x} {oper} {y} = {res}\n(already written to txt file)' )
        again = input('Вы хотите рассчитать другие числа? Да/Нет: ').lower()
        if again == 'Да':
            useresult = input('Вы хотите использовать результат последней операции? (Да/Нет): ').lower()
            if useresult == 'Да':
                x = res
                continue
            elif useresult == 'Нет':
                break
            else:
                sys.exit()           
        else:   
            sys.exit()