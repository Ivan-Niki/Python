
# 1. Счастливая последовательность 1
""" В популярном сериале «Остаться в живых» использовалась последовательность чисел 4 8 15 16 23 42, 
которая принесла героям удачу и помогла сорвать джекпот в лотерее. 
Напишите программу, которая выводит данную последовательность чисел с одним пробелом между ними. """
print(4, 8, 15, 16, 23, 42)

# 2. Счастливая последовательность 2
""" Измените предыдущую программу так, чтобы каждое число последовательности 4 8 15 16 23 424 8 15 16 23 42 
печаталось на отдельной строке.
Примечание. Каждая последующая команда print() выводит указанный текст, начиная с новой строки. """
print(4)
print(8)
print(15)
print(16)
print(23)
print(42)

# 3. Звездный треугольник
""" Напишите программу, которая выводит указанный треугольник, состоящий из звездочек (*).
Sample Output:
*
**
***
****
*****
******
*******                                                              """

print("*")
print("**")
print("***")
print("****")
print("*****")
print("******")
print("*******")

# 4. Приветствие
""" На вход программе подается строка текста – имя человека. 
Напишите программу, которая принимает эту строку текста через стандартный поток ввода. 
Далее программа должна выводить на экран приветствие в виде слова «Привет» (без кавычек), после которого 
должна стоять запятая и пробел, а затем – введенное имя. """
name = input()
print("Привет,", name)

# 5. Любимая команда
""" На вход программе подается строка текста – название футбольной команды. 
Напишите программу, которая принимает через стандартный поток ввода эту строку и печатает ее на экране 
со словами « - чемпион!» (без кавычек). """
team = input()
print(team, '- чемпион!')

# 6. Повторяй за мной
""" Напишите программу, которая считывает три строки по очереди, а затем выводит их в той же 
последовательности, каждую на отдельной строчке. """
first_word = input()
second_word = input()
third_word = input()
print(first_word)
print(second_word)
print(third_word)

# 7. Что будет выведено на экран в результате выполнения следующего кода?
print('31', '12', '2019', sep='-')
# Ответ: 31-12-2019

# 8. Что будет выведено на экран в результате выполнения следующего кода?
print('Mercury', 'Venus', sep='*', end='!')
print('Mars', 'Jupiter', sep='**', end='?')
# Ответ: Mercury*Venus!Mars**Jupiter?

# 9. Сколько строк будет распечатано в результате выполнения следующего кода?
print('a', 'b', 'c', sep='*')
print('d', 'e', 'f', sep='**', end='')
print('g', 'h', 'i', sep='+', end='%')
print('j', 'k', 'l', sep='-', end='\n')
print('m', 'n', 'o', sep='/', end='!')
print('p', 'q', 'r', sep='1', end='%')
print('s', 't', 'u', sep='&', end='\n')
print('v', 'w', 'x', sep='%')
print('y', 'z', sep='/', end='!')
# Ответ: 5

# 10. Кастомный разделитель
""" Напишите программу, которая считывает строку-разделитель и три строки, а затем 
выводит указанные строки через разделитель. """
separator = input()
word1 = input()
word2 = input()
word3 = input()
print(word1, word2, word3, sep=separator)

# 11. Что будет напечатано в результате выполнения следующей программы?
""" 
# print('Java')
# print('Ruby')
# print('Scala')
print('Python', end='+')  # print('C++')
# print('GO')
print('C#', end='=')  # print('C')
print('awesome')
# finish
""" 
# Ответ: Python+C#=awesome

# 12. Три последовательных числа
""" Напишите программу вывода на экран трех последовательно идущих чисел, каждое на отдельной строке. 
Первое число вводит пользователь, остальные числа вы должны сами вычислять в программе. """
num1 = int(input())
print(num1)
print(num1 + 1)
print(num1 + 2)

# 13. Три последовательных числа
""" Напишите программу вывода на экран трех последовательно идущих чисел, каждое на отдельной строке. 
Первое число вводит пользователь, остальные числа вы должны сами вычислять в программе. """
num1 = int(input())
num2 = int(input())
num3 = int(input())
print(num1 + num2 + num3)

# 14. Куб
# Напишите программу, вычисляющую объем куба и площадь его полной поверхности по введенному значению длины ребра.
length1 = int(input())
volume = length1 * length1 * length1
s = 6 * length1 * length1
print('Объем =', volume)
print('Площадь полной поверхности =', s)

# 15. Значение функции
# Напишите программу вычисления значения функции f(a, b) = 3(a+b)3+275b2− 127a−41 по введенным целым значениям a и b.
a = int(input())
b = int(input())
result = 3 * ((a + b) * (a + b) * (a + b)) + 275 * b * b - 127 * a - 41
print(result)

