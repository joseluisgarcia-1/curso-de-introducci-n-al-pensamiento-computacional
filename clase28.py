"""
con el try except lo que hacemos es si alguien usa la división entre cero o pasa un dato 0 lo que pasa es que
imprimir la lista normal, el programa no se revienta
"""
def divide_elementos_de_la_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print("***no muestra el error***",e)
        return lista
lista = list(range(1,11))
#con 2 la función trabaja bien
#divisor = 2
#ahora para que salga un error y poder manejarlo con una try except le colocamos el divisor = 0
divisor = 0
print(divide_elementos_de_la_lista(lista,divisor))