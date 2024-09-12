saldo = 0.00
num_of_saques = 0
extrato = []

def deposito(valor):
    #Só é possível adicionar valores positivos.
    if valor > 0:
        #Todos os depositos devem ser armazenados em uma variável.
        global saldo
        saldo += valor
        print("\nDepósito feito com sucesso.")
    else:
        print("\nValor inválido.")

def saque(valor):
    #Só é possível 3 saques por dia.
    #De até 500.00 reais.
    global num_of_saques
    if num_of_saques <= 3:
        if valor > 0 and valor <= 500.00:
            global saldo
            if saldo > valor:
                saldo -= valor
                num_of_saques += 1
                print("\nSaque realizado com sucesso.")
            else:
                #Mensagem de saldo insuficiente.
                print("\nSaldo insuficiente.")
        else:
            print("valor de saque inválido (Permitido até R$500.00).")
    else:
        print("limite de saques diários alcançados.")


def add_extrato(valor, operacao):
    new_extrato = {'valor': valor, 'operacao': operacao}
    new_extrato['valor'] = f"R$ {new_extrato['valor']:.2f}"
    extrato.append(new_extrato)
    print("Extrato inserido com sucesso.\n")

def menu():
    print("""         GRANDE BANCO
 ------------------------------
 Aperte o número correspondente
 à operação desejada:
        
 [1]Depósito.
 [2]Saque.
 [3]Extrato.
 [4]Encerrar(Sair).\n """)

    choice = int(input())
    possible_numbers = (1, 2, 3, 4)

    if choice in possible_numbers:
        if choice == 1:
            print("\nValor do depósito: ")
            value = float(input())
            deposito(value)
            add_extrato(**{"valor" : value, "operacao" : "deposito"})
            menu()
        elif choice == 2:
            print("\nValor do saque: ")
            value = float(input())
            saque(value)
            add_extrato(**{"valor" : value, "operacao" : "saque"})
            menu()
        elif choice == 3:
            print("\n", extrato , "\n")
            print(f"Saldo atual: R${saldo:.2f} \n")
            menu()
        elif choice == 4:
            exit()
    else:
        print("Opção inválida.\n")
        menu()

menu()