def valorMaximo():
	lista = [12,32,5,13,68,1,123,78]
	max=0
	for i in lista:
		if i>max:
			max=i
	return lista.index(max)

print("La posicion del valor maximo de la lista es: " + str(valorMaximo()))