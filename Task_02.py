#2) Вводим с клавиатуры целое число X. Далее вводим Х целых чисел.
#Необходимо вывести на экран максимальное и второе максимальное число из введенных чисел.

x = int(input('Введите колличество чисел: '))

temp = 0
maximum_one = 0
maximum_two = 0
for i in range(x):
    number = int (input('Введите целое число: '))
    if number > maximum_one:
        maximum_two = maximum_one
        maximum_one = number
    
print(f'Первое максимальное число: {maximum_one}')
print(f'Второе максимальное число: {maximum_two}')

