"""
Projeto: Calculadora de Quatro Operações
Descrição: Uma calculadora em Python que realiza as quatro operações básicas.
Autor: [Joseffer Maxwel Oliveira das Mercês]
Contato: [joseffermax1472@gmail.com ou https://github.com/joseffermax]
"""

import os
from colorama import Style

# Função para criar uma linha de caracteres "-" com tamanho personalizável
def linha(tam=50):
    return "-" * tam

# Função para criar uma linha de caracteres "-" com tamanho personalizável (usada no cabeçalho)
def linha_igual(tam=50):
    return "-" * tam

# Função para exibir um cabeçalho
def cabecalho(txt):
    print(linha())
    print(txt.center(50))
    print(linha())

# Função para exibir o título da calculadora
def titulo_calculadora():
    print(linha_igual(50))
    print("CALCULADORA SIMPLES".center(50))
    print(linha_igual(50))

# Função para exibir o menu
def menu(lista):
    cabecalho("CALCULADORA SIMPLES")
    print(lista)

while True: # Página inicial
    titulo_calculadora()
    print("[1] - Iniciar")
    print("[2] - Sair do sistema")
    print(linha_igual(50))
    entrada = input("Sua opção: ")

    try:
        opcao = int(entrada)

        if opcao == 1: # Iniciar
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                titulo_calculadora()

                while True:
                    try:
                        primeiro_num = float(input("Digite o primeiro número: ")) # Entrada para o primeiro número
                        segundo_num = float(input("Digite o segundo número: ")) # Entrada para o segundo número
                        print(linha_igual(50))
                        break
                    except ValueError: # Entrada de erro caso digite letras de vez número
                        print("Erro... Apenas números são permitidos")
                        print('Ex: 10, 100, 1500.50, -5000')
                        input("Pressione " + Style.BRIGHT + "'Enter'" + Style.RESET_ALL + " para voltar... ")
                        os.system("cls" if os.name == "nt" else "clear")
                        titulo_calculadora()

                num1 = primeiro_num
                num2 = segundo_num

                while True:
                    operadores = input("Qual operador você deseja usar?\n[1] soma\n[2] subtração\n[3] multiplicação\n[4] divisão\nSua opção: ") # Operadores
                    opcao_operadores = operadores

                    if operadores == "1": # Entrada para Soma
                        print(linha_igual(50))
                        print(f"A soma entre {primeiro_num} + {segundo_num} é igual a {primeiro_num + segundo_num}")
                        break
                    elif operadores == "2": # Entrada para Menos
                        print(linha_igual(50))
                        print(f"A subtração entre {primeiro_num} - {segundo_num} é igual a {primeiro_num - segundo_num}")
                        break
                    elif operadores == "3": # Entrada para Multiplicação
                        print(linha_igual(50))
                        print(f"A multiplicação entre {primeiro_num} * {segundo_num} é igual a {primeiro_num * segundo_num}")
                        break
                    elif operadores == "4": # Entrada para Divisão
                        print(linha_igual(50))
                        if segundo_num != 0: 
                            print(f"A divisão entre {primeiro_num} / {segundo_num} é igual a {primeiro_num / segundo_num}")
                            break
                        else: # Entrada para divisão igual a 0
                            print("Erro... Não é possível dividir por 0!")
                            break
                    else: # Entrada de erro caso o usuário digite números diferentes de 1, 2, 3 e 4 
                        print("São apenas permitidos os números '1', '2', '3' e '4'")
                        input("Pressione " + Style.BRIGHT + "'Enter'" + Style.RESET_ALL + " para continuar ")
                        os.system("cls" if os.name == "nt" else "clear")
                        titulo_calculadora()
                        print(f"Números digitados foram: {num1} e {num2}\nEscolha a operação desejada!\n ")

                resposta = input("Deseja continuar calculando? (S/N): ")
                if resposta.upper() == 'S': # Continua calculando
                    continue
                else: # Para de calcular
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break

        elif opcao == 2: # Sair do sistema
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                titulo_calculadora()
                print("Encerrando o programa...")
                print("Obrigado pela preferência!")
                print(linha_igual(50))
                sair_ou_voltar = input("Pressione S (para sair) ou N (para voltar): ")

                if sair_ou_voltar.upper() == "S": # Encerra o programa
                    exit()
                elif sair_ou_voltar.upper() == "N": # Volta para o programa
                    print("Retornando ao sistema...")
                    input("Pressione " + Style.BRIGHT + "'Enter'" + Style.RESET_ALL + " para continuar ")
                    os.system("cls" if os.name == "nt" else "clear")
                    break
                else: # Entrada diferente de S e N
                    print("Opção inválida. Apenas 'S' e 'N' são permitidos!") 
                    input("Pressione " + Style.BRIGHT + "'Enter'" + Style.RESET_ALL + " para voltar... ")
                os.system("cls" if os.name == "nt" else "clear")

        else: # Entrada de erro caso o usuário digite números diferentes de 1 e 2
            os.system("cls" if os.name == "nt" else "clear")
            titulo_calculadora()
            print("Erro... Número incorreto!")
            input("Pressione " + Style.BRIGHT + "'Enter'" + Style.RESET_ALL + " para voltar... ")
            os.system("cls")

    except ValueError: # Entrada de erro caso o usuário digite letra envés de 1 e 2
        os.system("cls" if os.name == "nt" else "clear")
        titulo_calculadora()
        print("Erro... Apenas '1' e '2' são permitidos!")
        input("Pressione " + Style.BRIGHT + "'Enter'" + Style.RESET_ALL + " para voltar... ")
        os.system("cls")

