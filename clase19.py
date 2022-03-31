#es una lectura de finobacci y la recursividad, eso está en el archivo de apuntes.txt

def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Ingresa un entero: "))
print(fibonacci(n))