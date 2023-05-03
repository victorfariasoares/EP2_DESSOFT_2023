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

    return frota #volta um dicionario com o nome do navio sendo a chave e suas posições em listas

    
# Ep2 - Faz jogada(Ex3)
def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna] == 0: 
        tabuleiro[linha][coluna] = '-'
    elif tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'

    return tabuleiro


# EP2 - Posiciona Frota (ex4)
def posiciona_frota(frota): #Aqui vai entrar como argumento o que retornamos no ex2 (preenche frota)
    tabuleiro = [[0 for coluna in range(10)] for linha in range(10)]
    for nome_navio in frota:
        for lista_de_coordenadas in frota[nome_navio]:
            for coordenada in lista_de_coordenadas:
                x, y = coordenada
                tabuleiro[x][y] = 1
    return tabuleiro


#EP2 - Quantas embarcações afundadas (Ex5)
def afundados(frota, tabuleiro):
    navios_afundados = 0
    navio_afundado = False
    for nome_navio in frota.values():
        for lista_de_coordenadas in nome_navio:
            for coordenada in lista_de_coordenadas:
                if tabuleiro[coordenada[0]][coordenada[1]] == 'X':
                    navio_afundado = True
                else:
                    navio_afundado = False
                    break
            if navio_afundado == True:
                navios_afundados += 1
    return navios_afundados


#EP2 - Posição Válida (Ex6)
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    lista_vazia = []
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    for nome_navio in frota:
        for lista_de_coordenadas in frota[nome_navio]:
            for coordenada in lista_de_coordenadas:
                lista_vazia.append(coordenada)
    for posicao in posicoes:
        if posicao[0] not in range(10) or posicao[1] not in range(10):
            return False
        if posicao in lista_vazia:
            return False
    
    return True


#EP2 - Posicionando Frota (Ex5)
dicio_de_infos = {'porta-aviões': {'quantidade': 1, 'tamanho': 4},
 'navio-tanque': {'quantidade': 2, 'tamanho': 3}, 
 'contratorpedeiro': {'quantidade': 3, 'tamanho': 2},
'submarino': {'quantidade': 4, 'tamanho': 1}}

frota = {}

for nomes, info in dicio_de_infos.items():
    lista = []
    i = 0
    while i < dicio_de_infos [nomes]['quantidade']:
        tamanho = info['tamanho']
        if nomes != 'submarino':
            print(f'Insira as informações referentes ao navio {nomes} que possui tamanho {tamanho}')
            linha =int(input('Digite a linha da embarcação: '))
            coluna = int(input('Digite a coluna da embarcação: '))
            orientacao = int(input('Digite a orientação da embarcação. > [1] Vertical [2] Horizontal '))
            if orientacao == 1:
                orientacao = 'vertical'
            elif orientacao == 2:
                orientacao = 'horizontal'
        if nomes == 'submarino': 
            print(f'Insira as informações referentes ao navio {nomes} que possui tamanho {tamanho}')
            linha = int(input('Digite a linha da embarcação '))
            coluna = int(input('Digite a coluna da embarcação '))
        if posicao_valida(frota, linha, coluna, orientacao, tamanho) == True:
            i+=1
            lista.append(define_posicoes(linha, coluna, orientacao, tamanho))
            frota[nomes] = lista
            
        elif posicao_valida(frota, linha, coluna, orientacao, tamanho) == False:
            print('Esta posição não está válida!')
print(frota)


