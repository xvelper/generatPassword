import random

# Набор доступных символов
ARRAY_SYMBOLS = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'a', 'b', 'c',
    'A', 'B', 'C',
    '!', '@']

# Получаем количество символов в пароле.
CONST_COUNT_SYMBOLS = 4
custom_count_symbols = int(input('Введите кол-во символов в пароле: '))
if custom_count_symbols > 0:
    count_symbols = custom_count_symbols
else:
    count_symbols = CONST_COUNT_SYMBOLS

count_variant = len(ARRAY_SYMBOLS) ** count_symbols


# Функция случайных символом
def random_symbols():
    return ARRAY_SYMBOLS[
        random.randint(0, len(ARRAY_SYMBOLS) - 1)
    ]

print(f'Кол-во доступных символов: {len(ARRAY_SYMBOLS)}')
print(f'Кол-во возможных вариантов: {count_variant}')
print(ARRAY_SYMBOLS[random.randint(0, len(ARRAY_SYMBOLS) - 1)])


# Массив  символов
password_array = [i for i in range(0, count_symbols)]


password = ''

for i in password_array:
    password = password + f'{random_symbols()}'

print(f'Сгенерированный пароль: {password}')

with open('password.txt', 'a') as password_string:
    password_string.write('{}\n'.format(f'{password}'))
