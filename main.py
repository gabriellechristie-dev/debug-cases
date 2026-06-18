import menu
import time
from cases import case1, case2, case3, case4, case5

while True:
    choice = menu.menu()
    
    if choice == 1:

        resultado = case1.run_case1()
        while resultado == False:
            
            time.sleep(2)
           
            resultado = case1.run_case1()
        time.sleep(2)

      
        resultado = case2.run_case2()
        while resultado == False:
            
            time.sleep(2)
            
            resultado = case2.run_case2()
       
        time.sleep(2)
        
        resultado = case3.run_case3()
        while resultado == False:
           
            time.sleep(2)
           
            resultado = case3.run_case3()
     
        time.sleep(2)

        resultado = case4.run_case4()
        while resultado == False:
           
            time.sleep(2)
            
            resultado = case4.run_case4()
       
        time.sleep(2)

        resultado = case5.run_case5()
        while resultado == False:
            
            time.sleep(2)
           
            resultado = case5.run_case5()
       
        time.sleep(2)

        print("===================================")
        print("CASO ENCERRADO")
        print("===================================")
        print("Parabéns, Investigador!")
        print("Você solucionou todos os casos de debug da campanha.")
        print("Variáveis, loops, condicionais, listas e funções não são mais um mistério para você.")
        print("Todos os sistemas foram restaurados com sucesso.")
        print("===================================")
        time.sleep(2)

    elif choice == 2:
        print("Saindo do jogo...") 
        break 
    else:
        print("Opção inválida. Por favor, escolha 1 para Jogar ou 2 para Sair.")
