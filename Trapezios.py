import math
def Formula_nTrapezios(vetor_f,h):
    '''
      Essa função recebe o vetor_f=[f(x0),...,f(xn)] e o valor
      de h=(b-a)/n.
      Retornando o valor aproximado da integral de f
      Obtido ao utilizar a Fórmula dos n-Trapézios.
    '''
    n=len(vetor_f)-1
    soma=vetor_f[0]/2+vetor_f[n]/2

    for i in range(1,n):
        soma+=vetor_f[i]

    return soma*h

def f(x):
    '''
      Essa função recebe o valor x
      e retorna o valor de f(x)
    '''

    return #Inisira aqui a função f(x)

def estimativa_erro(a,b,h):
    '''
          Essa função calcula a estimativa
          de erro para o Método dos Trapézios

          Recebe h=(b-a)/n e os valores a , b
          Retorna: A estimativa de erro
    '''
    M2= #Insira aqui o valor de M2=max|f''(t)|
    return M2**(b-a)*(h**2)/12
def main():
    '''
         Essa função é responsável
         por mostrar os resultados
         obtidos
    '''
    a,b= #Insira aqui os valores a,b do intervalo [a,b] que se quer integrar f(x)
    n= #Insira aqui o valor de n
    vetor_x=[] #Vetor de pontos xi igualmente espaçados [x0,...,xn]
    vetor_f=[] #Vetor [f(x0),...,f(xn)]

    h=(b-a)/n
    for k in range(n+1):
        xi=a+k*h
        vetor_x.append(xi)
        vetor_f.append(f(xi))

    Integral=Formula_nTrapezios(vetor_f,h)
    print("Integral Aproximada: ", Integral)

    valor_exato= #Insira aqui o valor exato da Integral
    erro_exato = abs(Integral - valor_exato)
    print("Erro Exato: ",erro_exato)

    erro_estimado=estimativa_erro(a,b,h)
    print("Estimativa de Erro: ", erro_estimado)


main()
