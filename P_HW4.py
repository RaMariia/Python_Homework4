# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# from random import randint

# numFirst = int(input("Введите количество элементов первого массива: "))
# array_1 = [randint(0,10) for _ in range(numFirst)]
# print(array_1)  
# array_1 = set(array_1)

# numSecond = int(input("Введите количество элементов первого массива: "))
# array_2 = [randint(0,10) for _ in range(numSecond)] 
# print(array_2)  
# array_2 = set(array_2)

# array_3 = array_1.union(array_2)
# print('Числа, которые встречаются без повторений: ', array_3)

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, 
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод 
# – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды 
# с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать 
# за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.


# N_NumberOfBushes = int(input("Введите количество кустов: "))
# N_Bush = int(input("Введите номер интересующего куста:"))
# Sum_berries = 0
# if N_Bush == N_NumberOfBushes : 
#     Sum_berries = N_Bush*2
# elif N_Bush == 1 :
#     Sum_berries = N_NumberOfBushes+3
# else : Sum_berries == N_Bush*3
# print (Sum_berries)

# from random import randint
# NumberOfBushes = int(input('Введите количество кустов: '))
# array_bushes = list(randint(1,10) for i in range (NumberOfBushes))
# print(array_bushes)
# N_Bush = int(input("Введите номер интересующего куста:"))
# sum_berries = 0
# if N_Bush == 1:
#     sum_berries = array_bushes[0] + array_bushes[1] + array_bushes[-1]
# elif N_Bush == len(array_bushes):
#     sum_berries = array_bushes[-2] + array_bushes[-1] + array_bushes[0]
# else:
#     sum_berries = array_bushes[N_Bush-1] + array_bushes[N_Bush-2] + array_bushes[N_Bush]
# print('максимальное количество ягод: ', sum_berries)