import math

def f(x):
    return #Insira aqui a função f(x)

def main():
    n= #Insira aqui o valor de n
    a,b= #Insira aqui os valores de a,b do intervalo [a,b] que se quer integrar f(x)


    vetor_w=[] #Insira aqui os valores de wi da Tabela [w0,...,wn]
    vetor_x=[] #Insira aqui os valores de xi da Tabela [x0,...,xn]

    valor_quadratura=0

    for i in range(n+1):
        # Aplicando a transformação de variável
        t=((b-a)/2)*vetor_x[i]+(a+b)/2
        F_xi=((b-a)/2)*f(t)

        #Calculando a Fórmula da Quadratura
        valor_quadratura+=vetor_w[i]*F_xi

    print("Valor aproximado da Integral: ",valor_quadratura)
    print()
    Valor_real= #Insira aqui o valor real da Integral
    print("Erro exato: ",abs(valor_quadratura-Valor_real))


main()
