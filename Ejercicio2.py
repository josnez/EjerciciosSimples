#5. Escribir un programa que calcule el área de un triángulo, capturando los valores de base y
#altura.

def main():
    b = input("Digite la base: ")
    a = input("Digite la altura: ")
    print(area(int(b), int(a)))

def area(base, altura):
    return (base * altura)/2;

main()