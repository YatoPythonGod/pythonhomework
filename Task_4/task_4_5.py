# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст
from task_4_4 import greate_file, read_file


def run_length_encoding(text: str):
    """RLE encoding str"""
    result = []
    a = None
    count = 1
    for i in text + chr(ord(text[-1]) + 1):
        if i == a:
            count += 1
        else:
            if count > 1:
                result.append(f'{count}{a}')
            else:
                result.append(a)
            count = 1
        a = i
    result.append(a)

    return ''.join(result[1:-1])


def decode_rle(text: str):
    """RLE decode str"""
    count = ''
    result = ''
    for i in text:
        if i.isdigit():
            count += i
        else:
            if count:
                result += int(count) * i
                count = ''
            else:
                result += i
    return result


if __name__ == '__main__':
    rle_text = run_length_encoding('AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool')
    print(rle_text)
    greate_file('task_4_5.txt', rle_text)
    print(decode_rle(read_file('task_4_5.txt')))

