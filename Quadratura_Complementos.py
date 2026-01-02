import math

def main():
    n=#Insira aqui o valor de n
    Quadratura=0
    a,b=-math.pi/2,math.pi/2

    vetor_x=[]
    h=(b-a)/n

    for i in range(n):
        xi=a+i*h
        xi1=a+(i+1)*h


        num=2*(math.cos(xi)-math.cos(xi1))
        den=xi+xi1
        Quadratura+=num/den

    print("Valor aproximado: ", Quadratura)
    print()
    Valor_real=2.7415243363
    print("Erro exato: ", abs(Valor_real-Quadratura))

main()
