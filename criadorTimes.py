import numpy as np

'''
Exception criada para quando o nome inserido para o esporte é/contém um número
'''

class NomeInvalido(Exception):
        pass

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
    operacao_pos_esp_final = False

    while True:
        try: 
            print('Coletando informações gerais sobre o(s) jogo(s)')
           
            esporte = input('Digite o nome do esporte a ser jogado: ')
            if esporte.isnumeric:
                raise NomeInvalido
           
            n_times = input('Digite a quantidade de times a serem formados: ')
            n_times_int = int(n_times)
           
            n_jog = input('Digite a quatidade total de jogadores que participarão da partida: ')
            n_jog_int = int(n_jog)
        except NomeInvalido:
            print('Nome inserido é invalido!\n')
            continue
        except ValueError:
            print('Foi inserido um valor inválido! A operação será reiniciada\n')
            continue
        else:
            break
    
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
                    print('Quantidade inválida! Devem haver um jogador de posição especial por equipe,'\
                          ' caso hajam mais/menos considere que não há jogadores de posição especial.')
            case 'N':
                n_pos_esp_int = 0
                pos_esp = False
                operacao_pos_esp_final = True
            case _: 
                print('Valor inválido! Apenas "S" e "N" são aceitos como resposta!')
    
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
Função para posicionar os jogadores especiais em cada time

Essa função cria a lista que será composta com os times e será chamada apenas quando
existem jogadores em funções especiais.
Como existem 1 jogador especial para cada time, cada jogador é inserido em uma lista vazia
, a qual representa um time, e a mesma é inserida em outra que engloba todos os times.

Recebe a lista de times, o set de jogadores especiais e o número de times
Retorna a lista de times atualizada
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
Função para posicionar os demais jogadores em times

Aloca cada jogador no 'próximo' time até que seja percorrido todos os jogadores.
Caso não tenham jogadores especiais, faz-se necessário a criação das listas para cada time.

Recebe a lista de times (vazia ou não), set de jogadores, se tem ou não jogadores especiais e nº de times
Retorna a lista de times atualizada
'''

def define_times_jogadores(list_times: list, jogadores: set, tem_jog_esp: bool, n_times: int):
    lista_jogadores = list(jogadores)


    if tem_jog_esp is False:
        for _ in range(n_times):
            novo_time = []
            list_times.append(novo_time)
    
    i = 0
    extrai_jogador = (jog for jog in lista_jogadores)
    while True:
        if i == n_times:
            i = 0
        
        try:
            list_times[i].append(next(extrai_jogador))
        except StopIteration:
            break
        
        i += 1
    
    
    return list_times

'''
Função para definir os times com seus respectivos jogadores

Função que serve como "meio-campo" para as funções que constroem os times.

Recebe os sets de jogadores e número de times
Retorna lista de listas com os times
'''

def define_times(jogadores: set, jog_esp: set, tem_jog_esp: bool,n_times : int):
    lista_times = []
    tamanho_time = np.ceil((len(jogadores) + len(jog_esp)) / n_times)
    print(f'Tamanho times: {tamanho_time}')

    if tem_jog_esp:
        lista_times = define_times_jogadores_especiais(lista_times, jog_esp, n_times)
    
    lista_times = define_times_jogadores(lista_times, jogadores, tem_jog_esp, n_times)
    
    return lista_times
    ...

'''
Função principal
'''

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
    
    for time in times:
        print(time)

main()