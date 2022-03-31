objetivo = int(input("Escoge un número entero: "))
respuesta = 0

#le vamos a decir que mientras que la respuesta al cuadrado sea menor que el objetivo que quiere decir, el número ingresado por el usuario
# aumente la respuesta en 1
while respuesta**2 < objetivo:
    respuesta += 1
    print("número con el que probé para encontrar la raíz:",respuesta)
if respuesta**2 == objetivo:
    print(f'la raíz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'{objetivo} no tiene raíz cuadrada exacta')