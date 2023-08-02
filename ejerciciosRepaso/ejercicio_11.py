numeros = list(range(1,100))

def imprimirPares():
    for valor in numeros:
        if (valor % 2) == 0:
            print(valor)

imprimirPares()