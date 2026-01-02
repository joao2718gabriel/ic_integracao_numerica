import math
def Formula_nSimpsons(vetor_f,h):
    '''
      Essa função recebe o vetor_f=[f(x0),...,f(xn)] e o valor
      de h=(b-a)/(2n).
      Retornando o valor aproximado da integral de f
      Obtido ao utilizar a Fórmula dos n-Trapézios.
    '''
    m=len(vetor_f)-1 #m=2n
    soma=vetor_f[0]+vetor_f[m]

    for i in range(1,m):
        if i%2==0:
            soma+=2*vetor_f[i]
        else:
            soma+=4*vetor_f[i]

    return soma*h/3

def f(x):
    '''
      Essa função recebe o valor x
      e retorna o valor de f(x)
    '''

    return #Insira aqui a função f(x)

def estimativa_erro(a,b,h):
    '''
          Essa função calcula a estimativa
          de erro para o Método de Simpson

          Recebe h=(b-a)/(2n) e os valores a , b
          Retorna: A estimativa de erro
    '''
    M4= #Insira aqui o valor de M4=max|f''''(t)|
    return M4*(b-a)*(h**4)/180
def main():
    '''
         Essa função é responsável
         por mostrar os resultados
         obtidos
    '''

    a, b = # Insira aqui os valores a,b do intervalo [a,b] que se quer integrar f(x)
    n =  # Insira aqui o valor de n
    vetor_x = []  # Vetor de pontos xi igualmente espaçados [x0,...,x2n]
    vetor_f = []  # Vetor [f(x0),...,f(x2n)]

    h = (b - a) / (2*n)
    for k in range(2*n + 1):
        xi = a + k * h
        vetor_x.append(xi)
        vetor_f.append(f(xi))
    Integral = Formula_nSimpsons(vetor_f, h)
    print("Integral Aproximada: ", Integral)
    valor_exato = # Insira aqui o valor exato da Integral
    erro_exato = abs(Integral - valor_exato)
    print("Erro Exato: ", erro_exato)

    erro_estimado = estimativa_erro(a, b, h)
    print("Estimativa de Erro: ", erro_estimado)


main()
