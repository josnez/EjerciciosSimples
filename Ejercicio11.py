def main():
	d = input("Digite un caracter: \n")
	esNum(d)

def esNum(n):
	try:
		nEntero = int(n)
		print("Es un numero entero")
	except ValueError:
		print("No es un numero entero")
main()
		