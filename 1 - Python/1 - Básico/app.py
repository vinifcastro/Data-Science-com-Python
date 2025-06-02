import os

def nome_programa():
    print('''
    █▀ ▄▀█ █▄▄ █▀█ █▀█   █▄▄ █▀█ ▄▀█ █▀ █ █░░ █▀▀ █ █▀█ █▀█
    ▄█ █▀█ █▄█ █▄█ █▀▄   █▄█ █▀▄ █▀█ ▄█ █ █▄▄ ██▄ █ █▀▄ █▄█\n''')

def menu():
    print('1 - Cadastrar Restaurante.')
    print('2 - Listar Restaurantes.')
    print('3 - Ativar Restaurante.')
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
        case 3:
            print('Ativar Restaurante.')
            loop(restaurantes)
        case 4:
            finalizar_programa()
        case _:
            opcao_invalida(restaurantes)

def finalizar_programa():
    os.system('cls')
    print('Saindo...')

def opcao_invalida(restaurantes):
    os.system('cls')
    print('Opção inválida!!!\n')
    loop(restaurantes)

def cadastrar_restaurante(restaurantes):
    os.system('cls')
    print('Ｃａｄａｓｔｒｏ ｄｅ ｎｏｖｏｓ ｒｅｓｔａｕｒａｎｔｅｓ．\n')

    nome_restaurante = input('Informe o nome do restaurante a ser cadastrado: ')
    restaurantes.append(nome_restaurante)
    
    os.system('cls')
    print(f'O restaurante: {nome_restaurante} foi cadastrado!')
    loop(restaurantes)

def listar_restaurantes(restaurantes):
    os.system('cls')
    print('Ｌｉｓｔａ ｄｅ Ｒｅｓｔａｕｒａｎｔｅｓ\n')

    if len(restaurantes) == 0:
        print('Não há restaurantes cadastrados!')
    else:
        for index, restaurante in enumerate(restaurantes, start=1):
            print(f'{index} - {restaurante}')
    loop(restaurantes)

def loop(restaurantes):
    input('\nAperte ENTER para voltar ao menu principal.')
    main(restaurantes)

def main(restaurantes):
    os.system('cls')
    nome_programa()
    menu()
    escolher_opcao(restaurantes)

if __name__ == '__main__':
    restaurantes = []  # lista criada apenas uma vez aqui!
    main(restaurantes)
