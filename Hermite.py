import numpy as np
import matplotlib.pyplot as plt

def coeficientes(vetor_x, vetor_f,vetor_derivadas_f):
    '''
    Essa funcao calcula os coeficientes do polinomio
    interpolador a partir das diferencas de Newton.
    Recebe o vetor_ com os pontos [x0,...,xn] e
    o vetor_f com os pontos [f(x_0),f(x_1),...,f(x_n)] e
    o vetor_derivadas_f com os pontos [f'(x_0),f'(x_1),...,f'(x_n)].
    Retorna um vetor com os coeficientes a0,...,an
    '''



    n=len(vetor_x)

    #Duplicando cada ponto xi
    vetor_x_duplicado=[]
    for i in range(n):
        vetor_x_duplicado.append(vetor_x[i])
        vetor_x_duplicado.append(vetor_x[i])

    ar=np.zeros((2*n,2*n),float)


    for i in range(2*n):
        if i%2==0:
            ar[i][0] = vetor_f[i//2]
        else:
            ar[i][0] = vetor_f[(i-1)//2]


    for col in range(1,2*n):
        for lin in range(col,2*n):
            if vetor_x_duplicado[lin]==vetor_x_duplicado[lin-col]:
                ar[lin][col] = vetor_derivadas_f[lin//2]
            else:
                    ar[lin][col]=(ar[lin][col-1]-ar[lin-1][col-
                    1])/(vetor_x_duplicado[lin]-vetor_x_duplicado[lin-col])

    diagonal=[]
    for q in range(2*n):
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

    return # Coloque aqui a funcao f

def derivada_f(x):
    '''
               Essa funcao calcula e retorna o
               valor da derivada f no ponto x
    '''
    return # Coloque aqui a expressao da derivada da f

def main():
    '''
               Essa funcao plota os graficos
               de P(x) e f(x)
    '''
    vetor_x=#Insira aqui o vetor np.array([x0,x1,...,xn])
    vetor_f = f(vetor_x)
    vetor_derivadas_f = derivada_f(vetor_x)
    diagonal=coeficientes(vetor_x,vetor_f,vetor_derivadas_f) #Vetor dos coeficientes [a0,a1,...,an]

    vetor_x_duplicado = []
    for i in range(len(vetor_x)):
        vetor_x_duplicado.append(vetor_x[i])
        vetor_x_duplicado.append(vetor_x[i])

    pontosx_paraPlotar = []  # Esse e o vetor de pontos x para plotar os graficos
    pontosf_paraPlotar=[]  # Esse e o vetor de pontos f(x) para plotar os graficos
    pontosP_paraPlotar=[]  # Esse e o vetor de pontos H(x) para plotar os graficos
    delta=1/5000
    for i in range(-10000,10001): # Para plotar o gráfico no intervalo [-2,2]
        xi=i*delta
        pontosx_paraPlotar.append(xi)

        px=constroiPolinomio(xi,vetor_x_duplicado,vetor_f,diagonal)
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
