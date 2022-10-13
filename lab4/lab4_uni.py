from py_json_to_proto.convert import convert, Options
import re

convert_format = input('Введите формат нового файла: ')


def to_proto():
    with open('timetable.json', 'r', encoding='utf8') as file:
        data = convert(file.read(), Options(False, False))

    with open('timetable.proto', 'w') as file:
        file.write(str(data))


def to_wml():
    with open("timetable.json", 'r', encoding="utf8") as file:
        text = [i.strip() for i in file.read().split('\n')]
    count = 1
    tmp = []

    with open('timetable.wml', 'w', encoding='utf8') as file:
        file.write('<wml> \n')
        for i in range(1, len(text) - 1):
            if ': {' in text[i]:
                tag = re.search(r'"(\w*)":', text[i])[0][1:-2]
                tmp.append(text[i])
                file.write('     ' * count + f'<{tag}> \n')
                count += 1
            elif ':' in text[i]:
                tag = re.search(r'"(-\w*)":', text[i])[0][2:-2]
                info = re.search(r'": "([\S\s]*)"', text[i])[0][4:-1]

                file.write('     ' * count + f'<{tag}> {info} </{tag}> \n')
            elif '}' in text[i]:
                count -= 1
                tag = re.search(r'"(\w*)":', tmp.pop())[0][1:-2]
                file.write('     ' * count + f'</{tag}> \n')
        file.write('</wml>')


def to_tsv():
    with open("timetable.json", 'r', encoding="utf8") as file:
        text = [i.strip() for i in file.read().split('\n')]

    with open('timetable.tsv', 'w', encoding='utf8') as file:
        tags = []
        infos = []
        for i in range(1, len(text) - 1):
            if ': {' in text[i]:
                tag = re.search(r'"(\w*)":', text[i])[0][1:-2]
                file.write(f'{tag}\n')
            elif ':' in text[i]:
                tags.append(re.search(r'"(-\w*)":', text[i])[0][2:-2])
                infos.append(re.search(r'": "([\S\s]*)"', text[i])[0][4:-1])
            elif '}' in text[i]:
                for j in tags:
                    file.write(j + '    ')
                file.write('\n')
                for k in infos:
                    file.write(k + '    ')
                file.write('\n')


def to_csv():
    with open("timetable.json", 'r', encoding="utf8") as file:
        text = [i.strip() for i in file.read().split('\n')]

    with open('timetable.csv', 'w', encoding='utf8') as file:
        tags = []
        infos = []
        for i in range(1, len(text) - 1):
            if ': {' in text[i]:
                tag = re.search(r'"(\w*)":', text[i])[0][1:-2]
                file.write(f'{tag}\n')
            elif ':' in text[i]:
                tags.append(re.search(r'"(-\w*)":', text[i])[0][2:-2])
                infos.append(re.search(r'": "([\S\s]*)"', text[i])[0][4:-1])
            elif '}' in text[i]:
                for j in tags:
                    file.write(j + ',')
                file.write('\n')
                for k in infos:
                    file.write(k + ',')
                file.write('\n')


def to_yml():
    with open("timetable.json", 'r', encoding="utf8") as file:
        text = [i.strip() for i in file.read().split('\n')]
    count = 0

    with open('timetable.yml', 'w', encoding='utf8') as file:
        for i in range(1, len(text) - 1):
            if ': {' in text[i]:
                tag = re.search(r'"(\w*)":', text[i])[0][1:-2]
                file.write('     ' * count + f'{tag}: \n')
                count += 1
            elif ':' in text[i]:
                tag = re.search(r'"(-\w*)":', text[i])[0][2:-2]
                info = re.search(r'": "([\S\s]*)"', text[i])[0][4:-1]

                file.write('     ' * count + f'{tag}: {info} \n')


if convert_format == 'proto':
    to_proto()
elif convert_format == 'wml':
    to_wml()
elif convert_format == 'tsv':
    to_tsv()
elif convert_format == 'csv':
    to_csv()
elif convert_format == 'yml':
    to_yml()
