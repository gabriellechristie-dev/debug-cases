import time

#narrativa inicial
def run_case2():
    print("Iniciando investigação do caso 2...")
    time.sleep(3)

    print("Uma empresa relatou que o sistema de processamento de pedidos ficou preso executando indefinidamente...")
    time.sleep(3)

    print("Os pedidos deveriam ser processados e o programa encerrado após concluir o trabalho...")
    time.sleep(3)
    
    print("No entanto, o sistema continua executando sem parar, nunca chegando a mostrar a mensagem de processamento final de todos os pedidos...")
    time.sleep(4)

    #código bugado
    codigo_bugado2 = """Código Bugado para análise:
    
    pedidos_processados = 0

    while pedidos_processados < 50:
        pedido = int(input("Digite o número do pedido que deseja processar:"))
       
        print("Pedido processado com sucesso")

    print("Todos os pedidos foram processados com sucesso")

    """

#output/comportamento observado
    output = """ Output/comportamento observado:
    Digite o número do pedido que deseja processar: 101
    Pedido processado com sucesso

    Digite o número do pedido que deseja processar: 102
    Pedido processado com sucesso

    Digite o número do pedido que deseja processar: 103
    Pedido processado com sucesso

    Digite o número do pedido que deseja processar: 104
    Pedido processado com sucesso
"""
    print(codigo_bugado2)
    time.sleep(2)
    print(output)
    time.sleep(3)

#investigações
    menu_case2 = """ Menu de Pistas
    1. Verificar contador de pedidos
    2. Monitorar encerramento do sistema
    """

#diagnóstico
    investigacao = 0
    while investigacao < 2:
        print(menu_case2)
        escolha = input("Escolha uma opção para investigar: ")  
        if escolha == "1":
            print("A quantidade de pedidos processados parece permanecer a mesma durante a execução.")
            investigacao += 1
        elif escolha == "2":
            print("A mensagem de conclusão final do processamento nunca é exibida.")
            investigacao += 1
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

#resultado final
    menu_decisao_final2 = """
    1. O contador de pedidos não está sendo atualizado corretamente
    2. A condição do while está escrita incorretamente.

    """

    print(menu_decisao_final2)


    decisao_final2 = input("Qual é a causa do bug? ")
    if decisao_final2 == "1":
        print("Correto! O contador de pedidos não está sendo atualizado durante a execução. Como seu valor permanece 0, a condição de parada nunca é alcançada e o loop continua indefinidamente.")
        return True
    elif decisao_final2 == "2":
        print("Incorreto. A condição do while está escrita corretamente. O problema é que a variável utilizada na condição não é atualizada durante a execução.")
        return False
    else:   
        print("Opção inválida. Por favor, escolha uma opção válida.")
        return False