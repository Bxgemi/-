from random import *
digits='0123456789'
lowercase_letters='abcdefghijklmnopqrstuvwxyz'
uppercase_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation='!#$%&*+-=?@^_'
def generate_password():
    chars = ''
    n = int(input('Количество паролей для генерации:'))
    a = int(input('Длина одного пароля:'))
    digOn = input('Включать ли цифры 0123456789? (y/n)')
    ABCon = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
    abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
    chOn = input('Включать ли символы !#$%&*+-=?@^_? (y/n)')
    excOn = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)')
    if digOn == 'y':
        chars += digits
    if ABCon == 'y':
        chars += uppercase_letters
    if abcOn == 'y':
        chars += lowercase_letters
    if chOn == 'y':
        chars += punctuation
    if excOn == 'y':
        for c in 'il1Lo0O':
            chars = chars.replace(c, '')
    if not chars:
        print('Ошибка: не выбран ни один тип символов!')
        return
    print('\nСгенерированные пароли:')
    for i in range(n):
        password = ''.join(choice(chars) for _ in range(a))
        print(f'{i + 1}. {password}')

generate_password()
