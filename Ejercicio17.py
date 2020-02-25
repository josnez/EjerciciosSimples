ruta = 'D:/Documentos/Uni/EjerciciosSimples/ASCII.txt'
archivo = open(ruta, 'w')

for i in range (32, 255):
	print(chr(i))
	archivo.write(chr(i))

archivo.close()