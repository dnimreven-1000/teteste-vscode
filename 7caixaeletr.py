#                                        Task 07: Caixa eletrônico
# Receba um valor de saque e informe a quantidade de notas de 100, 50, 20 e 10, 5 e 2 e moedas de 1 real (hardcore: 50, 25, 10 e 5 centavos) necessárias. Pratique: divisão inteira, resto e condicionais.
# Regras: não aceitar valores menores que 10 e informar quando o valor não puder ser sacado.
print("Caixa Eletrônico\n")

notas = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01]
def valor():
    try:
        seila = "notas de"
        qtd_inicial = float(input("Quantos reais você quer sacar? R$"))
        qtd = qtd_inicial
        if qtd == 0:
            print("Oxe tropa\n")
        if qtd < 0:
            raise ValueError
        else:
            for n in notas:
                qtdnotas = int(qtd // n)
                qtd = qtd % n
                if qtdnotas == 0:
                    continue
                else:
                    if n - int(n) != 0 or n < 1:
                        seila = "moedas de"
                        print(f"Quantidade de {seila} {int(n * 100)} centavos: {qtdnotas}")
                    else:
                        print(f"Quantidade de {seila} R${n}: {qtdnotas}")
                    if qtd == 0:
                        print("Fim!")
                        break
    except ValueError:
        print("Valor inválido.\n")
valor()