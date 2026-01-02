import math
import numpy as np
import matplotlib.pyplot as plt

def ConstroiMatriz(vetor_x, vetor_f,ponto_x):
    '''
    Essa funcao constroi a matriz triangular
    inferior, calculando o polinomio
    interpolador Pi,..,i+k (elemento de linha
    i+k e coluna k da matriz) a cada passo.

    Todos os polinomios ja sao calculados no ponto_x
    (Pi,..,i+k(ponto_x)). Ate que e obtido (e retornado pela
    funcao) o ultimo elemento da matriz (o polinomio de grau n
    que interpola x0,...,xn), tambem ja calculado no ponto_x.

    Recebe o vetor_ com os pontos [x0,...,xn] e
    o vetor_f com os pontos [f(x_0),f(x_1),...,f(x_n)].

    Retorna o polinomio interpolador calculado no ponto_x
    '''


    n=len(vetor_x)

    ar=np.zeros((n,n),float)


    i=0
    for f in vetor_f:
        ar[i][0]=f
        i+=1


    for col in range(1,n):
        for lin in range(col,n):
            ar[lin][col]=((ponto_x-vetor_x[lin-col])*ar[lin][col-1]-(ponto_x-vetor_x[lin])*ar[lin-1][col-1])/(vetor_x[lin]-vetor_x[lin-col])


    return ar[n-1][n-1] #Ultimo elemento da matriz



def f(x):
    '''
            Essa funcao calcula e retorna o
            valor de f no ponto x
    '''

    return #Insira aqui a funcao (para plotar o grafico)

def main():
    '''
               Essa funcao plota os graficos
               de P(x) e f(x)
    '''
    vetor_f=#Insira aqui o vetor [f(x0),f(x1),...,f(xn)]
    vetor_x=#Insira aqui o vetor [x0,x1,...,xn]

    pontosx_paraPlotar = []  # Esse e o vetor de pontos x para plotar os graficos
    pontosf_paraPlotar=[]  # Esse e o vetor de pontos f(x) para plotar os graficos
    pontosP_paraPlotar=[]  # Esse e o vetor de pontos P(x) para plotar os graficos
    delta=1/5000
    for i in range(-5000,5001):
        xi=i*delta
        pontosx_paraPlotar.append(xi)

        px=ConstroiMatriz(vetor_x,vetor_f,xi) #Calculando P(x)
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
