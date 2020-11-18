#conjnto caminhões
#A posição do peso no vetor representa a capacidade de cada caminhão
T = [5]

#peso dos itens, a posição deste vetor reflete no lucro do vetor V
G = [2,3,4]

#Lucro por item, a posição do lucro reflete o peso no vetor G
V = [3,4,5]


def main():
    for i in range(len(T)):
        pesoLimite = T[i]
        result = mochila(G,V,pesoLimite)
        print(result)

def mochila(itens, valor, W):
    n = len(itens)
    M = [[0 for x in range(W+1)] for x in range(n+1)]

    for i in range( n+1):
        for w in range( W+1 ):
            if i == 0 or w == 0: 
                M[i][w] = 0
            elif(w < itens[i-1] ):
                M[i][w] = M[i-1][w]
            else:
                lstTemp = [M[i-1][w], valor[i-1]+ M[i-1][w-itens[i-1]]]
                M[i][w] = max( lstTemp )
    return M[n][W]

if __name__ == "__main__":
    main()