# 16. Следующее и предыдущее
""" Напишите программу, которая считывает целое число, после чего на экран выводится 
следующее и предыдущее целое число с пояснительным текстом. """
num = int(input())
print('Следующее за числом', num, 'число:', num + 1)
print('Для числа', num, 'предыдущее число:', num - 1)

# 17. Стоимость покупки
""" Напишите программу, которая считает стоимость трех компьютеров, состоящих из монитора, 
системного блока, клавиатуры и мыши. """
monitor_price = int(input())
s_block_price = int(input())
keyboard_price = int(input())
mouse_price = int(input())
print((monitor_price + s_block_price + keyboard_price + mouse_price) * 3)

# 18. Напишите программу, в которой вычисляется сумма, разность и произведение двух целых чисел, введенных с клавиатуры.
num1 = int(input())
num2 = int(input())
print(num1, '+', num2, '=', num1 + num2)
print(num1, '-', num2, '=', num1 - num2)
print(num1, '*', num2, '=', num1 * num2)

# 19. Арифметическая прогрессия
""" Арифметической прогрессией называется последовательность чисел  a1,a2,...,an, каждое из которых, 
начиная с a2, получается из предыдущего путем прибавления к нему одного и того же постоянного числа d (разность прогрессии). 
Например, арифметической прогрессией является следующая последовательность:
−6,−3,0,3,6,9,12−6,−3,0,3,6,9,12
Если известен первый член прогрессии (a1) и её разность (d), то n-ый член арифметической прогрессии 
находится по формуле:  an = a1 + d(n−1)
Входные данные:
-> На вход программе подаётся три целых числа: a1, d и n, каждое на отдельной строке.
Выходные данные:
-> Программа должна вывести n-ый член арифметической прогрессии. """
a1 = int(input())
d = int(input())
n = int(input())
result = a1 + d * (n - 1)
print(result)

# 20. Разделяй и властвуй
""" Напишите программу, которая считывает целое положительное число x и выводит на экран 
последовательность чисел x,2x,3x,4x и 5x, разделённых тремя черточками. """
num = int(input())
print(num, num*2, num*3, num*4, num*5, sep='---')

# 21. Геометрическая прогрессия
""" Геометрической прогрессией называется последовательность чисел b1,b2,…,bn, каждое из которых, начиная 
с b2, получается из предыдущего умножением на одно и то же постоянное число q (знаменатель прогрессии).
Если известен первый член прогрессии и ее знаменатель, то n-ый член геометрической прогрессии находится по формуле   bn = b1 * q в степени n−1
Входные данные:
-> На вход программе подаётся три целых числа: 1b1, q и n, каждое на отдельной строке.
Выходные данные:
-> Программа должна вывести n-ый член геометрической прогрессии. """
b1 = int(input())
q = int(input())
n = int(input())
print(b1 * q ** (n - 1))

