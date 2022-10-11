import re
import time

start_time = time.time()

with open("timetable.json", 'r', encoding="utf8") as file:
    text = [i.strip() for i in file.read().split('\n')]
count = 0
tmp = []

with open('timetable_regexp.xml', 'w', encoding='utf8') as file:
    for i in range(1, len(text) - 1):
        if ': {' in text[i]:
            tag = re.search(r'"(\w*)":', text[i])[0][1:-2]
            tmp.append(text[i])
            count += 1
            file.write('     '*count + f'<{tag}> \n')
        elif ':' in text[i]:
            tag = re.search(r'"(-\w*)":', text[i])[0][2:-2]
            info = re.search(r'": "([\S\s]*)"', text[i])[0][4:-1]

            file.write('     '*count + f'<{tag}> {info} </{tag}> \n')
        elif '}' in text[i]:
            count -= 1
            tag = re.search(r'"(\w*)":', tmp.pop())[0][1:-2]
            file.write('     '*count + f'</{tag}> \n')

print('%s seconds' % (time.time() - start_time))
