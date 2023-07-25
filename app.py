import database

while True:
    print("\n1-Criar tarefa\n2-Visualizar tarefas\n3-Excluir tarefa\n4-Atualizar tarefa\n5-Sair\n")
    opcao = input()
    if opcao == "1":
        print("Qual o título da tarefa?")
        titulo = input()
        print("Qual a descrição da tarefa?")
        descricao = input()
        print("Qual o status da tarefa?")
        status = input()
        database.add_one(titulo, descricao, status)

    if opcao == "2":
        database.showAll()

    if opcao == "3":
        database.showAll()
        print("\nSelecione o id da tarefa que deseja excluir:")
        tarefaId = input()
        database.delete_one(tarefaId)

    if opcao == "4":
        print("\nSelecione o id da tarefa que deseja atualizar:")
        idStatus = input()
        print("Qual o novo status da tarefa?")
        novoStatus = input()
        database.status_update(idStatus, novoStatus)


    if opcao == "5":
        break