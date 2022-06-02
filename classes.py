import requests


class Api():
    def __init__(self, url):
        self.api = requests.get(url).json()

    def listar_paises(self):
        lis = list(map(lambda x: x['name']['common'], self.api))
        lis.sort()

        numero = 1
        for country in lis:
            print(f'{numero}° - {country}') 
            numero += 1

    def selecionar_pais(self):
        nome_pais = str(input('Digite o nome do pais: '))
        pais_especifico = requests.get(f'https://restcountries.com/v3.1/name/{nome_pais}').json()
        # pais_especifico = requests.get(f'https://restcountries.com/v3.1/name/brazil').json()

        pais = dict()
        pais['nome'] = pais_especifico[0]['name']['common']
        pais['populacao'] = pais_especifico[0]['population']

        print(f'Nome: {pais["nome"]}')
        print(f'População: {pais["populacao"]:,.2f}')

    def acao_selecionada(self):
        while True:
            try:
                acao = int(input('Digite o número da ação que deseja: '))
                if acao < 1 or acao > 2:
                    print('\033[31mValor Inválido! Digite Uma Opção Válida.\033[m')
                    continue
            except ValueError:
                print('\033[31mValor Inválido! Digite Uma Opção Válida.\033[m')
                continue
            else:
                if acao == 1:
                    return self.listar_paises()
                elif acao == 2:
                    return self.selecionar_pais()
                break
        
