import time
from visual import mostrar_titulo, mostrar_narrativa, mostrar_codigo, mostrar_output, mostrar_pistas, mostrar_diagnostico
from rich.console import Console


console = Console()

#narrativa inicial
def run_case2():
    console.print("")
    caso = """📂 CASO 2"""
    titulo_caso = "Loop Infinito"
    
    narrativa = """
Uma empresa relatou que o sistema de processamento de pedidos ficou preso executando indefinidamente...
Os pedidos deveriam ser processados e o programa encerrado após concluir o trabalho...
No entanto, o sistema continua executando sem parar, nunca chegando a mostrar a mensagem de processamento final de todos os pedidos...
                """
    mostrar_titulo(titulo_caso, caso)
    time.sleep(2)
    mostrar_narrativa(narrativa)
    time.sleep(4)

#código bugado
    codigo_bugado = """
    pedidos_processados = 0

    while pedidos_processados < 50:
        pedido = int(input("Digite o número do pedido que deseja processar:"))
       
        print("Pedido processado com sucesso")

    print("Todos os pedidos foram processados com sucesso")

    """

#output/comportamento observado
    output_observado = """
Digite o número do pedido que deseja processar: 101
Pedido processado com sucesso

Digite o número do pedido que deseja processar: 102
Pedido processado com sucesso

Digite o número do pedido que deseja processar: 103
Pedido processado com sucesso

Digite o número do pedido que deseja processar: 104
Pedido processado com sucesso
"""
    mostrar_codigo(codigo_bugado)
    time.sleep(3)
    mostrar_output(output_observado)
    time.sleep(2)

#investigações
    menu_investigacao = """
1. Verificar contador de pedidos
2. Monitorar encerramento do sistema
    """

#diagnóstico
    pista_vista1 = False
    pista_vista2 = False
    mostrar_pistas(menu_investigacao)
    while pista_vista1 == False or pista_vista2 == False:
       
        escolha = int(input("Escolha uma opção para investigar: "))
        console.print("")
        time.sleep(2)
        if escolha == 1:
            if pista_vista1 == True:
                console.print("⚠ EVIDÊNCIA JÁ COLETADA.", style ="blink yellow")
                console.print("")
                time.sleep(2)
            else:
                console.print("━━━━━━━━━━ 💡 PISTA ENCONTRADA ━━━━━━━━━━\n➜ A quantidade de pedidos processados parece permanecer a mesma durante a execução.", style ="bold cyan")
                console.print("")
                time.sleep(2)
                pista_vista1 = True
       
        elif escolha == 2:
            if pista_vista2 == True:
                console.print("⚠ EVIDÊNCIA JÁ COLETADA", style ="blink yellow")
                console.print("")
                time.sleep(2)
            else:
                console.print("━━━━━━━━━━ 💡 PISTA ENCONTRADA ━━━━━━━━━━\n➜ A mensagem de conclusão final do processamento nunca é exibida.", style ="bold cyan")
                pista_vista2 = True
                time.sleep(2)
        else:
            console.print("Por favor, escolha a opção 1 ou 2!")
            console.print("")


#resultado final
    menu_decisao_final = """1. O contador de pedidos não está sendo atualizado corretamente
2. A condição do while está escrita incorretamente.
"""

    mostrar_diagnostico(menu_decisao_final)



    decisao_final = input("Qual é a causa do bug? ")
    if decisao_final == "1":
        console.print("━━━━━━━━━━ ✅ CASO RESOLVIDO ━━━━━━━━━━\n\nCAUSA IDENTIFICADA\n\nO contador de pedidos não está sendo atualizado durante a execução. Como seu valor permanece 0, a condição de parada nunca é alcançada e o loop continua indefinidamente.\n\n🏆 Caso encerrado com sucesso.", style ="blink green")
        time.sleep(2)
        return True
    elif decisao_final == "2":
        console.print("━━━━━━━━━━ ❌ DIAGNÓSTICO INCORRETO ━━━━━━━━━━\n\nA condição do while está escrita corretamente. O problema é que a variável utilizada na condição não é atualizada durante a execução.\n\n🔄 Reiniciando investigação...", style="blink red")
        time.sleep(2)
        return False
    else:   
        console.print("Opção inválida. Por favor, escolha uma opção válida.")
        return False