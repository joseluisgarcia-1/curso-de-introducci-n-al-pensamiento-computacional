"""
para evitar que la iteración se vuelva infirita lo que hacemos es decirle al contador que iniciamos en 0, pasarle un valor de 1
para que él empiece a sumarlo, si no como contador está en 0 si no le aumentamos el valor siempre va ser 0 y por ende esa iteración
siempre va ser infinita, por eso le decimos contador +=1, y ahí el empieza a contar hasta llegar a 10
- contador = contador + 1, es lo mismo qué:
contador +=1
"""

#ejemplo uno de while
contador = 0
while contador < 10:
    print("soy el valor:",contador)
    contador += 1

#ejemplo dos de while
contador_interno = 0
contador_externo = 0
while contador_externo < 10:
    while contador_interno < 6:
        print("valor de interno:",contador_interno, "valor de externo",contador_externo)
        contador_interno +=1
        if contador_interno >= 3:
            break
    contador_externo +=1
    contador_interno = 0
# lo que le decimos aquí es que: mientras que el valor externo sea menor que 10, imprima el contador interno en numeros que sean menores que 6
# ya con el break lo que le decimos es mientras que el valor externo sea menor que 10, imprima hasta el numero 10, pero si el contador interno es mayor o igual que 3 deténgase
# solo imprima hasta el número maoyr o igual que 3
