import os
import json
from tabulate import tabulate

def nome_programa():
    '''
    Exibe o nome estilizado do programa.

    Inputs: Nenhum
    Outputs: Impressão do título do programa no console
    '''
    print('''
    █▀ ▄▀█ █▄▄ █▀█ █▀█   █▄▄ █▀█ ▄▀█ █▀ █ █░░ █▀▀ █ █▀█ █▀█
    ▄█ █▀█ █▄█ █▄█ █▀▄   █▄█ █▀▄ █▀█ ▄█ █ █▄▄ ██▄ █ █▀▄ █▄█\n''')


def menu():
    '''
    Exibe o menu principal de opções do sistema.

    Inputs: Nenhum
    Outputs: Impressão das opções do menu no console
    '''
    print('1 - Cadastrar Restaurante.')
    print('2 - Listar Restaurantes.')
    print('3 - Ativar/Desativar Restaurante.')
    print('4 - Sair.')


def escolher_opcao(restaurantes):
    '''
    Recebe a opção do usuário e executa a funcionalidade correspondente.

    Inputs:
        restaurantes (list): Lista dos restaurantes carregados
    Outputs: Nenhum (executa a opção escolhida)
    '''
    opcao_escolhida = input('\nEscolha sua opção: ')
    if not opcao_escolhida.isdigit():
        opcao_invalida(restaurantes)
        return

    opcao_escolhida = int(opcao_escolhida)

    match opcao_escolhida:
        case 1:
            cadastrar_restaurante(restaurantes)
        case 2:
            listar_restaurantes(restaurantes)
            input('\nAperte ENTER para continuar...')
        case 3:
            ativar_restaurante(restaurantes)
        case 4:
            finalizar_programa()
        case _:
            opcao_invalida(restaurantes)


def finalizar_programa():
    '''
    Finaliza o programa com uma mensagem de saída.

    Inputs: Nenhum
    Outputs: Encerra a execução do programa
    '''
    titulo('Saindo...', True, False)
    exit()


def opcao_invalida(restaurantes):
    '''
    Informa que a opção escolhida é inválida.

    Inputs:
        restaurantes (list): Lista de restaurantes (não usada diretamente)
    Outputs: Mensagem de erro exibida ao usuário
    '''
    titulo('Opção inválida!!!\n', True, False)
    input('\nAperte ENTER para continuar...')


def cadastrar_restaurante(restaurantes):
    '''
    Cadastra um novo restaurante no sistema.

    Inputs:
        restaurantes (list): Lista atual de restaurantes
    Outputs: Restaurante adicionado à lista e salvo no arquivo JSON
    '''
    titulo('Ｃａｄａｓｔｒｏ ｄｅ ｎｏｖｏｓ ｒｅｓｔａｕｒａｎｔｅｓ．\n', False, True)

    restaurante_atual = {
        'id': len(restaurantes) + 1,
        'nome': input('Informe o nome do restaurante a ser cadastrado: '),
        'categoria': input('Informe a categoria: '),
        'ativo': False        
    }

    restaurantes.append(restaurante_atual)
    salvar_restaurantes(restaurantes)

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'O restaurante "{restaurante_atual["nome"]}" foi cadastrado com sucesso!')
    input('\nAperte ENTER para continuar...')


def listar_restaurantes(restaurantes):
    '''
    Lista todos os restaurantes cadastrados no sistema.

    Inputs:
        restaurantes (list): Lista de restaurantes
    Outputs:
        bool: True se a lista foi exibida, False se estiver vazia
    '''
    titulo('Ｌｉｓｔａ ｄｅ Ｒｅｓｔａｕｒａｎｔｅｓ\n', False, True)

    if not restaurantes:
        print('Não há restaurantes cadastrados!')
        return False

    tabela = []
    for restaurante in restaurantes:
        status = 'Restaurante Ativo' if restaurante['ativo'] else 'Restaurante Inativo'
        tabela.append([
            restaurante['id'],
            restaurante['nome'],
            restaurante['categoria'],
            status
        ])

    cabecalhos = ['ID', 'NOME RESTAURANTE', 'CATEGORIA', 'STATUS']
    print(tabulate(tabela, headers=cabecalhos, tablefmt='fancy_grid'))
    return True


