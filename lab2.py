msg = [int(i) for i in list(input())]
print('Полученное сообщение:', *msg)

errors = []

first_control = sum([msg[i] for i in range(2, 7, 2)])
second_control = msg[2] + msg[5] + msg[6]
third_control = sum([msg[i] for i in range(4, 7)])

if first_control % 2 != int(msg[0]):
    errors.append(1)
if second_control % 2 != int(msg[1]):
    errors.append(2)
if third_control % 2 != int(msg[3]):
    errors.append(3)

error_ind = sum(errors) - 1
msg[error_ind] = abs(msg[error_ind] - 1)

print(f'Ошибка в бите {error_ind + 1}' if error_ind > 0 else 'Ошибок в полученном сообщении нет')
print('Исправленное сообщение:', *msg)
# print(f"В десятичной записи: {int(''.join(map(str, msg)), 2)}")
