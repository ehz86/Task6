flag = True
while flag:
    try:
        a = input('Введите числовую последовательность: ').split()
        delta = int(input('Введите число DELTA: '))
        m = int(a[0])    
    except ValueError:
        print('неверный ввод')
    else: 
        flag = False
c = 0
for i in range(len(a)):
    a[i] = int(a[i])
    if int(a[i]) < m:
        m = a[i]
for i in range(len(a)):
    if a[i] - m == delta:
        c += 1
print(c)