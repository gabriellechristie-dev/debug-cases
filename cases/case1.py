import time

#narrativa inicial
def run_case1(): 
    print("O banco recebeu diversos relatos de clientes afirmando que seus saldos desapareciam após operações de depósito e saque...")
    time.sleep(2)
    print("Os valores pareciam ser redefinidos de forma inesperada, comprometendo a integridade do sistema financeiro...")
    time.sleep(2)
    print(" Sua missão é investigar o código e identificar o bug responsável pelo desaparecimento dos saldos...")
    time.sleep(2)

#código bugado
codigo_bugado1 = """ 
    saldo_inicial = 100
    valor_deposito = 50

    def depositar(saldo, valor):
        saldo = valor
        return saldo
    resultado = depositar(saldo_inicial, valor_deposito)
    print(f"Saldo após depósito: {resultado}")

"""
output = "Saldo após depósito: 50"

print(codigo_bugado1)
time.sleep(1)
print(output)

#menu de investigação
#mostrar opções
menu_case1 = """
1. Analisar variável saldo  
2. Testar depósito
""" 

print(menu_case1)

#receber escolha de investigação
escolha = input("Escolha uma opção para investigar: ")  
if escolha == "1":
    print("O valor armazenado no saldo parece não permanecer após a operação.")
elif escolha == "2":
    print("O valor final corresponde apenas ao último depósito realizado.")
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")

#decisão final (correção do bug)
menu_decisao_final = """
1. A variável saldo está sendo reinicializada dentro da função
2. O sistema está exibindo o resultado incorretamente

"""
print(menu_decisao_final)
#retorno do resultado 
decisao_final = input("Qual é a causa do bug? ")
if decisao_final == "1":
    print("Correto! A variável saldo está sendo reinicializada dentro da função, o que faz com que o valor anterior seja perdido.")
elif decisao_final == "2":
    print("Incorreto. O sistema está exibindo o resultado corretamente, mas o problema está na forma como a variável saldo é manipulada dentro da função.")
else:   
    print("Opção inválida. Por favor, escolha uma opção válida.")