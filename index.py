saldo = 0
limite = 500
cheque_especial = 1000  # FOI ADICIONADO O CHEQUE ESPECIAL A CONTA BLACK
extrato = ""
numero_saque = 0
LIMITES_SAQUES = 3

tipo_conta = input("Selecione o tipo de conta (Gold ou Black): ").lower() # FOI UTILIZADO O LOWER PARA CONVETER TODOS OS CARACTERES EM MINUSCULO

while tipo_conta not in ["gold", "black"]:
    print("Tipo de conta inválido. Por favor, escolha entre Gold ou Black.")
    tipo_conta = input("Selecione o tipo de conta (Gold ou Black): ").lower()

menu = f"""
    [d] = Depositar
    [s] = Sacar
    [e] = Extrato
    [q] = Sair
    """

while True:
    
    print(menu)
    opção = input("Escolha uma opção: ").lower()

    if opção == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print("Operação inválida!")

    elif opção == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saque >= LIMITES_SAQUES

        if tipo_conta == "black" and valor > (saldo + cheque_especial):
            print("Operação falhou! O valor do saque excede o saldo disponível mais o limite do cheque especial.")

        elif excedeu_saldo and tipo_conta == "gold":
            print("Operação falhou! Você não tem saldo suficiente")

        elif excedeu_limite and tipo_conta == "gold":
            print("Operação falhou! O valor do saque excedeu o limite")

        elif excedeu_saque and tipo_conta == "gold":
            print("Operação falhou! Número de saques excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1

        else:
            print("Operação inválida")
            
    elif opção == "e":
        print("\n=============== EXTRATO ===============")
        print("Não foram realizadas operações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        if tipo_conta == "black":
            print(f"Cheque Especial: R$ {cheque_especial:.2f}")
        print("=========================================")
        
    elif opção == "q":
        break
        
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada!")
