from random import *
def uqadaika():
    print('Добро пожаловать в числовую угадайку')
    count = 0
    while True:
        n = randint(1, 100)

        while True:
            b = int(input('Напишите число [1,100]: '))

            if b < 1 or b > 100:
                print('А может быть все-таки введем целое число от 1 до 100?')
                continue

            if b < n:
                count += 1
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif b > n:
                count += 1
                print('Ваше число больше загаданного, попробуйте еще разок')
            elif b == n:
                count += 1
                print('Вы угадали, поздравляем!')
                print('Число попыток:', count)
                break

        snova = input('Хотите сыграть еще раз? (да/нет): ')
        if snova.lower() != 'да':
            print('Спасибо, что играли! Еще увидимся...')
            break


uqadaika()
