from random import choice

words = [
    'python', 'программа', 'компьютер', 'алгоритм',
    'функция', 'переменная', 'список', 'цикл',
    'строка', 'словарь', 'класс', 'модуль'
]

hangman_stages = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]

def get_display(word, guessed):
    return ' '.join(letter if letter in guessed else '_' for letter in word)

def is_won(word, guessed):
    return all(letter in guessed for letter in word)

def hangman():
    word = choice(words)
    guessed = []
    wrong = []
    attempts = 6

    print('Добро пожаловать в игру Виселица!')
    print('Угадайте слово. У вас 6 попыток.\n')

    while True:
        print(hangman_stages[len(wrong)])
        print(f'\nСлово: {get_display(word, guessed)}')
        print(f'Неверные буквы: {", ".join(wrong) if wrong else "-"}')
        print(f'Осталось попыток: {attempts - len(wrong)}\n')

        if is_won(word, guessed):
            print(f'Поздравляем! Вы угадали слово: {word}')
            break

        if len(wrong) >= attempts:
            print(f'Вы проиграли! Загаданное слово было: {word}')
            break

        letter = input('Введите букву: ').lower().strip()

        if len(letter) != 1 or not letter.isalpha():
            print('Введите одну букву!')
            continue

        if letter in guessed or letter in wrong:
            print('Эту букву вы уже вводили!')
            continue

        if letter in word:
            guessed.append(letter)
            print(f'Буква "{letter}" есть в слове!')
        else:
            wrong.append(letter)
            print(f'Буквы "{letter}" нет в слове!')

    again = input('\nСыграть ещё раз? (да/нет): ')
    if again.lower() == 'да':
        hangman()
    else:
        print('Спасибо за игру!')

hangman()
