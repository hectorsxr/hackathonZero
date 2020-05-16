'''
    Una panadería vende barras de pan a 3'49.
    Si el pan no es del día cuesta 60% menos.
'''

precio_pan = 3.49
descuento = 1 - 0.6

precio_pan_descuento = precio_pan * descuento
barras_de_pan = input('Introduce las barras de pan que quieres comprar: ')
barras_de_pan = int(barras_de_pan)

print('Total de barras: ', barras_de_pan)
print('Precio descuento: ', precio_pan_descuento)
print('Precio total: ', barras_de_pan * precio_pan_descuento)