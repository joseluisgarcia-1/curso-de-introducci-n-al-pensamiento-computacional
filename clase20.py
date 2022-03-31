def multiplicar_por_dos(n):
    return n * 2

def sumar_dos(n):
    return n + 2

def aplicar_operacion(f, numeros):
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)
        print(resultados)

n = int(input("ingrese un número: "))
print(multiplicar_por_dos(n))
print(sumar_dos(n))
print()
numeros = [1, 2, 3]
aplicar_operacion(multiplicar_por_dos, numeros)
print()
#[2, 4, 6]
print()
aplicar_operacion(sumar_dos, numeros)
#[3, 4, 5]
print()
sumar = lambda x, y: x + y
print("la lambda",sumar(2, 3))
print()
#5

def aplicar_operaciones(num):
    operaciones = [abs, float]

    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))

    return resultado
print(aplicar_operaciones(-5))