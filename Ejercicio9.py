def elimBlan():
	cadenaOriginal = "Hola soy una cadena de caracteres"
	cadenaTransfor = ""
	for i in cadenaOriginal:
		if i != ' ':
			cadenaTransfor += i
	return cadenaTransfor

print(elimBlan())