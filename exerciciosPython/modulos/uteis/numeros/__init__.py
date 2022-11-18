def fatorial(n):
    f = 1
    for c in range(1,n+1):
        f *= c
    return f


def metade(n):
    return n/2


def dobro(n):
    return n*2


def diminui(n, p, formato=False):
    res = n-((n*p)/100)
    return res if formato is False else moeda(res) 

def aumenta(n, p):
    return n+((n*p)/100)

def moeda(n):
    return f"R$ {n:.2f}".replace('.',',')