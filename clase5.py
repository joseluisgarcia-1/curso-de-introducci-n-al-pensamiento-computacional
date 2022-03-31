#<literales> = 1,'abc', 2.0, True
#<operadores> = +,/,*,%,**,=,==
#<literal><operador><literal>

suma = 1+2
print("suma de 1+2 =",suma)
#div_mal = 5 / 'platzi'
#print("esto nos arroja error porque un número no se puede dividir por un string o una línea de caracteres",div_mal)
multi = 5*'platzi'
print("esto si se puede hacer en python, multi = 5*'platzi', multiplicar una cadena de caracteres:",multi)
print("Hola amiguitos")

#<objeto><operador><objeto> "expresión"
#>> <valor>
suma_cadenas = 'platzi' + 'aprender'
print(suma_cadenas)
#le estados diciendo que el 2 es un objeto el + el operador y el otro dos el otro objeto, teniendo en cuenta la sintáxis que tengo antes,y valor es el resultado de la suma
new_suma = 2+2
print(new_suma)
print()
my_int = 1
my_float = 1.0
my_bool = False
my_none = None
print(type(my_int))
print(type(my_float))
print(type(my_bool))
print(type(my_none))
print()
#con lo anterior obtenemos la clase de datos que es cada uno de ellos
print("operaciones que podemos hacer en python")
print()
suma1 = 20+98
print("suma de 20+98:",suma1)
resta1 = 30-43
print("resta de 30-43:",resta1)
multi1 = 3.3 * 5
print("multiplicacion de 3.3*5:",multi1)
div_doble = 9 // 2
print("división doble de 9//2, con el cuál obtenemos el resultado como número entero:",div_doble)
div_senci = 9/2
print("división normal de 9/2, con el cuál obtenemos el resultado como número decimal:",div_senci)
modul = 9%2
print("división con la cual obtenemos el resto de la división de 9%2:",modul)
potencia = 2**3
print("potencia la cual obtenemos con el doble ** y hacemos la operación de 2**3:",potencia)