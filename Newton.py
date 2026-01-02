import math
import numpy as np
import matplotlib.pyplot as plt

def coeficientes(vetor_x, vetor_f):
    '''
    Essa funcao calcula os coeficientes do polinomio
    interpolador a partir das diferencas de Newton.
    Recebe o vetor_ com os pontos [x0,...,xn] e
    o vetor_f com os pontos [f(x_0),f(x_1),...,f(x_n)].
    Retorna um vetor com os coeficientes a0,...,an
    '''


    n=len(vetor_x)

    ar=np.zeros((n,n),float)


    i=0
    for f in vetor_f:
        ar[i][0]=f
        i+=1


    for col in range(1,n):
        for lin in range(col,n):
            ar[lin][col]=(ar[lin][col-1]-ar[lin-1][col-
            1])/(vetor_x[lin]-vetor_x[lin-col])

    diagonal=[]
    for q in range(n):
        diagonal.append(ar[q][q])
    return diagonal

def constroiPolinomio(x,vetor_x, vetor_f, coeficientes):
    '''
        Essa funcao constroi o polinomio interpolador P,
        ja calculado no ponto x.

        Recebe: O ponto x para se calcular P(x), o vetor_x=[x0,...,xn] ,
        o vetor_f=[f(x_0),f(x_1),...,f(x_n)] e o vetor
        coeficientes=[a0,a1,...,an].

        Retorna: O valor de P(x)
    '''

    P_x=vetor_f[0]
    for i in range(1,len(vetor_x)):
        polinomio=1
        for k in range(i):
            polinomio*=x-vetor_x[k]
        P_x+=polinomio*coeficientes[i]

    return P_x

def f(x):
    '''
            Essa funcao calcula e retorna o
            valor de f no ponto x
    '''

    return math.e**x

def main():
    '''
               Essa funcao plota os graficos
               de P(x) e f(x)
    '''
    vetor_f=#Insira aqui o vetor [f(x0),f(x1),...,f(xn)]
    vetor_x=#Insira aqui o vetor [x0,x1,...,xn]
    diagonal=coeficientes(vetor_x,vetor_f) #Vetor dos coeficientes [a0,a1,...,an]

    pontosx_paraPlotar = []  # Esse e o vetor de pontos x para plotar os graficos
    pontosf_paraPlotar=[]  # Esse e o vetor de pontos f(x) para plotar os graficos
    pontosP_paraPlotar=[]  # Esse e o vetor de pontos P(x) para plotar os graficos
    delta=1/10000
    for i in range(10001):
        xi=i*delta
        pontosx_paraPlotar.append(xi)

        px=constroiPolinomio(xi,vetor_x,vetor_f,diagonal)
        pontosP_paraPlotar.append(px)

        pontosf_paraPlotar.append(f(xi))


    #Plotando os graficos
    plt.plot(pontosx_paraPlotar, pontosf_paraPlotar, label="f(x)", color="blue")
    plt.plot(pontosx_paraPlotar, pontosP_paraPlotar, label="P(x)", color="green")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.title("Interpolacao Polinomial")
    plt.grid(True)
    plt.show()

main()
