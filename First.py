import math
while True:   
    print(' \n Добро пожаловать в калькулятор')
    print('Вот несколько команд, которые я знаю: ')
    print('1. Сложить')
    print('2. Вычесть')
    print('3. Умножить')
    print('4. Разделить')
    print('5. Возвести в степень')
    print('6. Извлечь квадратный корень')
    print('7. Факториал числа')
    print('8. Косинус угла')
    print('9. Синус угла')
    print('10. Тангенс угла')
    print('0. Выход')
    try: 
        caseID = int(input('Введите команду '))
        if(caseID <11 and caseID > -1):
            if caseID in [6,7]: 
                one = float (input('Введите число '))
            if caseID in [8,9,10]: 
                one = float(input('Введите угол в градусах '))
            if caseID == 0: 
                break 
            else:
                one = float (input('\n Введите первое число '))
                two = float (input('Введите второе число ')) 
        else:
            print('Вы можете вводить команды только от 0 до 10')
            break
        if caseID == 1: 
            result = one + two
        if caseID == 2 : 
            result = one - two
        if caseID == 3 : 
            result = one*two
        if caseID == 4 : 
            result = one/two 
        if caseID == 5 : 
            result = one**two
        if caseID == 6 : 
            result = math.isqrt(one)
        if caseID == 7 : 
            result = math.factorial(one)
        if caseID == 8 : 
            result = math.sin(one)
        if caseID == 9 : 
            result = math.cos(one)
        if caseID == 10 : 
            result = math.tan(one)
        print('\n Результат: ', result)
    except ValueError: print('\n Вы допустили ошибку, попробуйте снова')
    except ZeroDivisionError: print('\n На ноль делить нельзя')


