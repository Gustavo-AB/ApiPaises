from classes import *

api = Api('https://restcountries.com/v3.1/all')

if __name__ == '__main__':
    while True:
        print(f'{"~"*10}Sobre Paises{"~"*10}')
        print('[1]-Listar Todos os Paises')
        print('[2]-Informações Sobre Determinado Pais')
        api.acao_selecionada()

  
        execucao = str(input('Deseja Continuar? [S]/[N]')).lower().strip()
        if execucao not in 'nNsS':
            print('\033[31mValor Inválido! Digite Uma Opção Válida.\033[m')
        else:
            if execucao in 'nN':
                break
print('Até Logo!')