#Essa função procura um intervalo [a, b] onde uma função f(x) muda de sinal — ou seja, onde há pelo menos uma raiz de f(x) (um valor x tal que f(x) = 0) entre a e b.

def buscaInt(a,h,xmax,f):
    b = a + h
    
    while b <= xmax:
        if f(a) * f(b) < 0:
            return a,b
        a = b
        b = a + h