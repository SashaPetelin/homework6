# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.


from random import randint

# def list(n):
#     list = []
#     for i in range(n):
#         list.append(randint(-n, n))
#     return list

n = int(input('Введите число N: '))
# numbers = list(n)
# print(numbers)

numbers = [x for x in range(-n,n+1)]
print(numbers)

mlt = 1
original = 'file.txt'
with open(original, 'r') as main:
    for line in main:
        mlt *= numbers[int(line)]
    print("Произведение чисел равно ",mlt)