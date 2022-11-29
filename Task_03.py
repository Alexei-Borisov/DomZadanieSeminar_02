#3) Вводим с клавиатуры целое число - это зарплата.
#Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
#И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 3 рублевых и 1 рублевых

salary = int(input('Введите целое число - это зарплата: '))
sum_banknots = 0

while salary > 0:
    if salary >= 25:
        print(f'Купюры по 25 рублей: {salary // 25} штук')
        sum_banknots += salary // 25
        salary %= 25
    elif salary >= 10:
        print(f'Купюры по 10 рублей: {salary // 10} штук')
        sum_banknots += salary // 10
        salary %= 10
    elif salary >= 3:
        print(f'Купюры по 3 рубля: {salary // 3} штук')
        sum_banknots += salary // 3
        salary %= 3
    else:
        print(f'Купюры по 1 рублю: {salary // 1} штук')
        sum_banknots += salary // 1
        salary %= 1

print('Общее минимальное количество купюр = ', sum_banknots)


