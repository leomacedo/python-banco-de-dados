from database import criar_tabela

def menu():
    print("\n--- Banco de Dados do Universo Sonic 🌀 ---")
    print("1. Adicionar personagem")
    print("2. Listar todos")
    print("3. Buscar por ID")
    print("4. Atualizar personagem")
    print("5. Remover personagem")
    print("6. Sair")

def iniciar():
    criar_tabela()
    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "6":
            print("Encerrando programa. Até mais!")
            break
        else:
            print("Função ainda em desenvolvimento.\n")  # Colocaremos as funções depois

iniciar()
