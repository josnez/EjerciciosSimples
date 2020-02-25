def sumaNum():
	cont=0
	j=0
	aux=0
	lista = []
	while cont!=20:
		if j%2==0:
			lista.append(j)
			cont+=1
		j+=1

	for i in lista:
		aux += i
	return aux

print("La suma de los numeros de la lista es: "+str(sumaNum()))