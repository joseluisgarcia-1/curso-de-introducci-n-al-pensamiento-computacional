mi_lista = [1,2,3,4]
print("estoy accediendo al dato que está en la posición o indice 3 y corresponde al número 4:",mi_lista[3])
#podemos acceder con los slices también
print("aquí estamos accediendo al dato desde la posición 0 hasta la 1",mi_lista[:2])
#podemos agregar datos a la lista mediate el metodo .append() y unicamente se le puede pasar un dato a la vez
mi_lista.append(6)
print(mi_lista)
#le voy a modificar el valor que está en la posición 0 y le voy a colocar un string
mi_lista[0] = 'Messi'
print(mi_lista)
#le voy a modificar el valor que está en la posición 0 y le voy a colocar un diccionario adentro
mi_lista[3] = {'messi': 'barca', 'psg': 'mbappe'}
print(mi_lista)
mi_lista.append('Europeos')
print(mi_lista)
print(len(mi_lista))
#ahora le voy a quitar un dato a la lista con el método .pop, para quitar un dato con este método hay que pasarle el indice, es decir, la posición del dato que queremos quitar
mi_lista.pop(2)
print(mi_lista)
#ahora voy a iterar las listas
print("**for**")
for n in mi_lista:
    print(n)

mi_lista_2 = ['Messi', 2, 3, {'messi': 'barca', 'psg': 'mbappe'}, 6, 'Europeos']
mi_lista_2.clear()
print("mi lista quedó limpia porque le apliqué el metodo clear():",mi_lista_2)
print()
# para pasar una lista a otra lista y con diferente id es más fácil con el método list, así:
mi_lista_2 = ['Messi', 2, 3, {'messi': 'barca', 'psg': 'mbappe'}, 6, 'Europeos']
lista_3 = mi_lista_2
lista_clonada = list(lista_3)
print(id(mi_lista_2))
print(id(lista_3))
print("nos damos cuenta que el id ya cambió y hemos clonado la lista:",id(lista_clonada))
print()
print("****list comprehensions****")
my_list = list(range(10))
print(my_list)
print()
#vamos a multiplicar por 2 todos los números pares de la lista
multi_2 = [i*2 for i in my_list]
print("multiplicar por 2 todos los números pares de la lista:",multi_2)
print()
#vamos a obtener solo los números pares de la lista
pares = [i for i in my_list if i % 2 ==0]
print("solo los números pares de la lista:",pares)
#vamos a obtener solo los números impares de la lista
impares = [i for i in my_list if i % 2 ==1]
print("solo los números impares de la lista:",impares)
