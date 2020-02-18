#16. Escribir un programa que detecte si un número introducido desde el teclado es positivo o
#negativo.
def signo():
    num = int(input("Digite un numero: "))
    if num == 0:
        print("El numero es 0")
    elif num < 0:
        print("El numero es negativo")
    elif num > 0:
        print("El numero es positivo")

signo();