"""
funciones:

def <nombre>(<parametros>):
    <cuerpo de la función>
    return <expresión>

def suma(a,b):
    total = a+b
    return total    
suma(2,4)
"""
def suma(a,b):
    total = a+b
    print(total)
    return total    
suma(2,6)

def nombres(name, lastname, inverso=False):
    if inverso:
        print(f'{lastname} {name}')
    else:
        print(f'{name} {lastname}')

nombres('Messi', 'Lio')
nombres('Messi', 'Lio', inverso=True)
nombres(lastname='Lio', name='Messi')
