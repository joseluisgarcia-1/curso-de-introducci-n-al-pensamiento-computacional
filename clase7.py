#len
my_str = 'hola amiguitos'
print("me cuenta cuantos caracteres tiene mi string: my_str = 'hola amiguitos':",len(my_str))
print()
#indexación
print("voy a imprimir my_str[3], es decir, el dato que está en la posición 3 de mi string:",my_str[3])
#slicing
print("voy a imprimir my_str[3:10], es decir, el dato que está en la posición 3 hasta antes del 10:",my_str[3:10])
print("voy a imprimir my_str[3:12:2], es decir, el dato que está en la posición 3 hasta antes del 12 en pasos de 2:",my_str[3:12:2])
print("voy a imprimir my_str[::-1], es decir, que me ponga la cadena de atras para adelante:",my_str[::-1])
print("voy a imprimir my_str[::], es decir, desde el principio hasta el final:",my_str[::])

format_read = f'{my_str} cómo están'
print(format_read)
print(len(format_read))
#puedo contar también el número de posiciones así:
print(len(format_read[15:20]))
#o imprimir los caracteres así:
print(format_read[15:21])
#se le puede colocar en mayúsculas también
print(format_read[15:21].upper())
#o imprimir cuantas veces hay un caracter en el string así:
print("voy a imprimir cuántas veces está la o en ese string:",format_read[::].count('i'))
format_read2 = f'{my_str} platzi' * 3
print("cadena multiplicada por 3:",format_read2)
print()
#entradas con input
name = input("ingresa un nombre de futbolista: ")
print(name)
print("el nombre que ingresaste es:",name)
print(type(name))
print()
number = int(input("ingresa un número: "))
print("el número que ingresaste es:",number)
print("el numero es de tipo entero",type(number))
print()
number_float = float(input("ingresa un número: "))
print("el número que ingresaste es:",number_float)
print("el numero es de tipo float",type(number_float))
print()
#reto, recibir el nombre, darle un saludo, y contar la longitud del saludo como del nombre
name_reto = input("Ingresa tu nombre: ")
print("nombre ingresado:",name_reto)
welcome = f'hola amigo {name_reto}'
print("saludo:",welcome)
print("número de caracteres de la cadena:",len(welcome))
