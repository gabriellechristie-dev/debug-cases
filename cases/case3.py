import time

#narrativa inicial
def run_case3():
    print("Iniciando investigação do caso 3...")
    time.sleep(3)

    print("Uma empresa relatou falhas no sistema de autenticação de usuários...")
    time.sleep(3)

    print("Apenas usuários com login e senha válidos deveriam conseguir acessar o sistema...")
    time.sleep(3)

    print("No entanto, pessoas sem as credenciais corretas estão conseguindo entrar normalmente...")
    time.sleep(3)

    print("Sua missão é investigar o código e descobrir por que o sistema está liberando acessos indevidos.")
    time.sleep(4)

#código bugado
    codigo_bugado3 = """Código Bugado para análise:
    
    usuario_digitado = input(“Digite seu usuário(Apenas letras): ”)
    senha_digitada = input(“Digite sua senha(Apenas números): ”)

    usuario = “admin”
    senha = “1234”

    if usuario_digitado == usuario or senha_digitada == senha:
        print(“Acesso liberado!”)
    else:
        print(“Usuário ou senha incorretos”)

    """

#output/comportamento observado 
    output = """ Tentativa 1:
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
    print(codigo_bugado3)
    time.sleep(2)
    print(output)
    time.sleep(3)

#investigações
    menu_case3 = """ Menu de Pistas:
    1. Verificar validação de credenciais
    2. Testar combinações de login e senha
    """

#diagnóstico
    investigacao = 0
    while investigacao < 2:
        print(menu_case3)
        escolha = input("Escolha uma opção para investigar: ")  
        if escolha == "1":
            print("A autenticação parece ser aprovada mesmo quando apenas uma das credenciais está correta.")
            investigacao += 1
        elif escolha == "2":
            print("Usuários conseguem acessar o sistema mesmo informando login ou senha incorretos.")
            investigacao += 1
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

#resultado final

    menu_decisao_final3 = """
    1. O operador lógico utilizado na validação está incorreto.
    2. A senha cadastrada está armazenada incorretamente.
    """

    print(menu_decisao_final3)


    decisao_final3 = input("Qual é a causa do bug? ")
    if decisao_final3 == "1":
        print("Correto! O sistema utiliza OR na validação em vez de AND. Dessa forma, basta que o usuário ou a senha estejam corretos para que o acesso seja liberado. O correto seria exigir que ambas as credenciais fossem válidas.")
        return True
    elif decisao_final3 == "2":
        print("Incorreto! A senha está sendo comparada corretamente. O problema está na lógica utilizada para validar as credenciais.")
        return False
    else:   
        print("Opção inválida. Por favor, escolha uma opção válida.")
        return False