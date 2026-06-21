import time
from visual import mostrar_titulo, mostrar_narrativa, mostrar_codigo, mostrar_output, mostrar_pistas, mostrar_diagnostico
from rich.console import Console
from textwrap import dedent

console = Console()

#narrativa inicial:
def run_case4():
    console.print("")
    caso = """📂 CASO 4"""
    titulo_caso = "Cadastro de Alunos"
    
    narrativa = """
Uma escola relatou problemas no sistema de cadastro de alunos...
Ao atualizar as informações de um aluno, os demais registros deveriam permanecer salvos...
No entanto, após algumas atualizações, alunos que estavam cadastrados desaparecem da lista sem explicação...
Sua missão é investigar o código e descobrir por que os registros estão sendo perdidos.
               """
    mostrar_titulo(titulo_caso, caso)
    time.sleep(2)
    mostrar_narrativa(narrativa)
    time.sleep(4)


#código bugado
    codigo_bugado = dedent("""


    lista_de_alunos = ["Maria", "João", "Ana"]

    def atualizar_aluno(nome, novo_nome):

        # Atualizar cadastro da Maria

        lista_de_alunos = ["Maria Silva"]

    atualizar_aluno("Maria", "Maria Silva")
""")

#output/comportamento observado 
    output_observado = """ 
    Lista de alunos antes da atualização:
    ["Maria", "João", "Ana"]

    Lista de alunos após a atualização:
    ["Maria Silva"]
    """
    mostrar_codigo(codigo_bugado)
    time.sleep(3)
    mostrar_output(output_observado)
    time.sleep(2)

#investigações
    menu_investigacao = """
1. Verificar quantidade de alunos cadastrados
2. Analisar lista após a atualização
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
                console.print("━━━━━━━━━━ 💡 PISTA ENCONTRADA ━━━━━━━━━━\n➜ Antes da atualização existiam 3 alunos cadastrados. Após a atualização, apenas 1 permaneceu na lista.", style ="bold cyan")
                console.print("")
                time.sleep(2)
                pista_vista1 = True
       
        elif escolha == 2:
            if pista_vista2 == True:
                console.print("⚠ Você já investigou essa pista.", style ="blink yellow")
                console.print("")
                time.sleep(2)
            else:
                console.print("━━━━━━━━━━ 💡 PISTA ENCONTRADA ━━━━━━━━━━\n➜ Após a atualização, a lista contém apenas o registro atualizado da Maria.", style ="bold cyan")
                pista_vista2 = True
                time.sleep(2)
        else:
            console.print("Por favor, escolha a opção 1 ou 2!")
            console.print("")



#resultado final

    menu_decisao_final = """1. A lista de alunos foi substituída por uma nova lista durante a atualização.
2. O sistema remove alunos antigos automaticamente após uma atualização.
    """

    mostrar_diagnostico(menu_decisao_final)


    decisao_final = input("Qual é a causa do bug? ")
    time.sleep(2)
    if decisao_final == "1":
        console.print("━━━━━━━━━━ ✅ CASO RESOLVIDO ━━━━━━━━━━\n\nCAUSA IDENTIFICADA\n\nDurante a atualização, a lista original de alunos foi substituída por uma nova lista contendo apenas o registro atualizado. Como os demais alunos não foram preservados, seus cadastros foram perdidos.\n\n🏆 Caso encerrado com sucesso.", style ="blink green")
        time.sleep(2)
        return True
        
    elif decisao_final == "2":
        console.print("━━━━━━━━━━ ❌ DIAGNÓSTICO INCORRETO ━━━━━━━━━━\n\nO problema não está em uma remoção automática de alunos. A lista original foi substituída durante a atualização, causando a perda dos demais registros.\n\n🔄 Reiniciando investigação...", style="blink red")
        time.sleep(2)
        return False
    else:   
        console.print("Opção inválida. Por favor, escolha uma opção válida.")
        return False