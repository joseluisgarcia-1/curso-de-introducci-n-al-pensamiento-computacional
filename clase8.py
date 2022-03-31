equal = 2==3
diferencia = 2!=3
mayorque = 2>3
menorque = 2<3
menoro = 2<=3
mayoro = 2>=3
num_1 = int(input("Ingresa el número 1 que sea entero entero: "))
num_2 = int(input("Ingresa el número 2 que sea entero: "))
if num_1 > num_2:
    print("El número 1 es mayor que el número 2")
elif num_1 < num_2:
    print("El número 2 es mayor que el número 1")
else:
    print("Los números son iguales")