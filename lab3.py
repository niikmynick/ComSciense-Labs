import re


def find_smile(text):
    book = {}
    eyes_part = re.findall(r'[:;X8=]', text)
    nose_part = re.findall(r'(?:-{)|(?:<{)|(?:-)|(?:<)', text)
    mouth_part = re.findall(r'[)(O|\\/P]', text)
    for i in range(len(eyes_part)):
        smile = eyes_part[i] + nose_part[i] + mouth_part[i]
        if smile in book.keys():
            book[smile] += 1
        else:
            book[smile] = 1
    for key, item in book.items():
        print(key, f'повторятся {item} раз(а)')


def eyes(num):
    temp = num % 5
    types = [':', ';', 'X', '8', '=']
    return types[temp]


def nose(num):
    temp = num % 4
    types = ['-', '<', '-{', '<{']
    return types[temp]


def mouth(num):
    temp = num % 7
    types = ['(', ')', 'O', '|', '\\', '/', 'P']
    return types[temp]


def print_smile(isu):
    print(f'{eyes(isu)}{nose(isu)}{mouth(isu)}')


def delete_repeated_word():
    text = input()
    string = r'\b(\w+) (\1)\b'
    print(re.sub(string, r'\1', text, flags=re.I))


def del_students():
    text = []
    while True:
        s = input()
        if s:
            text.append(s)
        else:
            break
    string = r'(\w+ (\w\.)(\2) P000)'
    for i in text:
        print(re.sub(string, ' ', i))


task_num = input('Проверка задания [def / add1 / add2] ')

if task_num == 'def':
    find_smile(input('Введите текст:'))
    print_smile(int(input('Введите свой номер ИСУ: ')))

elif task_num == 'add1':
    delete_repeated_word()

elif task_num == 'add2':
    del_students()

else:
    print('Такого задания нет')
