# Data: 17/04/2024
# Atividade: Faça um programa com as especificações:
#   1 - O Usuario deverá escolher entre os objetos a seguir
#           - Circulo
#           - Retângulo
#           - Triângulo
#           - Quadrado
#   2 - De acordo com o objeto escolhido, o usuário deverá informar a seguinte informação
#           - Para Circulo > Raio
#           - Para o Retângulo > Comprimento e largura
#           - Para o Triângulo > Base, altura e lado
#           - Para o Quadrado > Lado
#   3 - O programa deverá calcular: 
#           - Para o Circulo > Área e perímetro
#           - Para o Retângulo > Área e perímetro
#           - Para o Triângulo > Área e perímetro
#           - Para o Quadrado > Área e perímetro
# Autor: Higor Stanley aka Devyat009
import math;
# Função
def e_numero(string):
    try:
        if string.isnumeric():
            formata_int = int(string)
            return True
        else:
            formata_float = float(string)
            return True
    except ValueError:
        return False
# Programa em estado de loop    
while True:
        resultado = 0
        decisao = (input('''Insira as opções:
                        [1] Circulo
                        [2] Retângulo
                        [3] Triângulo
                        [4] Quadrado
                        [5] Sair
                        Opção a ser escolhida: '''))
    # Valida se o input do usuario e um número valido
        if e_numero(decisao):
            # Escolha 1: Circulo
            if decisao == '1':
                while True:
                    raio = input('Insira o raio do circulo: ')
                    if e_numero(raio):
                        raio = float(raio)
                        circuferencia = (2 * math.pi) * raio
                        area = math.pi * (raio ** 2)
                        diametro = 2 * raio 
                        print(f'''O resutado de calculos de um circulo com o valor inserido {raio} é:\n
                            Circuferência: {circuferencia}
                            Área: {area}
                            Diametro: {diametro}''')
                        break
                    else:
                        print('\nInsira um número válido para o raio!\n')    
            # Escolha 2: Retângulo
            elif decisao == '2':
                while True:
                    altura = input('Insira a altura do retângulo: ')
                    if e_numero(altura):
                        altura = float(altura)
                        while True:
                            base = input('Insira a base do retângulo: ')
                            if e_numero(base):
                                base = float(base)
                                area = altura * base
                                perimetro = 2 * (base + altura)
                                print(f'''O resutado de calculos de um retângulo com o valor inserido de {altura} altura e {base} da base:\n
                                        Área: {area}
                                        Perímetro: {perimetro}''')
                                break
                            else:
                                print('\nInsira um número válido para a base!\n')
                        break    
                    else:
                        print('\nInsira um número válido para a altura!\n')
            # Escolha 3: Triângulo
            # Multiplos 'while' para cada valor inserido para que haja uma validação de cada input do usuario
            elif decisao == '3':
                while True:
                    altura = input('Insira a altura do triângulo: ')
                    if e_numero(altura):
                        altura = float(altura)
                        while True:
                            base = input('Insira a base do triângulo: ')
                            if e_numero(base):
                                base = float(base)
                                while True:
                                    lado = input('Insira o lado do triângulo: ')
                                    if e_numero(lado):
                                        lado = float(lado)
                                        area = 1/2 * (base * altura)
                                        perimetro = base + lado + lado
                                        print(f'''O resutado de calculos de um triângulo com o valor inserido de {altura} altura, {base} da base e do lado {lado}:\n
                                                    Área: {area}
                                                    Perímetro: {perimetro}''')
                                        break
                                    else:
                                        print('\nInsira um número válido para o lado!\n')
                                break
                            else:
                                print('\nInsira um número válido para a base!\n')
                        break
                    else:
                        print('\nInsira um número válido para a altura!\n')
            # Escolha 4: Quadrado
            elif decisao == '4':
                while True:
                    lado = input('Insira o lado do quadrado: ')
                    if e_numero(lado):
                        area = lado ** 2
                        perimetro = lado + lado + lado + lado
                        print(f'''O resutado de calculos de um quadrade com o valor {lado} inserido é:\n
                                Área: {area}
                                Perímetro: {perimetro}''')
                        break
                    else:
                        print('\nInsira um número válido para o lado!\n')
            # Escolha 5: Sair do programa
            elif decisao == '5':
                print('Saindo...')
                break
            # Opção fora do escopo  
            else:
                print('\nOpção INVALIDA detectada\n')
        # Caso o input do usuario não seja um número alertar:
        else: 
            print('\nInsira um numero entre 1 e 5 e tente novamente!!\n')
