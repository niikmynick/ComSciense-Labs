import time

start_time = time.time()

with open("timetable.json", 'r', encoding="utf8") as file:
    text = [i.strip() for i in file.read().split('\n')]
count = 0
tmp = []

with open('timetable.xml', 'w', encoding='utf8') as file:
    for i in range(1, len(text) - 1):

        if ': {' in text[i]:
            file.write('     '*count + text[i].replace('":', '>').replace('"', '<').replace('{', '') + '\n')
            tmp.append(text[i])
            count += 1
        elif ':' in text[i]:
            file.write('     '*count + text[i].replace('"-', '<').replace('":', '>').replace('",', '').replace('"', ''))
            s = text[i].replace('"-', '</').replace('":', '>')
            file.write(s[:s.rindex('>') + 1] + '\n')
        elif '}' in text[i]:
            count -= 1
            file.write('     ' * count + tmp.pop().replace('":', '>').replace('"', '</').replace('{', '') + '\n')

print('%s seconds' % (time.time() - start_time))
