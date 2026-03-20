def caesar_encrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
                if char.isupper():
                    result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                else:
                    result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя':
                russian_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
                russian_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
                if char.isupper():
                    idx = russian_upper.index(char)
                    result += russian_upper[(idx + shift) % 32]
                else:
                    idx = russian_lower.index(char)
                    result += russian_lower[(idx + shift) % 32]
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


mode  = input('Режим (1 — шифрлау, 2 — дешифрлау): ')
text  = input('Мәтін енгізіңіз: ')
shift = int(input('Жылжу мөлшері (1-31): '))

if mode == '1':
    print(f'Нәтиже: {caesar_encrypt(text, shift)}')
elif mode == '2':
    print(f'Нәтиже: {caesar_decrypt(text, shift)}')
else:
    print('Қате: 1 немесе 2 енгізіңіз')
