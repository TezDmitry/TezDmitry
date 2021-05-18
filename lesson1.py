print('задание 1.')
a = 'Дмитрий'
b = 32
print(a, b)
c = int(input('Напишите число: '))
d = input('Как у вас дела? ')
print(c, d)


print('задание 2.')
time = int(input('Введите время в секундах: '))
hours = time // 3600
minute = (time - hours * 3600) // 60
second = time - (hours * 3600) - (minute * 60)
print(f'Время в формате чч:мм:сс - {hours:02d}:{minute:02d}:{second:02d}')


print('задание 3.')
n = input('Введите число: ')
result = int(n) + int(n * 2) + int(n * 3)
print(int(result))


print('задание 4.')
number = int(input('Введите целое положительное число: '))
more_number = 0
while number != 0:
    digit = number % 10
    if digit > more_number:
        more_number = digit
    number = number // 10
print(more_number)

print('задание 5.')
profit = int(input('Введите значение выручки фирмы: '))
costs = int(input('Введите значение издержек фирмы: '))
if profit > costs:
    print(f'Фирма работает в прибыль, рентабельность выручки равна {(profit / costs):.2f}')
    person = int(input('Введите количество работников фирмы: '))
    profit_person = (profit - costs) / person
    print(f'Прибыль фирмы на одного сотрудника составляет {profit_person}')
else:
    print('Фирма работает в убыток')


print('задание 6.')
a = int(input('Введите кол-во киллометров в первый день: '))
b = int(input('Конечный результат в км: '))
day = 1
while a < b:
    a = a + a * 0.1
    day += 1
print(f'На {day}-й день спортсмен достиг результата — не менее {b} км.')