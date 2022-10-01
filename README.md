# ComSciense-Labs

lab2 "Hamming code (7;4)"

Написать программу, получающую на вход из командной строки из 7 цифр «0» и «1», записанных подряд, а затем на основе классического кода Хэмминга (7,4) выдает правильное сообщение и указывает бит с ошибкой при его наличии.
<br />
<br />
<br />
<br />
lab3 "Smiles"

Основное задание<br />
Реализуйте программный продукт на языке Python, используя регулярные выражения по варианту, представленному в таблице.
Программа должна считать количество смайликов определённого вида (вид смайлика описан в таблице вариантов) в предложенном тексте. Все смайлики имеют такую структуру:
[глаза][нос][рот].
Вариантом является различные наборы глаз, носов и ртов.

![image](https://user-images.githubusercontent.com/76608743/191778447-395bb849-68c1-41eb-994a-2be77f261308.png)

Пример смайлика: 8<{P
4) * нарисовав смайлик по вашему варианту при помощи средств языка программирования Python, можно заработать дополнительные баллы.
<br />
<br />
<br />
Доп. задание №1 

Реализуйте программный продукт на языке Python, используя регулярные выражения по варианту, представленному в таблице.

Довольно распространённая ошибка ошибка – это повтор слова. Вот в предыдущем предложении такая допущена. Необходимо исправить каждый такой повтор.
Повтор это – слово, один или несколько пробельных символов, и снова то же слово.

Пример:
Ввод
Довольно распространённая ошибка ошибка – это лишний повтор повтор слова слова. Смешно, не не правда ли? Не нужно портить хор хоровод.

Вывод
Довольно распространённая ошибка – это лишний повтор слова. Смешно, не правда ли? Не нужно портить хор хоровод.
<br />
<br />
<br />
Доп. задание №2 <br />
Реализуйте программный продукт на языке Python, используя регулярные выражения по варианту, представленному в таблице.

Вывесили списки стипендиатов текущего семестра, которые представляют из себя список людей ФИО и номер группы этого человека. Вы решили подшутить над некоторыми из своих одногруппников и удалить их из списка.
С помощью регулярного выражения найдите всех студентов своей группы, у которых инициалы начинаются на одну и туже букву и исключите их из списка.

Пример (группа P000):
Ввод
Петров П.П. P000
Анищенко А.А. P33113
Примеров Е.В. P000
Иванов И.И. P000

Вывод
Анищенко А.А. P33113
Примеров Е.В. P000
