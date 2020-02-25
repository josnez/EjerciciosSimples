def main():
	n = int(input("Digite un numero: "))
	print(op(n))

def op(n):
	return cuandrado(n)-doble(n)

def cuandrado(n):
	return n*n

def doble(n):
	return n+n

main()