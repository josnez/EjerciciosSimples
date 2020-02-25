import moduloOpe

def main():
	n1 = int(input("Digite el numero 1: \n"))
	n2 = int(input("Digite el numero 2: \n"))
	op = input("Digite la operacion: \n")
	if op=='-':
		print(modulo.resta(n1, n2))
	elif op=='+':
		print(modulo.suma(n1, n2))
	elif op=='*':
		print(modulo.multiplicacion(n1, n2))
	elif op=='/':
		print(modulo.division(n1, n2))

main()