def cuadrado(x):
    if x < 3:
        print('if')
        return x * x
    else:
        print('else')
        return x ** 2 

x = input('Mete un valor: ')
print(cuadrado(int(x)))

array = [1,2,3,4,5,6,7,8]
for v in array:
    print(v)