def titulo(texto, limpar_tela_antes, limpar_tela_depois):
    '''
    Exibe um título no console, com a opção de limpar a tela antes e/ou depois.

    Inputs:
        texto (str): Texto a ser exibido como título
        limpar_tela_antes (bool): Se True, limpa a tela antes de exibir
        limpar_tela_depois (bool): Se True, limpa a tela após exibir
    Outputs: Impressão do título no console
    '''
    if limpar_tela_antes: 
        os.system('cls' if os.name == 'nt' else 'clear')

    print(texto)

    if limpar_tela_depois: 
        os.system('cls' if os.name == 'nt' else 'clear')


def ativar_restaurante(restaurantes):
    '''
    Alterna o status (ativo/inativo) de um restaurante.

    Inputs:
        restaurantes (list): Lista de restaurantes
    Outputs: Atualiza o status do restaurante e salva as alterações
    '''
    titulo('Ａｔｉｖａｒ／Ｄｅｓａｔｉｖａｒ Ｒｅｓｔａｕｒａｎｔｅ．', True, False)

    if not listar_restaurantes(restaurantes):
        input('\nAperte ENTER para continuar...')
        return

    restaurante_atual = obter_restaurante_por_id(restaurantes)
    if not restaurante_atual:
        titulo('Restaurante com ID inválido ou não encontrado.', True, False)
        input('\nAperte ENTER para continuar...')
        return

    alternar_status(restaurante_atual, restaurantes)
    input('\nAperte ENTER para continuar...')


def obter_restaurante_por_id(restaurantes):
    '''
    Obtém um restaurante com base no ID informado pelo usuário.

    Inputs:
        restaurantes (list): Lista de restaurantes
    Outputs:
        dict | None: Restaurante encontrado ou None se inválido
    '''
    try:
        id_desejado = int(input('Digite o ID do restaurante: '))
    except ValueError:
        return None

    for r in restaurantes:
        if r['id'] == id_desejado:
            return r
    return None


def alternar_status(restaurante,lista_restaurantes):
    '''
    Altera o status de ativo para inativo ou vice-versa.

    Inputs:
        restaurante (dict): Restaurante a ser alterado
    Outputs: Status do restaurante modificado e salvo
    '''
    status_atual = 'ativo' if restaurante['ativo'] else 'inativo'
    acao = 'desativar' if restaurante['ativo'] else 'ativar'
    acao2 = 'desativado' if restaurante['ativo'] else 'ativado'

    titulo(f'O restaurante "{restaurante["nome"]}" está atualmente {status_atual}.', True, False)
    resposta = perguntar_sim_nao(f'\nDeseja {acao} este restaurante? (s/n): ')

    if resposta == 's':
        restaurante['ativo'] = not restaurante['ativo']
        salvar_restaurantes(lista_restaurantes)
        titulo(f'Restaurante {acao2} com sucesso!', True, False)
    else:
        titulo('Nenhuma alteração realizada.', True, False)


def perguntar_sim_nao(mensagem):
    '''
    Solicita uma confirmação do usuário (s/n).

    Inputs:
        mensagem (str): Mensagem a ser exibida ao usuário
    Outputs:
        str: 's' para sim ou 'n' para não
    '''
    while True:
        resposta = input(mensagem).strip().lower()
        if resposta in ['s', 'n']:
            return resposta
        else:
            titulo('Opção inválida! Digite "s" para sim ou "n" para não.', True, False)


def main(restaurantes):
    '''
    Função principal do programa.

    Inputs:
        restaurantes (list): Lista de restaurantes carregados
    Outputs: Executa o menu interativo do sistema
    '''
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        nome_programa()
        menu()
        escolher_opcao(restaurantes)


def salvar_restaurantes(restaurantes, caminho='restaurantes.json'):
    '''
    Salva a lista de restaurantes em um arquivo JSON.

    Inputs:
        restaurantes (list): Lista de restaurantes
        caminho (str): Caminho do arquivo JSON
    Outputs: Arquivo JSON atualizado com os dados
    '''
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(restaurantes, f, ensure_ascii=False, indent=4)


def carregar_restaurantes(caminho='restaurantes.json'):
    '''
    Carrega a lista de restaurantes de um arquivo JSON.

    Inputs:
        caminho (str): Caminho do arquivo JSON
    Outputs:
        list: Lista de restaurantes carregados ou vazia
    '''
    if os.path.exists(caminho):
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


if __name__ == '__main__':
    restaurantes = carregar_restaurantes()
    main(restaurantes)
