def numDig(n):
	if n>9 or n<-9:
		return 1+numDig(n/10)
	return 1


print("El numero tiene:  "+str(numDig(int(input("Digite un numero \n"))))+" digitos")