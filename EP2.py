# EP2 - Define Posições(Ex1)
def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    soma_linha = 1
    soma_coluna = 1
    for i in range(tamanho):
        posicoes.append([])
    posicoes[0].insert(0,linha)
    posicoes[0].insert(1,coluna)
    if orientacao == 'vertical':
        for e in range(1, len(posicoes)):
            posicoes[e].insert(1,coluna)
            posicoes[e].insert(0, linha + soma_linha)
            soma_linha += 1
    if orientacao == 'horizontal':
        for e in range(1, len(posicoes)):
            posicoes[e].insert(0,linha)
            posicoes[e].insert(1, coluna + soma_coluna)
            soma_coluna += 1
    return posicoes



#Ep2 - Preenche Frota(Ex2)


def preenche_frota(frota,nome_navio,linha,coluna,orientacao,tamanho):
    if nome_navio not in frota:
        frota[nome_navio] = []
    
    frota[nome_navio].append(define_posicoes(linha, coluna, orientacao, tamanho))  

    return frota  
    
# Ep2 - Faz jogada(Ex3)

def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna] == 0: 
        tabuleiro[linha][coluna] = '-'
    elif tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'

    return tabuleiro