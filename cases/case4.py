import time
from visual import mostrar_titulo, mostrar_narrativa, mostrar_codigo, mostrar_output, mostrar_pistas, mostrar_diagnostico

#narrativa inicial:
def run_case4():
    titulo_caso = "Caso 4 - Cadastro de Alunos"
    
    narrativa = """
    Uma escola relatou problemas no sistema de cadastro de alunos...
    Ao atualizar as informações de um aluno, os demais registros deveriam permanecer salvos...
    No entanto, após algumas atualizações, alunos que estavam cadastrados desaparecem da lista sem explicação...
    Sua missão é investigar o código e descobrir por que os registros estão sendo perdidos.
               """
    print(titulo_caso)
    time.sleep(1.5)
    print(narrativa)
    time.sleep(1.5)

#código bugado
    codigo_bugado = """


    lista_de_alunos = ["Maria", "João", "Ana"]

    def atualizar_aluno(nome, novo_nome):

        # Atualizar cadastro da Maria

        lista_de_alunos = ["Maria Silva"]

    atualizar_aluno("Maria", "Maria Silva")


    """

#output/comportamento observado 
    output_observado = """ 
    Lista de alunos antes da atualização:
    ["Maria", "João", "Ana"]

    Lista de alunos após a atualização:
    ["Maria Silva"]
    """
    print(codigo_bugado)
    time.sleep(2)
    print(output_observado)
    time.sleep(2)

#investigações
    menu_investigacao = """
    1. Verificar quantidade de alunos cadastrados
    2. Analisar lista após a atualização
    """ 

#diagnóstico
    investigacao = 0
    while investigacao < 2:
        print(menu_investigacao)
        escolha = input("Escolha uma opção para investigar: ")  
        if escolha == "1":
            print("Antes da atualização existiam 3 alunos cadastrados. Após a atualização, apenas 1 permaneceu na lista.")
            investigacao += 1
        elif escolha == "2":
            print("Após a atualização, a lista contém apenas o registro atualizado da Maria.")
            investigacao += 1
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

#resultado final

    menu_decisao_final = """
    1. A lista de alunos foi substituída por uma nova lista durante a atualização.
    2. O sistema remove alunos antigos automaticamente após uma atualização.
    """

    print(menu_decisao_final)


    decisao_final = input("Qual é a causa do bug? ")
    if decisao_final == "1":
        print("Correto! Durante a atualização, a lista original de alunos foi substituída por uma nova lista contendo apenas o registro atualizado. Como os demais alunos não foram preservados, seus cadastros foram perdidos.")
        return True
        
    elif decisao_final == "2":
        print("Incorreto! O problema não está em uma remoção automática de alunos. A lista original foi substituída durante a atualização, causando a perda dos demais registros.")
        return False
    else:   
        print("Opção inválida. Por favor, escolha uma opção válida.")
        return False