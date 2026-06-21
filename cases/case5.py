import time
from visual import mostrar_titulo, mostrar_narrativa, mostrar_codigo, mostrar_output, mostrar_pistas, mostrar_diagnostico
from rich.console import Console
from textwrap import dedent

console = Console()

#narrativa inicial
def run_case5():
    console.print("")
    caso = """📂 CASO 5"""
    titulo_caso = "Sistema de Boletins"
  
    narrativa = """
Uma escola relatou que o sistema de emissão de boletins não está funcionando corretamente..
Os boletins deveriam ser gerados ao final do processamento das notas...
No entanto, o sistema encerra a execução sem gerar nenhum boletim...
Sua missão é investigar o código e descobrir por que a funcionalidade não está sendo executada.
                """
    mostrar_titulo(titulo_caso, caso)
    time.sleep(2)
    mostrar_narrativa(narrativa)
    time.sleep(4)

#código bugado
    codigo_bugado = dedent("""
    def gerar_boletim():

        print("Boletim gerado com sucesso")


    print("Iniciando sistema...")

    print("Sistema encerrado.")
""")


#output/comportamento observado 
    output_observado = """ 
    Iniciando sistema...

    Sistema encerrado.
    """
    mostrar_codigo(codigo_bugado)
    time.sleep(3)
    mostrar_output(output_observado)
    time.sleep(2)

#investigações
    menu_investigacao = """
1. Verificar execução da função de boletim
2. Analisar mensagens exibidas pelo sistema
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
                console.print("━━━━━━━━━━ 💡 PISTA ENCONTRADA ━━━━━━━━━━\n➜ A função responsável por gerar o boletim está presente no código, mas não há indícios de que ela tenha sido executada.", style ="bold cyan")
                console.print("")
                time.sleep(2)
                pista_vista1 = True
       
        elif escolha == 2:
            if pista_vista2 == True:
                console.print("⚠ Você já investigou essa pista.", style ="blink yellow")
                console.print("")
                time.sleep(2)
            else:
                console.print("━━━━━━━━━━ 💡 PISTA ENCONTRADA ━━━━━━━━━━\n➜ O sistema inicia e encerra normalmente, porém a mensagem 'Boletim gerado com sucesso' nunca é exibida.", style ="bold cyan")
                pista_vista2 = True
                time.sleep(2)
        else:
            console.print("Por favor, escolha a opção 1 ou 2!")
            console.print("")





#resultado final

    menu_decisao_final = """1. A função responsável por gerar o boletim nunca foi executada.
2. A função foi executada, mas o sistema não conseguiu exibir a mensagem.
    """
    mostrar_diagnostico(menu_decisao_final)

    decisao_final = input("Qual é a causa do bug? ")
    time.sleep(2)
    if decisao_final == "1":
        console.print("━━━━━━━━━━ ✅ CASO RESOLVIDO ━━━━━━━━━━\n\nCAUSA IDENTIFICADA\n\nA função responsável por gerar o boletim foi criada corretamente, porém nunca foi chamada durante a execução do programa. Como ela não é executada, o boletim não é gerado.\n\n🏆 Caso encerrado com sucesso.", style ="blink green")
        time.sleep(2)
        return True
        
    elif decisao_final == "2":
        console.print("━━━━━━━━━━ ❌ DIAGNÓSTICO INCORRETO ━━━━━━━━━━\n\nNão há evidências de que a função tenha sido executada. O problema é que ela foi definida no código, mas nunca chamada.\n\n🔄 Reiniciando investigação...", style="blink red")
        time.sleep(2)
        return False
    else:   
        console.print("Opção inválida. Por favor, escolha uma opção válida.")
        return False