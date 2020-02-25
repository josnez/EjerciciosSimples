import time
def main():
    h = int(input("Digite las horas: \n"))
    m = int(input("Digite los minutos: \n"))
    s = int(input("Digite los segundos: \n"))
    auxH = 0
    auxM = 0
    auxS = 0

    while(auxH!=h or auxM!=m or auxS!=s):
        if auxS<61:
            auxS+=1
            time.sleep(1)
            imprimir(auxH, auxM, auxS)
        else:
            auxS=0
            if(auxM<61):
                auxM+=1
                imprimir(auxH, auxM, auxS)
            else:
                auxM=0
                if auxH<20:
                    auxH+=1
                    imprimir(auxH, auxM, auxS)

def imprimir(h, m, s):
    print("Horas: "+str(h) + " Minutos: " + str(m) + " Segundos: " + str(s))

main()
