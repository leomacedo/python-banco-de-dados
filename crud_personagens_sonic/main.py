from database import (
    criar_tabela,
    adicionar_personagem,
    listar_personagens,
    atualizar_personagem,
    deletar_personagem,
    buscar_por_id
)


def menu():
    print("\n--- Banco de Dados do Universo Sonic 🌀 ---")
    print("1. Adicionar personagem")
    print("2. Listar todos")
    print("3. Atualizar personagem")
    print("4. Remover personagem")
    print("5. Sair")

def iniciar():
    criar_tabela()

    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do personagem: ")
            time = input("Time (Sonic, Dark, Chaotix, etc): ")
            tipo = input("Tipo (Speed, Power, Fly): ")
            cor = input("Cor predominante: ")
            poderes = input("Poderes: ")

            adicionar_personagem(nome, time, tipo, cor, poderes)
            print(f"{nome} adicionado com sucesso!")

        elif escolha == "2":
            personagens = listar_personagens()
            print("\n--- Lista de Personagens ---")
            for p in personagens:
                print(f"ID: {p[0]} | Nome: {p[1]} | Time: {p[2]} | Tipo: {p[3]} | Cor: {p[4]} | Poderes: {p[5]}")

        elif escolha == "3":
            try:
                id = int(input("ID do personagem a atualizar: "))
                personagem = buscar_por_id(id)

                if personagem:
                    nome = input("Novo nome: ")
                    time = input("Novo time: ")
                    tipo = input("Novo tipo: ")
                    cor = input("Nova cor: ")
                    poderes = input("Novos poderes: ")

                    atualizar_personagem(id, nome, time, tipo, cor, poderes)
                    print("✅ Personagem atualizado com sucesso!")
                else:
                    print("❌ ID não encontrado. Nenhuma atualização realizada.")
            except ValueError:
                print("⚠️  Entrada inválida. Por favor, digite um número.")

        elif escolha == "4":
            try:
                id = int(input("ID do personagem a remover: "))
                personagem = buscar_por_id(id)
                if personagem:
                    deletar_personagem(id)
                    print("🗑️ Personagem removido com sucesso!")
                else:
                    print("❌ ID não encontrado. Nenhuma exclusão realizada.")
            except ValueError:
                print("⚠️  Entrada inválida. Por favor, digite um número.")

        elif escolha == "5":
            print("Encerrando programa. Até mais!")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

# Inicia o sistema
iniciar()

