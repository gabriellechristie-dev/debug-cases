import time


#narrativa inicial
def run_case5():
    print("Iniciando investigação do caso 5...")
    time.sleep(3)

    print("Uma escola relatou que o sistema de emissão de boletins não está funcionando corretamente...")
    time.sleep(3)

    print("Os boletins deveriam ser gerados ao final do processamento das notas...")
    time.sleep(3)

    print("No entanto, o sistema encerra a execução sem gerar nenhum boletim...")
    time.sleep(3)

    print("Sua missão é investigar o código e descobrir por que a funcionalidade não está sendo executada.")
    time.sleep(4)



#código bugado
    codigo_bugado5 = """---Código Bugado para análise---
    def gerar_boletim():

        print("Boletim gerado com sucesso")


    print("Iniciando sistema...")

    print("Sistema encerrado.")

   """


#output/comportamento observado 
    output = """ 
    Iniciando sistema...

    Sistema encerrado.
    """
    print(codigo_bugado5)
    time.sleep(2)
    print(output)
    time.sleep(3)


#investigações
    menu_case5 = """ Menu de Pistas:
    1. Verificar execução da função de boletim
    2. Analisar mensagens exibidas pelo sistema
    """



#diagnóstico
    investigacao = 0
    while investigacao < 2:
        print(menu_case5)
        escolha = input("Escolha uma opção para investigar: ")  
        if escolha == "1":
            print("A função responsável por gerar o boletim está presente no código, mas não há indícios de que ela tenha sido executada.")
            investigacao += 1
        elif escolha == "2":
            print("O sistema inicia e encerra normalmente, porém a mensagem 'Boletim gerado com sucesso' nunca é exibida.")
            investigacao += 1
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")




#resultado final

    menu_decisao_final5 = """
    1. A função responsável por gerar o boletim nunca foi executada.
    2. A função foi executada, mas o sistema não conseguiu exibir a mensagem.
    """

    print(menu_decisao_final5)


    decisao_final5 = input("Qual é a causa do bug? ")
    if decisao_final5 == "1":
        print("Correto! A função responsável por gerar o boletim foi criada corretamente, porém nunca foi chamada durante a execução do programa. Como ela não é executada, o boletim não é gerado.")
        return True
        
    elif decisao_final5 == "2":
        print("Incorreto! Não há evidências de que a função tenha sido executada. O problema é que ela foi definida no código, mas nunca chamada.")
        return False
    else:   
        print("Opção inválida. Por favor, escolha uma opção válida.")
        return False