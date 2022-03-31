my_dict = {
    'Messi': 34,
    'Mbappe': 23,
    'Vinicius': 22
}
print("- diccionario original:",my_dict)
#para acceder a un dato de un diccionario lo podemos hacer así:
print("- con esto nos arroja el valor de la llave Messi:",my_dict['Messi'])
#para modificar un valor lo podemos hacer así:
my_dict['Messi'] = 30
print("- obtenemos que messi modificó su edad {'Messi': 30, 'Mbappe': 23, 'Vinicius': 22}",my_dict)
"""
una linda prueba de acceder a un dato que no existe y evitar que nos arroje un error lo podemos hacer así:

my_dict.get('Cr', 33)

lo que le estamos diciendo es, de ese diccionario traigame o acceda a la llave 'Cr' y si no existe esa llave 'Cr' imprimame el 33
y si por el contrario le paso una llave que si existe, el imprime el valor que está en el diccionario, así:
my_dict.get('Messi', 33)
entonces ahí le dije, del diccionario traigame el valor que corresponde a la llave messi y si no existe esa llave traigame el numero 33, pero como la llave 
si existe en el diccionario, me trajo el valor que corresponde a messi
"""
print(my_dict.get('Cr', 33))
print("me trajo el valor de 30 porque antes había modificado el valor que tenía messi:",my_dict.get('Messi', 33))
print()
#si queremos agregar una nueva llave al diccionario lo podemos hacer así:
my_dict['Haaland'] = 24
print("aquí nos damos cuenta que agregó a haaland:",my_dict)
print()
#ahora, si yo quiero eliminar un dato de ese diccionario lo que hago es pasarle la llave, así:
del my_dict['Vinicius']
print("aquí nos damos cuenta que eliminamos el dato de Vinicius:",my_dict)
print()
#iterar a lo largo del diccionario con for
#para obtener las llaves es con keys()
for llave in my_dict.keys():
    print(llave)
print()
#para obtener los valores es con values()
for valor in my_dict.values():
    print(valor)
print()
#para obtener las llaves y los valores es con items()
for llave, valor in my_dict.items():
    print(f'esta es la llave: {llave}, y este es el valor: {valor}')

#un truco para saber si existe una llave dentro del diccionario es así:
print("la llave messi existe en mi diccionario:",'Messi' in my_dict)