# 22. Расстояние в метрах
""" Напишите программу, которая находит полное число метров по заданному числу сантиметров.
Формат входных данных:
-> На вход программе подаётся натуральное число – количество сантиметров.
Формат выходных данных:
-> Программа должна вывести одно число – полное число метров. """
cm = int(input())
print(cm // 100)

# 23. Мандарины
""" n школьников делят k мандаринов поровну, неделящийся остаток остается в корзине. 
Сколько целых мандаринов достанется каждому школьнику? Сколько целых мандаринов останется в корзине?
-> Формат входных данных:
На вход программе подаётся два целых числа: количество школьников и количество мандаринов, каждое на отдельной строке.
-> Формат выходных данных:
Программа должна вывести два числа: количество мандаринов, которое достанется каждому школьнику, 
и количество мандаринов, которое останется в корзине, каждое на отдельной строке. """
n = int(input())
k = int(input())
print(k // n)
print(k % n)

# 24. Сама неотвратимость
""" Безумный титан Танос собрал все 6 камней бесконечности и намеревается уничтожить половину населения Вселенной по щелчку пальцев. 
При этом если население Вселенной является нечетным числом, то титан проявит милосердие и округлит количество выживших в большую сторону. 
Помогите Мстителям подсчитать количество выживших.
Формат входных данных:
-> На вход дается число целое n – население Вселенной.
Формат выходных данных:
-> Программа должна вывести одно число – количество выживших. """
n = int(input())
print(n // 2 + n % 2)


# 25. Номер купе
""" В купейном вагоне имеется 99 купе с четырьмя местами для пассажиров в каждом. 
Напишите программу, которая определяет номер купе, в котором находится место с заданным номером 
(нумерация мест сквозная, начинается с 11). """

num = int(input())
print((num + 3) // 4)


# 26. Пересчет временного интервала
""" Напишите программу для пересчёта величины временного интервала, заданного в минутах, 
в величину, выраженную в часах и минутах. """

min_count = int(input())
print(min_count, 'мин - это', min_count // 60, 'час', min_count % 60, 'минут.')

# 27. Трехзначное число
""" Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трехзначного числа.
Формат входных данных:
-> На вход программе подаётся положительное трёхзначное число.
Формат выходных данных:
-> Программа должна вывести два числа с поясняющим текстом: сумма цифр и произведение цифр. """

num = int(input())
third_digit = num % 10
second_digit = (num // 10) % 10
first_digit = num // 100
print('Сумма цифр =', third_digit + second_digit + first_digit)
print('Произведение цифр =', third_digit * second_digit * first_digit)


# 28. Перестановка цифр
""" Дано трехзначное число abc, в котором все цифры различны. 
Напишите программу, которая выводит шесть чисел, образованных при перестановке цифр заданного числа.
Формат входных данных:
-> На вход программе подаётся положительное трёхзначное целое число, все цифры которого различны.
Формат выходных данных:
-> Программа должна вывести шесть чисел, образованных при перестановке цифр заданного числа 
в следующем порядке:  abc,acb,bac,bca,cab,cba. """

num = int(input())
c = num % 10
b = (num // 10) % 10
a = num // 100
print(a, b, c, sep='')
print(a, c, b, sep='')
print(b, a, c, sep='')
print(b, c, a, sep='')
print(c, a, b, sep='')
print(c, b, a, sep='')


# 29. Четырёхзначное число
""" Напишите программу для нахождения цифр четырёхзначного числа.
Формат входных данных:
-> На вход программе подаётся положительное четырёхзначное целое число.
Формат выходных данных:
-> Программа должна вывести текст в соответствии с условием задачи.
Sample Input 1:
 3281
Sample Output 1:
 Цифра в позиции тысяч равна 3
 Цифра в позиции сотен равна 2
 Цифра в позиции десятков равна 8
 Цифра в позиции единиц равна 1       """

num = int(input())
fourth_digit = num % 10
third_digit = (num % 100) // 10
second_digit = (num % 1000) // 100
first_digit = num // 1000
print('Цифра в позиции тысяч равна', first_digit)
print('Цифра в позиции сотен равна', second_digit)
print('Цифра в позиции десятков равна', third_digit)
print('Цифра в позиции единиц равна', fourth_digit)

# 30. Звездный прямоугольник
""" Напишите программу, которая выводит прямоугольник, по периметру состоящий из звездочек (*).
Примечание. Высота и ширина прямоугольника равны 4 и 17 звёздочкам соответственно. """
print('*****************')
print('*               *')
print('*               *')
print('*****************')

# 31. Сумма квадратов VS квадрат суммы
""" Напишите программу, которая считывает два целых числа a и b и выводит на экран квадрат суммы (a+b)2 
и сумму квадратов a2+b2 этих чисел.
Формат входных данных:
-> На вход программе подаётся два целых числа, каждое на отдельной строке.
Формат выходных данных:
-> Программа должна вывести текст в соответствии с условием. """
a = int(input())
b = int(input())
print('Квадрат суммы', a, 'и', b, 'равен', (a + b) **2)
print('Сумма квадратов', a, 'и', b, 'равна', a**2 + b**2)

# 32. Большое число
""" Как известно, целые числа в языке Python не имеют ограничений, которые встречаются в других языках программирования. 
Напишите программу, которая считывает четыре целых положительных числа a,b,c и d и выводит на экран значение выражения a в степени b + c в степени d.
Формат входных данных:
-> На вход программе подаётся четыре целых положительных числа a,b,c и d , каждое на отдельной строке в указанном порядке.
Формат выходных данных:
-> Программа должна вывести значение ab+cd. """
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(a ** b + c ** d)

# 33. Размножение n-ок
""" Напишите программу, которая считывает целое положительное число n, n [1;9] и выводит 
значение числа n + nn + nnn.
Формат входных данных:
-> На вход программе подаётся одно целое положительное число n, n∈[1;9].
Формат выходных данных:
-> Программа должна вывести число n+nn+nnn.
Примечание. Для первого теста 1 + 11 + 111 = 123. """
n = int(input())
print(n + 11 * n + 111 * n)

# 34. Пароль
""" При регистрации на сайтах требуется вводить пароль дважды. 
Это сделано для безопасности, поскольку такой подход уменьшает возможность неверного ввода пароля.
Напишите программу, которая сравнивает пароль и его подтверждение. 
Если они совпадают, то программа выводит: «Пароль принят», иначе: «Пароль не принят».
Формат входных данных:
-> На вход программе подаются две строки.
Формат выходных данных:
-> Программа должна вывести одну строку в соответствии с условием задачи. """
pass1 = input()
pass2 = input()
if pass1 == pass2:
    print('Пароль принят')
else:
    print('Пароль не принят')

# 35. Четное или нечетное?
""" Напишите программу, которая определяет, является число четным или нечетным.
Формат входных данных:
-> На вход программе подаётся одно целое число.
Формат выходных данных:
-> Программа должна вывести «Четное», если число четное, и «Нечетное» — если число нечетное. """
num = int(input())
if num % 2 == 0:
    print('Четное')
else:
    print('Нечетное')

# 36. Соотношение 
""" Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение: сумма первой и последней цифр равна разности второй и третьей цифр.
Формат входных данных:
-> На вход программе подаётся одно целое положительное четырёхзначное число.
Формат выходных данных:
-> Программа должна вывести «ДА», если соотношение выполняется, и «НЕТ» — если не выполняется. """
num = int(input())
digit_1 = num // 1000
digit_2 = (num % 1000) // 100
digit_3 = (num % 100) // 10
digit_4 = num % 10
if digit_1 + digit_4 == digit_2 - digit_3:
    print('ДА')
else:
    print('НЕТ')

# 37. Роскомнадзор
""" Напишите программу, которая определяет, разрешен ли пользователю доступ к интернет-ресурсу или нет.
Формат входных данных:
-> На вход программе подаётся целое число — возраст пользователя.
Формат выходных данных:
-> Программа должна вывести текст «Доступ разрешен», если возраст не менее 18, и «Доступ запрещен» - в противном случае. """
num = int(input())
if num >= 18:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')

# 38. Арифметическая прогрессия
""" Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке) 
последовательными членами арифметической прогрессии.
Формат входных данных:
-> На вход программе подаются три числа, каждое на отдельной строке.
Формат выходных данных:
-> Программа должна вывести «YES» или «NO» (без кавычек) в соответствии с условием задачи. """
num1 = int(input())
num2 = int(input())
num3 = int(input())
if num3 - num2 == num2 - num1:
    print('YES')
else:
    print('NO')

# 39. Наименьшее из двух чисел
""" Напишите программу, которая определяет наименьшее из двух чисел.
Формат входных данных:
-> На вход программе подаётся два различных целых числа.
Формат выходных данных:
-> Программа должна вывести наименьшее из двух чисел. """
num1 = int(input())
num2 = int(input())
if num1 < num2:
    print(num1)
else:
    print(num2)

# 40. Наименьшее из четырёх чисел
""" Напишите программу, которая определяет наименьшее из четырёх чисел.
Формат входных данных
На вход программе подаётся четыре целых числа.
Формат выходных данных
Программа должна вывести наименьшее из четырёх чисел.
Примечание. Учитывайте, что минимальные числа могут повторяться. """
num1, num2, num3, num4 = int(input()), int(input()), int(input()), int(input())
minimal = num1
if num1 > num2:
    minimal = num2
if num2 > num3:
    minimal = num3
if num3 > num4:
    minimal = num4
print(minimal)

# 41. Возрастная группа
""" Напишите программу, которая по введённому возрасту пользователя сообщает, к какой возрастной группе он относится:
->	до 13 (включительно) – детство;
->	от 14 до 24 (включительно) – молодость;
->	от 25 до 59 (включительно) – зрелость;
->	от 60 – старость.
Формат входных данных: На вход программе подаётся одно целое число – возраст пользователя.
Формат выходных данных: Программа должна вывести название возрастной группы. """
age = int(input())
if age <= 13:
    print('детство')
if 13 < age <= 24:
    print('молодость')
if 24 < age <= 59:
    print('зрелость')
if age > 59:
    print('старость')

# 42. Только +
""" Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.
Формат входных данных:
-> На вход программе подаются три целых числа.
Формат выходных данных:
-> Программа должна вывести одно число – сумму положительных чисел.
Примечание. Если положительных чисел нет, то следует вывести 0. """
num1, num2, num3 = int(input()), int(input()), int(input())
sum = 0
if num1 > 0:
    sum = sum + num1
if num2 > 0:
    sum = sum + num2
if num3 > 0:
    sum = sum + num3
print(sum)

# 43. Принадлежность-1 
""" Напишите программу, которая принимает целое число x и определяет, принадлежит ли данное число указанному промежутку (от -1 до 17) (не включая эти точки). 
Формат входных данных:
-> На вход программе подаётся целое число x.
Формат выходных данных:
-> Программа должна вывести текст в соответствии с условием задачи. """
x = int(input())
if x > -1 and x < 17:
    print('Принадлежит')
else:
    print('Не принадлежит')

# 44. Принадлежность-2
""" Напишите программу, которая принимает целое число x и определяет, принадлежит ли данное число указанным промежуткам (от -3 и меньше и от +7 и выше) включая начальные точки.
Формат входных данных:
-> На вход программе подаётся целое число x.
Формат выходных данных:
-> Программа должна вывести текст в соответствии с условием задачи. """ 
x = int(input())
if x <= -3 or x >= 7:
    print('Принадлежит')
else:
    print('Не принадлежит')

# 45. Принадлежность-3
""" Напишите программу, которая принимает целое число x и определяет, принадлежит ли данное число указанным промежуткам:
- Первый промежуток: от -2 включительно до -30 не включительно
- Второй промежуток: от 7 не включительно до 25 включительно.
Формат входных данных: На вход программе подаётся целое число x.
Формат выходных данных: Программа должна вывести текст в соответствии с условием задачи. """
x = int(input())
if (x <= -2 and x > -30) or x > 7 and x <= 25:
    print('Принадлежит')
else:
    print('Не принадлежит')

# 46. Красивое число
""" Назовем число красивым, если оно является четырехзначным и делится нацело на 7 или на 17. 
Напишите программу, определяющую, является ли введённое число красивым. 
Программа должна вывести «YES», если число является красивым, или «NO» в противном случае.
- Формат входных данных: На вход программе подаётся натуральное число.
- Формат выходных данных: Программа должна вывести текст в соответствии с условием задачи. """
num = int(input())
if (num / 1000 >= 1 and num / 1000 < 10) and (num % 7 == 0 or num % 17 == 0):
    print('YES')
else:
    print('NO')

# 47. Неравенство треугольника
""" Напишите программу, которая принимает три положительных числа и определяет, существует ли 
невырожденный треугольник с такими сторонами.
Формат входных данных: На вход программе подаётся три положительных целых числа.
Формат выходных данных: Программа должна вывести «YES» или «NO» в соответствии с условием задачи.
Примечание. Треугольник существует, если выполняется неравенство треугольника: 
a + b > c 
a + c > b
b + c > a,
где a,b,c - стороны треугольника.

т.е. длина любой стороны треугольника всегда меньше суммы длин двух его других сторон"""
a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print('YES')
else:
    print('NO')

# 48. Високосный год
""" Напишите программу, которая определяет, является ли год с данным номером високосным. Если год является високосным, то выведите «YES», иначе выведите «NO».
Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400.
Формат входных данных: На вход программе подаётся натуральное число.
Формат выходных данных: Программа должна вывести текст в соответствии с условием задачи. """
year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('YES')
else:
    print('NO')

# 49. Ход ладьи
""" Даны две различные клетки шахматной доски. Напишите программу, которая определяет, 
может ли ладья попасть с первой клетки на вторую одним ходом. 
Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки 
сначала для первой клетки, потом для второй клетки. 
Программа должна вывести «YES», если из первой клетки ходом ладьи можно попасть во вторую, или «NO» в противном случае.
-> Формат входных данных: На вход программе подаётся четыре числа от 1 до 8.
-> Формат выходных данных: Программа должна вывести текст в соответствии с условием задачи.
Примечание. Шахматная ладья ходит по горизонтали или вертикали. """

colomn_num1 = int(input())
line_num1 = int(input())
colomn_num2 = int(input())
line_num2 = int(input())
if colomn_num1 == colomn_num2 or line_num1 == line_num2:
    print('YES')
else:
    print('NO')

# 50. Ход короля 🌶
""" Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли король 
попасть с первой клетки на вторую одним ходом. 
Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала 
для первой клетки, потом для второй клетки. 
Программа должна вывести «YES», если из первой клетки ходом короля можно попасть во вторую, или «NO» в противном случае.
Формат входных данных: На вход программе подаётся четыре числа от 1 до 8.
Формат выходных данных: Программа должна вывести текст в соответствии с условием задачи.
Примечание. Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку. """

# 1st version:
colomn_num1 = int(input())
line_num1 = int(input())
colomn_num2 = int(input())
line_num2 = int(input())
diff_line = line_num2 - line_num1
diff_column = colomn_num2 - colomn_num1
if (diff_line == -1 or diff_line == 1 or diff_line == 0) and (diff_column == -1 or diff_column == 1 or diff_column == 0):
    print('YES')
else:
    print('NO')

# 2nd version:
colomn_num1 = int(input())
line_num1 = int(input())
colomn_num2 = int(input())
line_num2 = int(input())
diff_line = line_num2 - line_num1
diff_column = colomn_num2 - colomn_num1
if (-1 <= diff_line <= 1) and (-1 <= diff_column <= 1):
    print('YES')
else:
    print('NO')


# 51. Гонка спидстеров
""" Зум бросил вызов Флэшу и предложил ему честный поединок в виде гонки вокруг магнетара. 
В случае проигрыша эта нейтронная звезда зарядится и уничтожит мир, поэтому Флэш решил не рисковать без 
причины и узнать у своего друга Циско Рамона, есть ли смысл принимать вызов. 
Циско получил данные, что скорость Зума равна n, а скорость Флэша равна k.
Напишите программу, которая должна вывести ответ Циско на вопрос Флэша.
- Формат входных данных: На вход программе подаётся два целых числа n и k – скорости Зума и Флэша.
- Формат выходных данных: Если Зум быстрее Флэша, нужно вывести «NO», а если Флэш быстрее Зума, нужно вывести «YES». В случае же если их скорости равны, нужно вывести "Don't know". """
n = int(input())
k = int(input())
if n > k:
    print('NO')
elif k > n:
    print('YES')
else:
    print("Don't know")

# 52. Вид треугольника
""" Напишите программу, которая принимает три положительных числа и определяет вид треугольника, длины сторон которого равны введенным числам.
Формат входных данных
На вход программе подаются три числа – длины сторон существующего треугольника.
Формат выходных данных
Программа должна вывести на экран текст – вид треугольника («Равносторонний», «Равнобедренный» или «Разносторонний»). """
a = int(input())
b = int(input())
c = int(input())
if a == b and b == c:
    print('Равносторонний')
elif a != b and b != c and a != c:
    print('Разносторонний')
else:
    print('Равнобедренный')


# 53. Среднее число
""" Даны три различных целых числа. Напишите программу, которая находит среднее по величине число.
Формат входных данных: На вход программе подаётся три различных целых числа, каждое на отдельной строке.
Формат выходных данных: Программа должна вывести среднее по величине число.
Примечание. Средним по величине называется число, которое будет вторым, если три числа отсортировать в порядке возрастания. """

# 1-й вариант
num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 > num2 and num2 > num3 or num1 < num2 and num2 < num3:
    print(num2)
elif num2 > num1 and num1 > num3 or num2 < num1 and num1 < num3:
    print(num1)
elif num2 > num3 and num3 > num1 or num2 < num3 and num3 < num1:
    print(num3)

# 2-й вариант
num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 > num2 > num3 or num1 < num2 < num3:
    print(num2)
elif num2 > num1 > num3 or num2 < num1 < num3:
    print(num1)
elif num2 > num3 > num1 or num2 < num3 < num1:
    print(num3)

# 54. Количество дней
""" Дан порядковый номер месяца (1,2,…, 12). 
Напишите программу, которая выводит на экран количество дней в этом месяце. Принять, что год является невисокосным.
Примечание. Постарайтесь написать программу так, чтобы в ней было не более трех условий.
Формат входных данных: На вход программе подаётся одно целое число – порядковый номер месяца.
Формат выходных данных: Программа должна вывести количество дней в этом месяце. """
num = int(input())
if num == 4 or num == 6 or num == 9 or num == 11:
    print(30)
elif num == 2:
    print(28)
else:
    print(31)

# 55. Церемония взвешивания
""" Известен вес боксера-любителя (целое число). Известно, что вес таков, что боксер может быть отнесён к одной из трех весовых категорий:
1.	Легкий вес – до 60 кг (невключительно);
2.	Первый полусредний вес – до 64 кг (невключительно);
3.	Полусредний вес – до 69 кг (невключительно).
Напишите программу, определяющую, в какой категории будет выступать данный боксер.
Формат входных данных: На вход программе подаётся одно целое число.
Формат выходных данных: Программа должна вывести текст – название весовой категории. """
weight = int(input())
if num < 60:
    print('Легкий вес')
elif num < 64:
    print('Первый полусредний вес')
else:
    print('Полусредний вес')

# 56. Самописный калькулятор 🌶
""" Напишите программу, которая считывает с клавиатуры два целых числа и строку. 
Если эта строка является обозначением одной из четырёх математических операций (+, -, *, /), то 
выведите результат применения этой операции к введённым ранее числам, 
в противном случае выведите «Неверная операция» (без кавычек). 
Если пользователь захочет поделить на ноль, выведите текст «На ноль делить нельзя!» (без кавычек).
Формат входных данных: На вход программе подаются два целых числа и строка, всё на отдельной строке.
Формат выходных данных: Программа должна вывести результат применения операции к введенным числам или соответствующий текст, если операция неверная либо если происходит деление на ноль. """
num1 = int(input())
num2 = int(input())
operation = input()
if operation == '*':
    print(num1 * num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '+':
    print(num1 + num2)
elif operation == '/':
    if num2 != 0:
        print(num1 / num2)
    else:
        print('На ноль делить нельзя!')
else:
    print('Неверная операция')

# 57. Цветовой микшер 🌶
""" Красный, синий и желтый называются основными цветами, потому что их нельзя получить путем смешения других цветов. 
При смешивании двух основных цветов получается вторичный цвет:
->	если смешать красный и синий, то получится фиолетовый;
->	если смешать красный и желтый, то получится оранжевый;
->	если смешать синий и желтый, то получится зеленый.
Напишите программу, которая считывает названия двух основных цветов для смешивания. 
Если пользователь вводит что-нибудь помимо названий «красный», «синий» или «желтый», то программа должна вывести сообщение об ошибке. 
В противном случае программа должна вывести название вторичного цвета, который получится в результате.
Формат входных данных: 
-> На вход программе подаются две строки, каждая на отдельной строке.
Формат выходных данных:
-> Программа должна вывести полученный цвет смешения либо сообщение «ошибка цвета», если введён был не цвет.
Примечание 1. Если смешать красный и красный, то получится красный и т.д. """

color_1 = input()
color_2 = input()

if color_1 == 'красный' and color_2 == 'синий' or color_2 == 'красный' and color_1 == 'синий':
    print('фиолетовый')
elif color_1 == 'красный' and color_2 == 'желтый' or color_2 == 'красный' and color_1 == 'желтый':
    print('оранжевый')
elif color_1 == 'синий' and color_2 == 'желтый' or color_2 == 'синий' and color_1 == 'желтый':
    print('зеленый')
elif color_1 == color_2 and (color_1 == 'красный' or color_1 == 'синий' or color_1 == 'желтый'):
    print(color_1)
else:
    print('ошибка цвета')

# 58. Цвета колеса рулетки 🌶
""" На колесе рулетки карманы пронумерованы от 0 до 36. Ниже приведены цвета карманов: 
•	карман 0 зеленый;
•	для карманов с 1 по 10 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
•	для карманов с 11 по 18 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный;
•	для карманов с 19 по 28 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
•	для карманов с 29 по 36 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный.
Напишите программу, которая считывает номер кармана и показывает, является ли этот карман зеленым, красным или черным. 
Программа должна вывести сообщение об ошибке, если пользователь вводит число, которое лежит вне диапазона от 0 до 36.
Формат входных данных: 
-> На вход программе подаётся одно целое число.
Формат выходных данных: 
-> Программа должна вывести цвет кармана либо сообщение «ошибка ввода», если введённое число лежит вне диапазона от 0 до 36. """

pocket_num = int(input())
if pocket_num == 0:
    print('зеленый')
elif 1 <= pocket_num <= 10:
    if pocket_num % 2 == 0:
        print('черный')
    else:
        print('красный')
elif 11 <= pocket_num <= 18:
    if pocket_num % 2 == 0:
        print('красный')
    else:
        print('черный')
elif 19 <= pocket_num <= 28:
    if pocket_num % 2 == 0:
        print('черный')
    else:
        print('красный')
elif 29 <= pocket_num <= 36:
    if pocket_num % 2 == 0:
        print('красный')
    else:
        print('черный')
elif pocket_num < 0 or pocket_num > 36:
    print('ошибка ввода')


# 59. Пересечение отрезков 
""" На числовой прямой даны два отрезка: [a1; b1] и [a2; b2]. 
Напишите программу, которая находит их пересечение.
Пересечением двух отрезков может быть:
- отрезок;
- точка;
- пустое множество.
Формат входных данных:
На вход программе подаются 4 целых числа a1, b1, a2, b2, каждое на отдельной строке. Гарантируется, что a1< b1 и a2 < b2.
Формат выходных данных:
Программа должна вывести на экран границы отрезка, являющегося пересечением, либо общую точку, либо текст «пустое множество». """

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if a1 < a2:
    if a2 > b1:
        print('пустое множество')
    elif a2 == b1:
        print(a2)
    elif a2 < b1 and b2 >= b1:
        print(a2, b1)
    elif a2 < b1 and b2 < b1:
        print(a2, b2)
elif a2 < a1:
    if b2 < a1:
        print('пустое множество')
    elif b2 == a1:
        print(a1)
    elif b2 > a1 and b2 <= b1:
        print(a1, b2)
    elif a1 < b2 and b1 < b2:
        print(a1, b1)
elif a1 == a2:
    if b1 <= b2:
        print(a1, b1)
    elif b2 < b1:
        print(a2, b2)

# 60. Начало столетия
""" Напишите программу, которая определяет, оканчивается ли год с данным номером на два нуля. 
Если год оканчивается, то выведите «YES», иначе выведите «NO».
Формат входных данных
На вход программе подаётся натуральное число.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи. """
year = int(input())
if year % 100 == 0:
    print('YES')
else:
    print('NO')

# 61. Шахматная доска
""" Заданы две клетки шахматной доски. Напишите программу, которая определяет, имеют ли указанные клетки один цвет или нет. 
Если они покрашены в один цвет, то выведите слово «YES», а если в разные цвета, то «NO».
Формат входных данных
На вход программе подаётся четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи. """
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x1 + y1) % 2 == 0 and (x2 + y2) % 2 == 0 or (x1 + y1) % 2 != 0 and (x2 + y2) % 2 != 0:
    print('YES')
else:
    print('NO')

# 62. Girls only
""" Футбольная команда набирает девочек от 10 до 15 лет включительно. 
Напишите программу, которая запрашивает возраст и пол претендента, используя обозначение пола 
буквы m (от male – мужчина) и f (от female – женщина) и определяет подходит ли претендент для вступления в команду или нет. 
Если претендент подходит, то выведите «YES», иначе выведите «NO».
Формат входных данных: на вход программе подаётся натуральное число – возраст претендента и буква обозначающая пол m (мужчина) или f (женщина).
Формат выходных данных: программа должна вывести текст в соответствии с условием задачи. """
age = int(input())
sex = input()
if 10 <= age <= 15 and sex == 'f':
    print('YES')
else:
    print('NO')

# 63. Римские цифры
""" Напишите программу, которая считывает целое число и выводит соответствующую ему римскую цифру. 
Если число находится вне диапазона 1−10, то программа должна вывести текст «ошибка».
Формат входных данных: На вход программе подаётся целое число.
Формат выходных данных: Программа должна вывести текст в соответствии с условием задачи. """
num = int(input())
if num == 1:
    print('I')
elif num == 2:
    print('II')
elif num == 3:
    print('III')
elif num == 4:
    print('IV')   
elif num == 5:
    print('V')    
elif num == 6:
    print('VI')    
elif num == 7:
    print('VII')
elif num == 8:
    print('VIII')   
elif num == 9:
    print('IX')    
elif num == 10:
    print('X')
else:
    print('ошибка')

# 63. YES or NO вот в чем вопрос
""" Напишите программу, которая принимает на вход число и в зависимости от условий выводит текст «YES», либо «NO».
Условия:
- если число нечётное, то вывести «YES»;
- если число чётное в диапазоне от 2 до 5 (включительно), то вывести «NO»;
- если число чётное в диапазоне от 6 до 20 (включительно), то вывести «YES»;
- если число чётное и больше 20, то вывести «NO».
Формат входных данных: На вход программе подаётся натуральное число.
Формат выходных данных: Программа должна вывести текст в соответствии с условием задачи. """
num = int(input())
if num % 2 != 0:
    print('YES')
elif num % 2 == 0:
    if num >= 2 and num <= 5:
        print('NO')
    elif num >= 6 and num <= 20:
        print('YES')
    elif num > 20:
        print('NO')

# 65. Ход слона
""" Даны две различные клетки шахматной доски. 
Напишите программу, которая определяет, может ли слон попасть с первой клетки на вторую одним ходом. 
Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для
первой клетки, потом для второй клетки. 
Программа должна вывести «YES», если из первой клетки ходом слона можно попасть во вторую или «NO» в противном случае.
Формат входных данных: На вход программе подаётся четыре числа от 1 до 8.
Формат выходных данных: Программа должна вывести текст в соответствии с условием задачи.
Примечание. Шахматный слон ходит по диагоналям. """
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x2 - x1 == y2 - y1):
    print('YES')
elif (x2 - x1 == y1 - y2):
    print('YES')
elif (x1 - x2 == y1 - y2):
    print('YES')
elif (x1 - x2 == y2 - y1):
    print('YES')
else:
    print('NO')

# 66. Ход коня
""" Даны две различные клетки шахматной доски. 
Напишите программу,  которая определяет, может ли конь попасть с первой клетки на вторую одним ходом. 
Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для 
первой клетки, потом для второй клетки. 
Программа должна вывести «YES», если из первой клетки ходом коня можно попасть во вторую или «NO» в противном случае.

