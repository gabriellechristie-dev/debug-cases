from visual import mostrar_tela_inicial
from rich.prompt import IntPrompt
from rich.console import Console

console = Console()

def menu():
    
    mostrar_tela_inicial()
    console.print("")
    choice = IntPrompt.ask("Escolha uma opção: ")
    
    return choice

