
my_range = range(1,8)
print(my_range)
for i in my_range:
    print(i)

range_pasos = range(0,7,2)
ranges_2 = range(0,8,2)
print()
print(range_pasos == ranges_2)

for paso1 in range_pasos:
    print(paso1)
print()
for paso2 in ranges_2:
    print(paso2)
#nos dimos cuenta que eran los mismos rangos porque los datos que tienen no incluyen más del último número que vendría siendo el 6
#para saber en qué id guarda el pc el rango o un dato y saber si un datos es diferente de otro lo podemos hacer así:
#también lo podemos verificar así:
print(id(range_pasos))
print(id(ranges_2))
#para saber si es igual que otro rango en este caso
print(range_pasos is ranges_2)
print()
print("numeros pares del 0 al 100")
for i in range(0,10,2):
    print(i)
print("impares del 1 al 99")
for i in range(1,11,2):
    print(i)