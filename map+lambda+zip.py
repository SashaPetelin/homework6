# Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.

#     *Пример:*

#     - Для n = 3:  {1: 2, 2: 2.25 , 3: 2.37}
#     Необходимо сложить все значения словаря и вывести  сумму на экран.

n = int(input("Введите число: "))

lst = list(map((lambda n: (1 + (1/n))**n),range(1,n+1)))
keys = list(range(1,n))
vocab = dict(zip(keys,lst))
print(vocab)
print(round(sum(vocab.values()),3))

# d = {i: (1+(1/i))**i for i in range(1,n+1)}
# print(d)
# print()
# summa = sum(d.values())
# print("Сумма значений в словаре равна", round(summa,3))