# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо.
# При расшифровке происходит обратная операция. К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо.
# "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст,
# а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

def encrypt(text: str, key=5):
    """encrypt str"""
    encrypted_list = [chr(ord(letter) + key) for letter in text]
    return ''.join(encrypted_list)


def decoding(text: str, key=5):
    """decoding str"""
    decoding_list = [chr(ord(letter) - key) for letter in text]
    return ''.join(decoding_list)


def greate_file(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(content)


def read_file(file_name):
    with open(file_name, encoding='utf-8') as f:
        return f.read()


if __name__ == '__main__':
    greate_file('encrypt_text.txt', encrypt('Moscow never sleep'))
    print(read_file('encrypt_text.txt'))
    print(decoding(read_file('encrypt_text.txt')))
    
