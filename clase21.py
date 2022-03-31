my_tuplin = ()
print(type(my_tuplin))
my_tuple =(1,'Barcelona',3,'Hola',5,True, False, {2,3,4,5})
print(my_tuple)
#puedo acceder a los datos de la tupla mediante sus indices, por ejemplo, así: my_tuple[7]
print("aquí accedí al indice 7 de mi tupla que corresponde al diccionario que tiene la tupla:",my_tuple[7])
#Quiero modificar un dato de mi tupla como lo hago en las lista, pues eso no lo puedo hacer porque las tuplas son inmutables
#por ejemplo para intentar hacer eso es así:
"""
my_tuple[5] = 2
entonces python arroja este error:
TypeError: 'tuple' object does not support item assignment
"""
#el siguiente no lo toma como una tupla, esto lo toma como un entero, aunque lo coloquemos dentro de parentesis
my_tuple1 = (1)
print(type(my_tuple1))
#nos imprime lo siguiente: <class 'int'>
print()
#si queremos generar una tupla con un solo elemento lo que hacemos es colocar el elemento seguido de una coma , por ejemplo así:
my_tuple_test = (100,)
print(type(my_tuple_test))
#aquí ya nos imprime lo siguiente: <class 'tuple'> y es una tupla con un solo elemento
print()
#también podemos sumar las tuplas así:
my_tuple_2 = (10,20,30)
suma_tuples = my_tuple_test + my_tuple_2
print(suma_tuples)
#eso nos imprime lo siguiente: (100, 10, 20, 30)
print()
print("desempacando tupla")
"""también podemos desempaquetar las tuplas pero para ello debemos pasarle igual número varibles como de datos que queremos desempaquetar
para que cada variable que le pasemos quede asignada a un valor, entonces lo hacemos así:
voy a desempaquetar la tupla sumada es decir, suma_tuples, que si le pasamos una variable de más arroja error
"""
print(suma_tuples)
a,b,c,d = suma_tuples
print("valor de a:",a,"valor de b:",b,"valor de c:",c,"valor de d:",d)
print()
print("""otra forma es mediante una función así:
def coordenadas():
    return 50,77
coordenada = coordenadas()
print("obtenemos los datos de la función coordenadas",coordenada)
(50, 77)
""")
def coordenadas():
    return 50,77
coordenada = coordenadas()
print("obtenemos los datos de la función coordenadas",coordenada)

print("""***una nueva forma es así:***

x,y = coordenadas()
print(x,y)
(50, 77)
x = 50
y = 77
""")
x,y = coordenadas()
print("x =",x)
print("y =",y)