import time
from visual import mostrar_titulo, mostrar_narrativa, mostrar_codigo, mostrar_output, mostrar_pistas, mostrar_diagnostico
from rich.console import Console
from textwrap import dedent

console = Console()

#narrativa inicial
def run_case3():
    console.print("")
    caso = """📂 CASO 3"""
    titulo_caso = "Login com Falha"

    narrativa = """Uma empresa relatou falhas no sistema de autenticação de usuários...
Somente os usuários com login e senha válidos deveriam conseguir acessar o sistema...
No entanto, pessoas sem as credenciais corretas estão conseguindo entrar normalmente...
Sua missão é investigar o código e descobrir por que o sistema está liberando acessos indevidos...
"""
    mostrar_titulo(titulo_caso, caso)
    time.sleep(2)
    mostrar_narrativa(narrativa)
    time.sleep(4)

#código bugado
    codigo_bugado = dedent("""
usuario_digitado = input("Digite seu usuário(Apenas letras): ")
senha_digitada = input(Digite sua senha(Apenas números): ")

usuario = "admin"
senha = "1234"

if usuario_digitado == usuario or senha_digitada == senha:
    print("Acesso liberado!")
else:
    print("Usuário ou senha incorretos")
""")

#output/comportamento observado 
    output_observado = """ 
    Tentativa 1:
    Usuário: admin
    Senha: 9999

    Acesso liberado!


    Tentativa 2:
    Usuário: joao
    Senha: 1234

    Acesso liberado!


    Tentativa 3:
    Usuário: admin
    Senha: 1234

    Acesso liberado!
    """
    mostrar_codigo(codigo_bugado)
    time.sleep(3)
    mostrar_output(output_observado)
    time.sleep(2)

#investigações
    menu_investigacao = """
1. Verificar validação de credenciais
2. Testar combinações de login e senha
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
                console.print("━━━━━━━━━━ 💡 PISTA ENCONTRADA ━━━━━━━━━━\n➜ A autenticação parece ser aprovada mesmo quando apenas uma dascredenciais está correta.", style ="bold cyan")
                console.print("")
                time.sleep(2)
                pista_vista1 = True
       
        elif escolha == 2:
            if pista_vista2 == True:
                console.print("⚠ Você já investigou essa pista.", style ="blink yellow")
                console.print("")
                time.sleep(2)
            else:
                console.print("━━━━━━━━━━ 💡 PISTA ENCONTRADA ━━━━━━━━━━\n➜Usuários conseguem acessar o sistema mesmo informando login ou senha incorretos.", style ="bold cyan")
                pista_vista2 = True
                time.sleep(2)
        else:
            console.print("Por favor, escolha a opção 1 ou 2!")
            console.print("")




#resultado final

    menu_decisao_final = """1. O operador lógico utilizado na validação está incorreto.
2. A senha cadastrada está armazenada incorretamente.
    """

    mostrar_diagnostico(menu_decisao_final)


    decisao_final = input("Qual é a causa do bug? ")
    time.sleep(2)
    if decisao_final == "1":
        console.print("━━━━━━━━━━ ✅ CASO RESOLVIDO ━━━━━━━━━━\n\nCAUSA IDENTIFICADA\n\nO sistema utiliza OR na validação em vez de AND. Dessa forma, basta que o usuário ou a senha estejam corretos para que o acesso seja liberado. O correto seria exigir que ambas as credenciais fossem válidas.\n\n🏆 Caso encerrado com sucesso.", style ="blink green")
        time.sleep(2)
        return True
    elif decisao_final == "2":
        console.print("━━━━━━━━━━ ❌ DIAGNÓSTICO INCORRETO ━━━━━━━━━━\n\nA senha está sendo comparada corretamente. O problema está na lógica utilizada para validar as credenciais.\n\n🔄 Reiniciando investigação...", style="blink red")
        time.sleep(2)
        return False
    else:   
        console.print("Opção inválida. Por favor, escolha uma opção válida.")
        return False