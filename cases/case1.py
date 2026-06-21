import time
from visual import mostrar_titulo, mostrar_narrativa, mostrar_codigo, mostrar_output, mostrar_pistas, mostrar_diagnostico
from rich.console import Console
from textwrap import dedent

console = Console()

#narrativa inicial
def run_case1(): 
    console.print("")
    caso = """📂 CASO 1"""
    titulo_caso = "Sistema Bancário"

    narrativa = """
Um banco recebeu diversos relatos de clientes afirmando que seus saldos desapareciam após operações de depósito e saque...
Os valores pareciam ser redefinidos de forma inesperada, comprometendo a integridade do sistema financeiro...
Sua missão é investigar o código e identificar o bug responsável pelo desaparecimento dos saldos...
                """
    mostrar_titulo(titulo_caso, caso)
    time.sleep(2)
    mostrar_narrativa(narrativa)
    time.sleep(4)

#código bugado
    codigo_bugado = dedent("""
saldo_inicial = 100
valor_deposito = 50

def depositar(saldo, valor):
    saldo = valor
    return saldo

    resultado = depositar(saldo_inicial, valor_deposito)

print("Saldo após depósito:", resultado)
""")

#output/comportamento observado
    output_observado = """ 
    "Saldo após depósito: 50"
    """
    mostrar_codigo(codigo_bugado)
    time.sleep(3)
    mostrar_output(output_observado)
    time.sleep(2)

#investigações
    menu_investigacao = """
1. Analisar variável saldo  
2. Testar depósito
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
                console.print("⚠ Você já investigou essa pista.", style ="blink yellow")
                console.print("")
                time.sleep(2)
            else:
                console.print("━━━━━━━━━━ 💡 PISTA ENCONTRADA ━━━━━━━━━━\n➜ O valor armazenado no saldo parece não permanecer após a operação.", style="bold cyan")
                console.print("")
                time.sleep(2)
                pista_vista1 = True
        
        elif escolha == 2:
            if pista_vista2 == True:
                console.print("⚠ Você já investigou essa pista.", style ="blink yellow")
                console.print("")
                time.sleep(2)
            else:
                console.print("━━━━━━━━━━ 💡 PISTA ENCONTRADA ━━━━━━━━━━\n➜ O valor final corresponde apenas ao último depósito realizado.", style="bold cyan")
                pista_vista2 = True
                time.sleep(2)
        else:
            console.print("Por favor, escolha a opção 1 ou 2!")
            console.print("")

#resultado final
    menu_decisao_final = """1. A variável saldo está sendo reinicializada dentro da função
2. O sistema está exibindo o resultado incorretamente

    """
    
    mostrar_diagnostico(menu_decisao_final)

    
    decisao_final = int(input("Qual é a causa do bug? "))
    time.sleep(2)
    if decisao_final == 1:
        console.print("━━━━━━━━━━ ✅ CASO RESOLVIDO ━━━━━━━━━━\n\nCAUSA IDENTIFICADA\n\nA variável saldo está sendo reinicializada dentro da função, substituindo o valor anterior pelo valor do depósito.\n\n🏆 Caso encerrado com sucesso.", style ="blink green")
        time.sleep(2)
        return True
    elif decisao_final == 2:
        console.print("━━━━━━━━━━ ❌ DIAGNÓSTICO INCORRETO ━━━━━━━━━━\n\nA hipótese escolhida não explica o comportamento observado.\n\n🔄 Reiniciando investigação...", style="blink red")
        time.sleep(2)
        return False
    else:   
        console.print("Opção inválida. Por favor, escolha uma opção válida.")
        return False