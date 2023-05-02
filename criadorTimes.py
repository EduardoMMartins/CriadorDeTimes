import numpy as np

'''
Função para coletar informações sobre os times a serem montados
    - Esporte
    - Quantidade de times
    - Número total de jogadores
    - Presença e quantidade de posições especiais (Goleiro/Líbero)

Não recebe parâmetros
Retorna cada informação para a função main
'''

def coleta_informacoes():
    print('Coletando informações gerais sobre o(s) jogo(s)')
    operacao_pos_esp_final = False

    esporte = input('Digite o nome do esporte a ser jogado: ')
    n_times = input('Digite a quantidade de times a serem formados: ')
    n_times_int = int(n_times)
    n_jog = input('Digite a quatidade total de jogadores que participarão da partida: ')
    n_jog_int = int(n_jog)
    
    while operacao_pos_esp_final == False:
        pos_esp = input('Haverão jogadores em posição especial para cada time (goleiro/líbero) - [S]im ou [N]ão: ')

        match pos_esp:
            case 'S':
                n_pos_esp = input('Haverão quantos jogadores de posição especial: ')
                n_pos_esp_int = int(n_pos_esp)
                if n_pos_esp_int == n_times_int:
                    pos_esp = True
                    operacao_pos_esp_final = True
                else:
                    print('Número inválido')
            case 'N':
                n_pos_esp_int = 0
                pos_esp = False
                operacao_pos_esp_final = True
            case _: 
                print('Valor inválido')
    
    return esporte, n_times_int, n_jog_int, pos_esp, n_pos_esp_int


'''
Função para coletar os todos jogadores que participarão da partida

Recebe parâmetros de qntd de jogadores, se tem jogador de posição especial e sua qntd 
Retorna um set com jogadores e outro set com posições especiais
'''

def coleta_jogadores(qtd_jogadores: int, tem_jog_esp : bool, qtd_pos_esp: int):
    i = 0
    set_jogadores = set()
    set_jog_pos_esp = set()

    if tem_jog_esp:
        print('Coletando inscrição jogadores de posições especiais:')
        for i in range(qtd_pos_esp):
            jogador = input(f'Digite o nome do jogador de posição especial [{i+1}]: ')
            set_jog_pos_esp.add(jogador)
    
    i = 0
    print('\nColetando inscrição dos demais jogadores:')
    for i in range(qtd_jogadores - qtd_pos_esp):
        jogador = input(f'Digite o nome do jogador [{i+1}]: ')
        set_jogadores.add(jogador)
    
    return set_jogadores, set_jog_pos_esp

'''

'''

def define_times_jogadores_especiais(lista_times : list, jog_esp : set, n_times : int):
    lista_jog_esp = list(jog_esp)

    for time in range(n_times):
        novo_time = []
        novo_time.append(lista_jog_esp[time])
        lista_times.append(novo_time)
    
    return lista_times
    ...

'''

'''

def define_times_jogadores(list_times: list):...

'''
Função para definir os times com seus respectivos jogadores

Recebe os sets de jogadores e número de times
Retorna lista de listas com os times
'''

def define_times(jogadores: set, jog_esp: set, tem_jog_esp: bool,n_times : int):
    lista_times = []
    tamanho_time = np.ceil((len(jogadores) + len(jog_esp)) / n_times)
    print(f'Tamanho times: {tamanho_time}')

    if tem_jog_esp:
        lista_times = define_times_jogadores_especiais(lista_times, jog_esp, n_times)
    
    lista_times = ...
    
    return lista_times
    ...

def main():
    
    print('Montando as equipes para o(s) jogo(s)\n')
    esporte, n_times, n_jog, tem_jog_esp, n_jog_esp = coleta_informacoes()

    print('\nInformações sobre o(s) jogo(s):')
    print(f'Esporte: {esporte}')
    print(f'Número de times: {n_times}')
    print(f'Número de jogadores: {n_jog}')
    print(f'Apresenta jogadores especiais: {tem_jog_esp}')
    print(f'Número de jogadores especiais: {n_jog_esp}\n')

    jogadores,jogadores_especiais = coleta_jogadores(n_jog, tem_jog_esp, n_jog_esp)
    print('Jogadores inscritos:')
    for jogador in jogadores:
        print(jogador)
    for jog_esp in jogadores_especiais:
        print(jog_esp)
    
    times = define_times(jogadores, jogadores_especiais, tem_jog_esp, n_times)
    print('\n', times)
    ...

main()