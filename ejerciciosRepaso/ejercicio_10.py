numero=int(input("Inserte el numero: "))
factorial=1
if numero!=0:
    for i in range(1, numero+1):
        factorial = factorial * i
print(f"El factorial es: {factorial}")