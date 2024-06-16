menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
Extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor do depósito: "))
        if valor >0:
            saldo += valor
            Extrato += f"Deposito: R$ {valor: .2f}\n"
    
        else:
            print("Operação falhou! O valor está incorreto.")


    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
    
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        execedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente!")

        elif excedeu_limite:
            print("Operação falhou ! Limite excedido!")

        elif execedeu_saques:
            print("Operação falhou ! Saque excedido!")

        elif valor > 0:
            saldo -= valor
            Extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou: O valor informado é inválido.")

    elif opcao == "e":
        print("\n========== EXTRATO=============")
        print("Não foram realizados movimentações." if not Extrato else Extrato)   
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================")

    elif opcao == "q":
            break

        else:
        print ("Operação inválida, por valor selecionamente novamente a operação desejada.")
