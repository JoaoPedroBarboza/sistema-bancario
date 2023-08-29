# Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato

# Operação de depósito: Deve ser possivel depositar valores positivos para a minha conta bancaria. Apenas um usuário. 
# Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

# Operação de saque: O sistema deve permitir realizar 3 saques diários com limite máximo de R$500,00 por saque. 
# Caso não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
# Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

# Operação de extrato: Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.
# Os valores devem ser exibidos utilizando o formato R$xxx,xx. Exemplo: 1500.45 = R$1500.45


menu = """
[1] Depositar
[2] Sacar 
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0 
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        print("======= DEPOSITO =======")
        deposito = float(input("Digite o valor do depósito: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Deposito: R${deposito:.2f}\n"
            print(f"Deposito de R${deposito:.2f} realizado com sucesso!")
        else:
            print("Deposito não pode ser realizado. O valor deve ser positivo")

    
    elif opcao == "2":
        print("======= SAQUE =======")
        saque = float(input("Digite o valor do saque: "))
        if saldo >= saque and saque <= limite:
            if numero_saques == LIMITE_SAQUES:
                print("Numéro total de saques ja realizado. Tente novamente amanhã")
            else:
                print("Saque realizado com sucesso!")
                saldo -= saque
                extrato += f"Saque: R${saque:.2f}\n"
                numero_saques += 1
                
        else:
            print("Valor não disponivel\nVerifique seu saldo na opção Extrato(3)\nO valor do saque deve ser até R$500,00")
    
    
    
    elif opcao == "3":
        print("======= EXTRATO =======")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R${saldo:.2f}")


    elif opcao == "0":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
