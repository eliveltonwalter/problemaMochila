#conjnto caminhões
#A posição do peso no vetor representa a capacidade de cada caminhão
T = [23]

#peso dos itens, a posição deste vetor reflete no lucro do vetor V
G = [1,2,5,6,7,9,11]

#Lucro por item, a posição do lucro reflete o peso no vetor G
V = [1, 6, 18, 22, 28, 40, 60]


def main():
    lstAllItens = []
    copyG = G
    copyV = V
    maxProfit = 0
    for i in range(len(T)):
        pesoLimite = T[i]
        tmpMaxProfit, M = mochila(copyG, copyV, pesoLimite)
        maxProfit += tmpMaxProfit
        lstItens = getIncludedItens(M, copyG, pesoLimite)
        lstAllItens.extend(lstItens)
        copyG = removeValueFromUsedItem(copyG, list(lstItens), True)
        copyV = removeValueFromUsedItem(copyV, list(lstItens), False)
    #print('Itens incluidos: ')
    #print(lstAllItens)
    #print('valor máximo: '+str(maxProfit))
    print('Itens não incluidos: ')
    print(getNotIncludedItens(copyG))
    print('Lucro perdido: ' + str(sum(copyV)))

#lstAllItens: todos os itens do problema;
#lstIncludedItem: itens já incluidos no caminhião;
#weight boolean para verificar se é valor ou peso para preencher
def removeValueFromUsedItem(lstAllItens, lstIncludedItem, weight):
    for i in lstIncludedItem:
        if(weight):
            lstAllItens[i] = 9999
        else:
            lstAllItens[i] = 0
    return lstAllItens

#Verifica quais itens não foram enviados baseado em seu peso, colocado método removeValueFromUsedItem
def getNotIncludedItens(lstAllItens):
    lstNotIncluded = []
    for i in range( len( lstAllItens ) ):
        if( lstAllItens[i] != 9999 ):
            lstNotIncluded.append(i)
    return lstNotIncluded

#Pega os itens adicionados no caminhão, baseado na mudança do seu valor entre cada linha da matriz,
#A diferença no valor da linha reflete que foi adicionado o item
def getIncludedItens(M, G, pesoLimite):
    i = len(G)
    j = pesoLimite
    lstIncludedItem = []
    while( i > 0 and j > 0 ):
        correctIndex = i - 1
        if(M[i][j] != M[correctIndex][j]):
            lstIncludedItem.append(correctIndex)
            j -= G[correctIndex]
            i -=1
        else:
            i -=1
    return lstIncludedItem

#algoritmo da mochila, baseado no algoritmo 41, da página 138 das anotações da disciplina
def mochila(itens, valor, W):
    n = len(itens)
    M = [[0 for x in range(W+1)] for x in range(n+1)]

    for i in range( n+1 ):
        for w in range( W+1 ):
            a = M[i-1][w]
            if i == 0 or w == 0: 
                M[i][w] = 0
            elif(w < itens[i-1] ):
                M[i][w] = a
            else:
                b = valor[i-1]+ M[i-1][w-itens[i-1]]
                lstTemp = [a, b]
                maxAB = max( lstTemp )
                M[i][w] = maxAB

    return M[n][W], M

if __name__ == "__main__":
    main()