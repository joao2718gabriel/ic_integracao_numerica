import math
def constroiBase(pontos, ponto_x):
    '''
        Essa funcao calcula e retorna a base B={L0,..Ln} de Pn.

        Recebe: Os vetores pontos=[x0,x1,..,xn]
        e ponto_x=Valor que se quer calcular (P(ponto_x))
        Retorna: A base B={L0,..Ln} de Pn na forma do 
        vetor B=[L0,..,Ln] onde cada Li
        ja esta calculado no ponto_x
    '''

    n = len(pontos)
    B = []
    for k in range(n):
        Lk = 1
        for i in range(n):
            if i != k:
                Lk *= (ponto_x - pontos[i]) / (pontos[k] - pontos[i])
        B.append(Lk)

    return B

def erro(resultado, pontos, ponto_x):
    '''
               Essa funcao calcula e retorna o erro f(x)-P(x), juntamente
               com o resultado teorico.

               Recebe: resultado=O resultado de P(ponto_x),o vetor pontos=[x0,...,nx]
               e o ponto_x (O ponto no qual se quer calcular P(ponto_x))
               Retorna: O erro f(x)-P(x) e o resultado teorico.
    '''

    valor_f =  # Insira aqui o valor de f(ponto_x)
    Erro_simulacao = valor_f - resultado

    pi_x = 1
    for ponto in pontos:
        pi_x *= ponto_x - ponto
    n = len(pontos)
    M =  # Insira aqui o valor de max da (n+1)-esima derivada de f
    Erro_Teorico = M / math.factorial(n).pi_x

    return Erro_simulacao, Erro_Teorico

def main(ponto_x):
    '''
                  Essa funcao fornece o output final,
                  calculando o Polinomio Interpolador em alguns pontos
                  pre-definidos e realizando as comparacoess necessarias com
                  a funcao f que foi aproximada.
                  
                  Recebe: O ponto_x para se calcular P(ponto_x)
                  Retorna: O output final
    '''
    pontos =  # Insira aqui o vetor pontos=[x0,..xn]
    pontos_f =  # Insira aqui o vetor pontos_f=[f(x0),...,f(xn)]
    

    B = constroiBase(pontos, ponto_x)
    P_x = 0

    for i in range(len(pontos)):
        P_x += B[i] * pontos_f

    Erros = erro(P_x, pontos, ponto_x)


    print("*************************************")
    print("RESULTADOS")
    print(f"Valor de P calculado no ponto {ponto_x}: {P_x}")
    print(f"Erro_simulacao: f(x)-P(x) = {Erros[0]}")
    print(f"Erro_Teorico:  {abs(Erros[1])}")
    print(f"Note ainda que, de fato: |f(x)-P(x)|
    <=Erro_Teorico: {abs(Erros[0])}<={abs(Erros[1])}")
    print("\n")


pontos_x=#Insira aqui o vetor [x1,x2,x3,...] de pontos para calcular P(x)

for ponto in pontos_x:
    main(ponto)
