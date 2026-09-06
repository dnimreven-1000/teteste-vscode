print("Caixa eletrônico\n\n")
saldo = 0
extrato = []
def deposito():
    global saldo
    while True:
        try:
            print("--------------------")
            valdep = float(input("Insira o valor do depósito: R$"))
            if valdep < 0:
                print("Valor inválido. Talvez você queira realizar um saque?\n")
            else:
                saldo = saldo + valdep
                print(f"Depósito efetuado! Agora seu novo saldo é de R${saldo}\n")
                extrato.insert(0, saldo)
                print("--------------------")
                break
        except ValueError:
            print("Valor inválido.\n")

def saque():
    global saldo
    while True:
        try:
            print("--------------------")
            valsaq = float(input("Insira o valor do saque: R$"))
            if valsaq < 0:
                print("Valor inválido. Talvez você queira realizar um depósito?\n")
            else:
                if saldo - valsaq < 0:
                    print("Impossível. O saque é maior que o saldo disponível. Saque uma quantia menor.")
                else:
                    saldo = saldo - valsaq
                    print(f"Saque efetuado! Agora seu novo saldo é de R${saldo}\n--------------------")
                    extrato.insert(0, saldo)
                    break
        except ValueError:
            print("Valor inválido.")

def extrat():
    print("--------------------")
    print(f"Saldo atual: R${saldo}\n")
    if len(extrato) == 0:
        print("Sem histórico de transação.")
        print("--------------------")
    else:
        print("Histórico (mais recente para mais antigo):")
        for n in extrato:
            print(f"R${n}")
        print("--------------------")

reqsair = None    
while True:
    try:
        print("Qual operação você deseja fazer?\n[1] Depósito\n[2] Saque\n[3] Ver extrato\n[4] Sair")
        op = "Operação"
        op = int(input(">>> "))
        if op != 1 and op != 2 and op != 3 and op !=4:
            raise ValueError
        else:
            if op == 1:
                deposito()
            if op == 2:
                saque()
            if op == 3:
                extrat()
            if op == 4:
                    try:
                        sair = input("Você deseja encerrar o programa? [s/n] ")
                        if sair == "s":
                            reqsair = True
                        elif sair == "n":
                            reqsair = False
                        else:
                            raise ValueError
                    except ValueError:
                        print("Resposta inválida.")
            if reqsair == True:
                break
            elif reqsair == False:
                continue
    except ValueError:
        print("Valor inválido.\n")