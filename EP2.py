# EP2 - Define Posições
def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    soma_linha = 1
    soma_coluna = 1
    for i in range(tamanho):
        posicoes.append([])
    posicoes[0].insert(0,linha)
    posicoes[0].insert(1,coluna)
    if orientacao == 'vertical':
        for e in range(len(posicoes)):
            posicoes[e+1].insert(1,coluna)
            posicoes[e+1].insert(0, linha + soma_linha)
            soma_linha += 1
    if orientacao == 'horizontal':
        for e in range(len(posicoes)):
            posicoes[e+1].insert(0,linha)
            posicoes[e+1].insert(1, coluna + soma_coluna)
            soma_coluna += 1
    return posicoes

x = define_posicoes(2, 4, 'vertical', 3)
print(x)
