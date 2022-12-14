# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

lst = [12, 34, -7, 1, 43, -99, 25, 100, 78, 5]

# sum = 0
# for i in range(len(lst)):
#     if i%2>0:
#         sum+=lst[i]
# print("Сумма чисел на нечетных позициях", sum)

odd = [num for index, num in enumerate(lst) if index%2==1]
print(odd)
print(sum(odd))