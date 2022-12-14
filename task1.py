num = '7 + 1 * 2 * 3 / 5 - 3'
num = num.split()
print(num)
while len(num) > 1:
    if '*' in num:
        num[num.index('*') - 1] = float(num[num.index('*') - 1]) * float(num[num.index('*') + 1])
        num.pop(num.index('*') + 1)
        num.pop(num.index('*'))
        print(num)
    elif '/' in num:
        num[num.index('/') - 1] = float(num[num.index('/') - 1]) / float(num[num.index('/') + 1])
        num.pop(num.index('/') + 1)
        num.pop(num.index('/'))
        print(num)
    elif '-' in num:
        num[num.index('-') - 1] = float(num[num.index('-') - 1]) - float(num[num.index('-') + 1])
        num.pop(num.index('-') + 1)
        num.pop(num.index('-'))
        print(num)
    elif '+' in num:
        num[num.index('+') - 1] = float(num[num.index('+') - 1]) + float(num[num.index('+') + 1])
        num.pop(num.index('+') + 1)
        num.pop(num.index('+'))
        print(num)

print(round(num[0], 3))    

