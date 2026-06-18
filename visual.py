from rich.console import Console
from rich.panel import Panel
from rich import box
from rich.rule import Rule
from rich.align import Align
from rich.syntax import Syntax 

console = Console()


def mostrar_titulo(titulo_caso,caso):
    panel = Panel(Align.center(titulo_caso), title = caso, box = box.DOUBLE )
    console.print(panel)
   


def mostrar_narrativa(narrativa):
    console.print("")
    console.print("")
    rule = Rule( title="📋 RELATÓRIO DO CASO", style = "cyan")
    console.print(rule)
    console.print(narrativa)
    


def mostrar_codigo(codigo_bugado):
    console.print("")
    console.print("")
    rule =  Rule(title="💻 CÓDIGO SUSPEITO" , style = "blue")
    syntax = Syntax(codigo_bugado, "python")
    console.print(rule)
    console.print(syntax)
    

def mostrar_output(output_observado):
    console.print("")
    console.print("")
    rule = Rule(title="🖥 COMPORTAMENTO OBSERVADO", style = "yellow")
    console.print(rule)
    console.print(output_observado)


    
def mostrar_pistas(menu_investigacao):
    console.print("")
    console.print("")
    rule = Rule(title="🔍 PISTAS DISPONÍVEIS", style = "magenta")
    console.print(rule)
    console.print(menu_investigacao)


def mostrar_diagnostico(menu_decisao_final):
    console.print("")
    console.print("")
    rule = Rule(title="🕵 DIAGNÓSTICO FINAL" , style = "red")
    console.print(rule)
    console.print(menu_decisao_final)

def mostrar_tela_inicial():
    cabecalho = "DEBUG CASES"

    boas_vindas = """
Bem-vindo, Investigador.
Hoje a sua missão é analisar sistemas defeituosos,
coletar pistas e descobrir a causa dos bugs!""" 

    opcoes = """
1.Iniciar Investigação
2.Sair """
    
    panel = Panel(Align.center(cabecalho), box.DOUBLE)
    console.print(panel)
    console.print(boas_vindas)
    console.print(opcoes)


    panel = Panel("💡 PISTA ENCONTRADA \n\n O valor armazenado no saldo parece não permanecer após a operação.", box.SIMPLE, expand = False)