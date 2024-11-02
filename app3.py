def adicionar_contato(agenda):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    contato = {"nome": nome, "telefone": telefone, "email": email}
    agenda.append(contato) 

    print("Contato adicionado com sucesso!") 

def buscar_contato(agenda, nome):
    for contato in agenda:
        if contato["nome"] == nome:
            print(contato)
            return
    print("Contato não encontrado.")

def remover_contato(agenda, nome):
    for i, contato in enumerate(agenda):
        if contato["nome"] == nome:
            del agenda[i]
            print("Contato removido com sucesso!")
            return
    print("Contato não encontrado.")

def imprimir_agenda(agenda):
    for contato in agenda:
        print(contato)

agenda = []

while True:
    print("\n--- Agenda Telefônica ---")
    print("1. Adicionar contato")
    print("2. Buscar contato")
    print("3. Remover contato")
    print("4. Imprimir agenda")
    print("5. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        adicionar_contato(agenda)
    elif opcao == '2':
        nome = input("Digite o nome do contato a ser buscado: ")
        buscar_contato(agenda, nome)
    elif opcao == '3':
        nome = input("Digite o nome do contato a ser removido: ")
        remover_contato(agenda, nome)
    elif opcao == '4':
        imprimir_agenda(agenda)
    elif opcao == '5':
        break
    else:
        print("Opção inválida.")