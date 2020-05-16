edad = input('Introduce tu edad: ')
edad = int(edad)

if edad < 4:
    print('Gratis')
elif edad >= 4 and edad <= 18:
    print('5€')
else:
    print('10€')