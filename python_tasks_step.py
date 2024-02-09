
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








