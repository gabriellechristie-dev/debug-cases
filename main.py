import menu
from cases import case1

while True:
    choice = menu.menu()

    if choice == "1":
        resultado = case1.run_case1()
       
        if resultado == True:
            print("Parabéns! Você resolveu o caso com sucesso!")
        else:
            print("Ops! Parece que a solução não está correta. Tente novamente.")
    elif choice == "2":
        print("Saindo do jogo...")
        break
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")
        
menu()
