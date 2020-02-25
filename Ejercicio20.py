def main():
    h = int(input("Digite las horas: \n"))
    m = int(input("Digite los minutos: \n"))
    s = int(input("Digite los segundos: \n"))

    imprimir(h, m, s)
    while(h!=0 or m!=0 or s!=0):
        if s > 0 and s < 61:
            s-=1
            imprimir(h, m, s)
        else:
            s=60
            if m > 0 and m < 61:
                m -= 1
                imprimir(h, m, s)
            else:
                m=60
                if h>0 and h<20:
                    h-=1
                    imprimir(h, m, s)


def imprimir(h, m, s):
    print("Horas: "+str(h) + " Minutos: " + str(m) + " Segundos: " + str(s))

main()