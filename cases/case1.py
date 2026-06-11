import time
from visual import mostrar_titulo, mostrar_narrativa, mostrar_codigo, mostrar_output, mostrar_pistas, mostrar_diagnostico

#narrativa inicial
def run_case1(): 
    titulo_caso = "Caso 1 - Sistema Bancário"

    narrativa = """
    Um banco recebeu diversos relatos de clientes afirmando que seus saldos desapareciam após operações de depósito e saque...
    Os valores pareciam ser redefinidos de forma inesperada, comprometendo a integridade do sistema financeiro...
    Sua missão é investigar o código e identificar o bug responsável pelo desaparecimento dos saldos...
                """
    mostrar_titulo(titulo_caso)
    time.sleep(1.5)
    mostrar_narrativa(narrativa)
    time.sleep(1.5)

#código bugado
    codigo_bugado = """
    saldo_inicial = 100
    valor_deposito = 50

    def depositar(saldo, valor):
        saldo = valor
        return saldo

    resultado = depositar(saldo_inicial, valor_deposito)

    print("Saldo após depósito:", resultado)
    """

#output/comportamento observado
    output_observado = """ 
    "Saldo após depósito: 50"
    """
    mostrar_codigo(codigo_bugado)
    time.sleep(2)
    mostrar_output(output_observado)
    time.sleep(2)

#investigações
    menu_investigacao = """ 
    1. Analisar variável saldo  
    2. Testar depósito
    """ 

#diagnóstico
    investigacao = 0
    while investigacao < 2:
        mostrar_pistas(menu_investigacao)
        escolha = input("Escolha uma opção para investigar: ")  
        if escolha == "1":
            print("O valor armazenado no saldo parece não permanecer após a operação.")
            investigacao += 1
        elif escolha == "2":
            print("O valor final corresponde apenas ao último depósito realizado.")
            investigacao += 1
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

#resultado final
    menu_decisao_final = """
    1. A variável saldo está sendo reinicializada dentro da função
    2. O sistema está exibindo o resultado incorretamente

    """

    mostrar_diagnostico(menu_decisao_final)

    
    decisao_final = input("Qual é a causa do bug? ")
    if decisao_final == "1":
        print("Correto! A variável saldo está sendo reinicializada dentro da função, o que faz com que o valor anterior seja perdido.")
        return True
    elif decisao_final == "2":
        print("Incorreto. O sistema está exibindo o resultado corretamente, mas o problema está na forma como a variável saldo é manipulada dentro da função.")
        return False
    else:   
        print("Opção inválida. Por favor, escolha uma opção válida.")
        return False