#El limite de recursión se lo puede modificar, ya sea ampliar o disminuir
import sys
print("limite de recursión por defecto de python:",sys.getrecursionlimit())
sys.setrecursionlimit(10000)
print("limite de recursión modificado a:",sys.getrecursionlimit())
print()
def factorial(n):
    """
    Calcúla el factorial de n.

    n int > 0
    returns n!

    """
    print(n)
    if n == 1:
        return 1
        
    return n*factorial(n-1)

n = int(input("Ingresa un entero: "))
print(factorial(n))