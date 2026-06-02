import menu
import time
from cases import case1, case2

while True:
    choice = menu.menu()
    
    if choice == "1":
        resultado = case1.run_case1()
        while resultado == False:
            print("Ops! Parece que a solução não está correta. Tente novamente.")
            time.sleep(3)
            print("Reiniciando investigação do caso 1...")
            resultado = case1.run_case1()
        print("Parabéns! Você resolveu o caso com sucesso!")
        time.sleep(2)
        resultado = case2.run_case2()

        while resultado == False:
            print("Ops! Parece que a solução não está correta. Tente novamente.")
            time.sleep(3)
            print("Reiniciando investigação do caso 2...")
            resultado = case2.run_case2()
        print("Parabéns! Você resolveu o caso com sucesso!")
        time.sleep(2)
        #caso3
    elif choice == "2":
        print("Saindo do jogo...") 
        break 
    
