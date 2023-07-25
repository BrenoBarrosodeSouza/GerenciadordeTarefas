import sqlite3

def showAll():
 conn=sqlite3.connect('tarefa.db')
 c=conn.cursor()

 c.execute("SELECT rowid,* FROM tarefas")
 items=c.fetchall()

 for item in items:
 	print(item)


 conn.commit()
 conn.close()

def add_one(titulo,descricao,status):
 conn=sqlite3.connect('tarefa.db')
 c=conn.cursor()
 c.execute("INSERT INTO tarefas VALUES (?,?,?)",(titulo,descricao,status))
 conn.commit()
 conn.close()

def delete_one(id):
 conn=sqlite3.connect('tarefa.db')
 c=conn.cursor()
 c.execute("DELETE FROM tarefas WHERE rowid = (?)",id)
 conn.commit()
 conn.close()

def status_update(id_tarefa, novo_status):
 conn = sqlite3.connect('tarefa.db')
 c = conn.cursor()

    # Verifica se a tarefa com o ID fornecido existe no banco de dados
 c.execute("SELECT rowid,* FROM tarefas WHERE rowid = ?", (id_tarefa,))
 tarefa = c.fetchone()

 if tarefa is None:
        print("Tarefa não encontrada. Verifique o ID informado.")
        
 else:

     c.execute("UPDATE tarefas SET status = ? WHERE rowid = ?", (novo_status, id_tarefa))
     print("Status da tarefa atualizado com sucesso.")
     conn.commit()
     conn.close()
 
