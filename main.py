def deposito(saldo):
    valor = int(input("Qual valor será depositado: "))
    #Esse While verifica se o valor de deposito é maior que zero
    while valor <= 0:
        print("O valor depositado deve ser maior que Zero")
        valor = int(input("Qual valor será depositado: "))
    #atualizaçao do saldo
    saldo = saldo + valor

    return {"valor": valor, "resposta": 200, "saldo":saldo}

def saque(saldo, limite, qtd_saque, LIMITE_SAQUE, saque_total):
    #Verifica se já foi feito 3 saques (que é o limite diário)
    if qtd_saque >= LIMITE_SAQUE:
        return("A quantidade de saque diário foi atingida")
    #Verifica se usuário já sacou o limite diário de R$1500,00
    if saque_total >= limite:
        return "Saque Bloqueado, você já sacou o limite diário disponível"
    valor = int(input("Qual valor deseja sacar?"))
    #Esse While verifica se o valor solicitado é Maior que zero
    while valor <= 0:
        print("O valor para saque deve ser maior que 0")
        valor = int(input("Qual valor deseja sacar?"))
    #Esse while verifica se o valor solicitado está disponível para saque
    while valor > saldo:
        print(f"Saldo indisponível, o seu saldo é de {saldo}")
        valor = int(input("Caso deseje sacar outro valor digite o valor, caso não digite 0 para"
                          "cancelar a operação"))
    #Esse while verifica se o valor solicitado é maior que o limite diário de saque
    while valor > limite:
        valor = int(input("Limite de saque diário é 1500, saque dentro do valor ou digite zero para cancelar "))
        if valor == 0:
            return ("Operação cancelada")
    #atualiza saldo
    saldo = saldo + valor

    return {"valor": valor, "resposta": 200, "saldo": saldo}

def ext(operacoes, saldo):
    #Verifica a qtd de saque e depositos
    #o valor é subtraido por 1 para ter o índice final da lista e dentro do for verificar
    #se é a ultima iteração para somar total de saques e depositos
    numero_saques = len(operacoes["saque"]) - 1
    numero_deposito = len(operacoes["deposito"]) - 1
    aux = 0
    print("             Saques \n -------------------------------------------------\n")
    for valor in operacoes["saque"]:
        print(f"............................R${valor}")
        if numero_saques - aux == 0:
            print(f"\nTotal.......................R${sum(operacoes['saque'])}")
    aux = 0
    print("            Depositos \n\n -------------------------------------------------\n")
    for valor in operacoes["deposito"]:
        print(f"............................R${valor}")
        if numero_deposito - aux == 0:
            print(f"\nTotal.......................R${sum(operacoes['deposito'])}")

    print(f"""\n\n --------------------------------------------------
    \nSaldo atual........................{saldo}""")
    return


menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 1500
extrato = ""
LIMITE_SAQUE = 3
qtd_saque = 0
operacoes = {"saque": [],"deposito": [] }

while True:

    opcao = input(menu)

    if opcao == "d":
        resposta = (deposito(saldo))
        if resposta["resposta"] == 200:
            operacoes["deposito"].append(resposta["valor"])
            saldo = resposta["saldo"]
            print("Operação realizada com sucesso!")


    elif opcao == "s":
        resposta = (saque(saldo, limite, qtd_saque, LIMITE_SAQUE,saque_total=sum(operacoes["saque"])))
        try:
            if resposta["resposta"] == 200:
                operacoes["saque"].append((resposta["valor"]))
                saldo = resposta["saldo"]
                print("Operação realizada com sucesso!")
        except:
            print(resposta)


    elif opcao == "e":
        ext(operacoes, saldo)


    elif opcao == "q":
        break

    else:
        print("Operação inválida, tente novamente!")