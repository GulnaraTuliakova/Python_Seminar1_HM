# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

# Пример:


# - 6 -> да
# - 7 -> да
# - 1 -> нет

a = int(input('Введите номер дня недели: '))
if a >= 1 and a <= 5:
    print(f'{a}  день недели -  не выходной ')
elif a == 6 or a == 7:
    print(f'{a}  день недели - выходной ')
else:
    print('Введите число от 1 до 7')
