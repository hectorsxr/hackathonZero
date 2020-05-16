'''
Almacena caracteres contraseña en una variable
'''

password = 'contraseña'

pasword_user = input('Introduzca contraseña: ')
pasword_user = pasword_user.lower()
password = password.lower()

if password == pasword_user:
    print('Coincide')
else:
    print('No coincide')