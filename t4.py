# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

num = input('Введите номер четверти координатной плоскости: ')
if num == '1':
    print(f'В {num} четверти x > 0, y > 0')
elif num == '2':
    print(f'В {num} четверти x < 0, y > 0')
elif num == '3':
    print(f'В {num} четверти x < 0, y < 0')
elif num == '4':
    print(f'В {num} четверти x > 0, y < 0')
else:
    print('Введите число от 1 до 4')
