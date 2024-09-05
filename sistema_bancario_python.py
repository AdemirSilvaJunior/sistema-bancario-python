import random

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[c] Consultar Saldo
[r] Reiniciar Conta
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def bonus(saldo):
    if saldo >= 1000:
        valor_bonus = random.uniform(10, 50)
        print(f"\nParabéns! Você ganhou um bônus de R$ {valor_bonus:.2f} por ter mais de R$1000 na conta!")
        return valor_bonus
    return 0

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            saldo += bonus(saldo)  # Aplicando o bônus
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente. 😢")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite. 💸")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido. 🚫")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "c":
        print(f"\nSeu saldo atual é de: R$ {saldo:.2f}")

    elif opcao == "r":
        confirmar = input("Tem certeza que deseja reiniciar a conta? [s/n]: ")
        if confirmar == "s":
            saldo = 0
            extrato = ""
            numero_saques = 0
            print("Conta reiniciada com sucesso!")
        else:
            print("Reinicialização cancelada.")

    elif opcao == "q":
        print("Saindo... Volte sempre! 👋")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
