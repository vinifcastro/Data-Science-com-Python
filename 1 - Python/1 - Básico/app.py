import os
import json

def nome_programa():
    print('''
    █▀ ▄▀█ █▄▄ █▀█ █▀█   █▄▄ █▀█ ▄▀█ █▀ █ █░░ █▀▀ █ █▀█ █▀█
    ▄█ █▀█ █▄█ █▄█ █▀▄   █▄█ █▀▄ █▀█ ▄█ █ █▄▄ ██▄ █ █▀▄ █▄█\n''')

def menu():
    print('1 - Cadastrar Restaurante.')
    print('2 - Listar Restaurantes.')
    print('3 - Ativar/Desativar Restaurante.')
    print('4 - Sair.')

def escolher_opcao(restaurantes):
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
    titulo('Saindo...', True, False)
    exit()

def opcao_invalida(restaurantes):
    titulo('Opção inválida!!!\n', True, False)
    input('\nAperte ENTER para continuar...')

def cadastrar_restaurante(restaurantes):
    titulo('Ｃａｄａｓｔｒｏ ｄｅ ｎｏｖｏｓ ｒｅｓｔａｕｒａｎｔｅｓ．\n', False, True)

    restaurante_atual = {
        'id': len(restaurantes) + 1,
        'nome': input('Informe o nome do restaurante a ser cadastrado: '),
        'categoria': input('Informe a categoria: '),
        'ativo': False        
    }

    restaurantes.append(restaurante_atual)
    salvar_restaurantes(restaurantes)

    os.system('cls')
    print(f'O restaurante "{restaurante_atual["nome"]}" foi cadastrado com sucesso!')
    input('\nAperte ENTER para continuar...')

def listar_restaurantes(restaurantes):
    titulo('Ｌｉｓｔａ ｄｅ Ｒｅｓｔａｕｒａｎｔｅｓ\n', False, True)

    if len(restaurantes) == 0:
        print('Não há restaurantes cadastrados!')
        return False
    else:
        for restaurante in restaurantes:
            id_atual = str(restaurante['id'])
            nome_atual = restaurante['nome']
            categoria_atual = restaurante['categoria']
            ativo = 'Restaurante Ativo' if restaurante['ativo'] else 'Restaurante Inativo'
            print(f'{id_atual.center(6)} | {nome_atual.center(22)} | {categoria_atual.center(22)} | {ativo.center(22)} |')
    return True

def titulo(texto, limpar_tela_antes, limpar_tela_depois):
    if limpar_tela_antes: 
        os.system('cls' if os.name == 'nt' else 'clear')

    print(texto)

    if limpar_tela_depois: 
        os.system('cls' if os.name == 'nt' else 'clear')

def ativar_restaurante(restaurantes):
    titulo('Ａｔｉｖａｒ／Ｄｅｓａｔｉｖａｒ Ｒｅｓｔａｕｒａｎｔｅ．', True, False)

    if not listar_restaurantes(restaurantes):
        input('\nAperte ENTER para continuar...')
        return

    restaurante = obter_restaurante_por_id(restaurantes)
    if not restaurante:
        titulo('Restaurante com ID inválido ou não encontrado.', True, False)
        input('\nAperte ENTER para continuar...')
        return

    alternar_status(restaurante)
    input('\nAperte ENTER para continuar...')

def obter_restaurante_por_id(restaurantes):
    try:
        id_desejado = int(input('Digite o ID do restaurante: '))
    except ValueError:
        return None

    for r in restaurantes:
        if r['id'] == id_desejado:
            return r
    return None

def alternar_status(restaurante):
    status_atual = 'ativo' if restaurante['ativo'] else 'inativo'
    acao = 'desativar' if restaurante['ativo'] else 'ativar'
    acao2 = 'desativado' if restaurante['ativo'] else 'ativado'

    titulo(f'O restaurante "{restaurante["nome"]}" está atualmente {status_atual}.',True, False)
    resposta = perguntar_sim_nao(f'\nDeseja {acao} este restaurante? (s/n): ')

    if resposta == 's':
        restaurante['ativo'] = not restaurante['ativo']
        salvar_restaurantes(restaurantes)
        titulo(f'Restaurante {acao2} com sucesso!',True,False)
    else:
        titulo('Nenhuma alteração realizada.',True,False)

def perguntar_sim_nao(mensagem):
    while True:
        resposta = input(mensagem).strip().lower()
        if resposta in ['s', 'n']:
            return resposta
        else:
            titulo('Opção inválida! Digite "s" para sim ou "n" para não.',True,False)

def main(restaurantes):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        nome_programa()
        menu()
        escolher_opcao(restaurantes)

def salvar_restaurantes(restaurantes, caminho='restaurantes.json'):
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(restaurantes, f, ensure_ascii=False, indent=4)

def carregar_restaurantes(caminho='restaurantes.json'):
    if os.path.exists(caminho):
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

if __name__ == '__main__':
    restaurantes = carregar_restaurantes()

    main(restaurantes)

