def banco():
    # Dados do cliente
    print("==============================")
    print("     BANCO PYTHON")
    print("==============================")

    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")

    saldo = 0.0
    extrato = []

    print("\nBem-vindo ao Banco Python,", nome + "!")

    # Menu principal
    while True:
        print("\n========= MENU =========")
        print("1 - Consultar saldo")
        print("2 - Depositar dinheiro")
        print("3 - Sacar dinheiro")
        print("4 - Consultar extrato")
        print("5 - Mostrar dados do cliente")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        # Consultar saldo
        if opcao == "1":
            print(f"\nSeu saldo atual é: R$ {saldo:.2f}")

        # Depositar dinheiro
        elif opcao == "2":
            valor = float(input("Digite o valor do depósito: R$ "))

            if valor > 0:
                saldo = saldo + valor
                extrato.append(f"Depósito: + R$ {valor:.2f}")
                print("Depósito realizado com sucesso!")
            else:
                print("Erro: o valor precisa ser maior que zero.")

        # Sacar dinheiro
        elif opcao == "3":
            valor = float(input("Digite o valor do saque: R$ "))

            if valor <= 0:
                print("Erro: o valor precisa ser maior que zero.")

            elif valor > saldo:
                print("Saldo insuficiente!")

            else:
                saldo = saldo - valor
                extrato.append(f"Saque: - R$ {valor:.2f}")
                print("Saque realizado com sucesso!")

        # Consultar extrato
        elif opcao == "4":
            print("\n========= EXTRATO =========")
            print("Cliente:", nome)

            if len(extrato) == 0:
                print("Nenhuma movimentação realizada.")
            else:
                for operacao in extrato:
                    print(operacao)

            print(f"Saldo atual: R$ {saldo:.2f}")

        # Mostrar dados do cliente
        elif opcao == "5":
            print("\n===== DADOS DO CLIENTE =====")
            print("Nome:", nome)
            print("CPF:", cpf)
            print(f"Saldo: R$ {saldo:.2f}")

        # Encerrar o sistema
        elif opcao == "6":
            print("\nObrigado por utilizar o Banco Python!")
            print("Até logo,", nome + "!")
            break

        # Opção inválida
        else:
            print("Opção inválida! Tente novamente.")


# Executar o sistema
banco()


