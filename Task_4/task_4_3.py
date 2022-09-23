# В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Пример:
# Волков Андрей 5
# Наталья Тарасова 5
# Фредди Меркури 3
# Денис Байцуров 4
#
# Программа выдаст:
# ВОЛКОВ АНДРЕЙ 5
# НАТАЛЬЯ ТАРАСОВА 5
# Фредди Меркури 3
# Денис Байцуров 4

from statistics import mean

with open('journal.txt', 'w', encoding='utf-8') as f:
    f.write('''Волков Андрей 5,4,5,5,5
Наталья Тарасова 5,3,4,5,4
Фредди Меркури 3,2,3,3,4,4
Денис Байцуров 4,2,3,4,5,2
''')


def check_journal(score: int, file='journal.txt'):
    """converts student names to uppercase if the average score is higher than the specified function"""
    with open(file, encoding='utf-8') as f1:
        result_dict = {line.rsplit(' ', 1)[0]: line.strip().rsplit(' ', 1)[1].split(',') for line in f1}
        with open(file, 'w', encoding='utf-8') as f2:
            for k, v in result_dict.items():
                if mean(list(map(int, v))) > score:
                    f2.write(f'{k.upper()} {",".join(v)}\n')
                else:
                    f2.write(f'{k} {",".join(v)}\n')


check_journal(4)
