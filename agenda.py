listaContato=[]

def menu():
   opcao=input('''
====================================
            Agenda Pessoal
Menu:
[1]Cadastrar contato
[2]Deletar contato
[3]Buscar contato 
[4]Editar contato             
[5]Cadastrar Tarefas
[6]Deletar tarefas 
[7]Buscar Tarefas
[8]Editar Tarefas            
[9]Cadastrar Compromissos
[10]Deletar Compromissos
[11]Buscar Compromissos
[12]Editar Compromisso
=====================================
    Escolha uma opção acima. ''')
   if opcao=="1":
      cadastrarContato()   
   elif opcao=="2":
      deletarContato()
   elif opcao=="3":
      buscarContato()
   elif opcao=="4":
      editarContato()
   elif opcao=="5":
      cadastrarTarefas()
   elif opcao=="6":
      deletarTarefas()
   elif opcao=="7":
      buscarTarefas()
   elif opcao=="8":
      editarTarefas()
   elif opcao=="9":
      cadastrarCompromissos()
   elif opcao=="10":
      deletarCompromissos()
   elif opcao=="11":
      buscarCompromissos()
   elif opcao=="12":
      editarCompromisso()
   else:
      print("Opção errada!")

def cadastrarContato():
   nome=input("Escreva o nome do contato. ")
   email=input("Digite o email do contato. ")
   telefone=input("Digite o número do contato. ")
   endereco=input("Digite o endereço do contato. ")
   try:
      agenda=open("agenda.txt","a")
      dados=f'{nome};{email};{telefone};{endereco}\n'
      agenda.write(dados)
      agenda.close()
      print(f'Contato gravado com sucesso!')
   except:
      print("Erro ao cadastrar contato.")

def deletarContato():
   nomeDeletar = input("Digite o nome do contato que pretende excluir: ")
   agenda = open("agenda.txt","r")
   aux = []
   aux2 = []
   for i in agenda:
      aux.append(i)
   for i in range(0, len(aux)):
      if nomeDeletar not in aux[i]:
         aux2.append(aux[i])
   agenda = open("agenda.txt", "w")
   for i in aux2:
      agenda.write(i)
   print("Contato deletado com sucesso!!")

def buscarContato():
   nome=input(f'Digite o nome do contato: ').upper()
   agenda=open("agenda.txt","r")
   for contato in agenda:
      if nome in contato.split(";")[0].upper():
         print(contato)
   agenda.close()
def editarContato():
    nomeEditar = input("Digite o nome do contato que pretende editar: ")
    agenda = open("agenda.txt", "r")
    aux = []
    for i in agenda:
        aux.append(i)
    for i in range(len(aux)):
        if nomeEditar in aux[i]:
            novo_nome = input("Digite o novo nome: ")
            novo_email = input("Digite o novo email: ")
            novo_telefone = input("Digite o novo número de telefone: ")
            novo_endereco = input("Digite o novo endereço: ")
            aux[i] = f"{novo_nome};{novo_email};{novo_telefone};{novo_endereco}\n"
            print("Contato editado com sucesso!")
    agenda = open("agenda.txt", "w")
    for i in aux:
      agenda.write(i)
def cadastrarTarefas():
   descricao=input("Escreva a descrição da tarefa: ")
   data_Inicial=input("Digite a data de inicio: ")
   horario_Inicial=input("Digite o horário de inicio: ")
   data_Final=input("Digite a data de término: ")
   horario_Final=input("Digite o horário de término:")
   try:
      tarefa=open("tarefa.txt","a")
      dados=f'{descricao};{data_Inicial};{horario_Inicial};{data_Final};{horario_Final}\n'
      tarefa.write(dados)
      tarefa.close()
      print(f'Tarefa gravada com sucesso!')
   except:
      print("Erro ao cadastrar taferas.")
def deletarTarefas():
   tarefaDeletar = input("Digite qual tarefa pretende excluir: ")
   tarefa = open("tarefa.txt","r")
   lista = []
   lista2 = []
   for i in tarefa:
      lista.append(i)
   for i in range(0, len(lista)):
      if tarefaDeletar not in lista[i]:
         lista2.append(lista[i])
   tarefa = open("tarefa.txt", "w")
   for i in lista2:
      tarefa.write(i)
   print("Tarefa excluída com sucesso!") 
def buscarTarefas():
   nome=input(f'Digite o nome da tarefa: ').upper()
   tarefa=open("tarefa.txt","r")
   for taf in tarefa:
      if nome in taf.split(";")[0].upper():
         print(taf)
   tarefa.close()
def editarTarefas():
    nomeEditar = input("Digite a tarefa que pretende editar: ")
    tarefa = open("tarefa.txt", "r")
    aux = []
    for i in tarefa:
        aux.append(i)
    for i in range(len(aux)):
        if nomeEditar in aux[i]:
            descricao=input("Escreva a descrição da tarefa: ")
            data_Inicial=input("Digite a data de inicio: ")
            horario_Inicial=input("Digite o horário de inicio: ")
            data_Final=input("Digite a data de término: ")
            horario_Final=input("Digite o horário de término:")
            aux[i] = f"{descricao};{data_Inicial};{horario_Inicial};{data_Final};{horario_Final}\n"
            print("Tarefa editada com sucesso!")
    tarefa = open("tarefa.txt", "w")
    for i in aux:
     tarefa.write(i)
def cadastrarCompromissos():
   descricao=input("Escreva a descrição de seu compromisso: ")
   data=input("Digite a data: ")
   horario=input("Digite o horário: ")
   local=input("Digite o local: ")
   try:
      compromissos=open("compromissos.txt","a")
      dados=f'{descricao};{data};{horario};{local}\n'
      compromissos.write(dados)
      compromissos.close()
      print(f'Compromisso gravado com sucesso!')
   except:
      print("Erro ao cadastrar compromisso.")
def deletarCompromissos():
   compromissosDeletar = input("Digite qual compromisso pretende excluir: ")
   compromissos = open("compromissos.txt","r")
   lista = []
   lista2 = []
   for i in compromissos:
      lista.append(i)
   for i in range(0, len(lista)):
      if compromissosDeletar not in lista[i]:
         lista2.append(lista[i])
   compromissos = open("compromissos.txt", "w")
   for i in lista2:
      compromissos.write(i)
   print("Compromisso excluído com sucesso!") 
def buscarCompromissos():
   nome=input(f'Digite o nome do seu compromisso que deseja buscar: ').upper()
   compromissos=open("compromissos.txt","r")
   for compr in compromissos:
      if nome in compr.split(";")[0].upper():
         print(compr)
   compromissos.close()
def editarCompromisso():
    nomeEditar = input("Digite o compromisso que deseja editar: ")
    compromissos = open("compromissos.txt", "r")
    aux = []
    for i in compromissos:
        aux.append(i)
    for i in range(len(aux)):
        if nomeEditar in aux[i]:
            descricao=input("Escreva a descrição de seu novo compromisso: ")
            data=input("Digite a data: ")
            horario=input("Digite o horário: ")
            local=input("Digite o local: ")
            aux[i] = f"{descricao};{data};{horario};{local}\n"
            print("Compromisso editado com sucesso!")
    compromissos = open("compromissos.txt", "w")
    for i in aux:
     compromissos.write(i)

def main():
   while True:
      menu()
main()