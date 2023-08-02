lista = [10, 3, 8, 2, 9, 200, 100, 3, 0, 90, 560, 32,80, 102]
menor = None
mayor = None
for numero in lista:
    if menor == None and mayor== None:
        menor = numero
        mayor = numero
    else:
        if numero < menor:
            menor = numero
        if numero > mayor:
            mayor = numero
print(f"El numero mayor es {mayor}")
print(f"El numero menor es {menor}")