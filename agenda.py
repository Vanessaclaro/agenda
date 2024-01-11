listaContato=[]

def menu():
   opcao=input('''
====================================
            Agenda Pessoal
Menu:
[1]Cadastrar contato
[2]Deletar contato
[3]Buscar contato 
[4]Tarefas
[5]Deletar tarefas              
[6]Compromissos
[7]Deletar Compromissos
=====================================
    Escolha uma opção acima.''')
   if opcao=="1":
      cadastrarContato()

      opcao2=input('''
      =========================================
                  Agenda Pessoal
      Menu:
      [1] Deletar contato
      [2] Editar Contato
      [3] Mostrar Contato
      =========================================
         Escolha uma opção acima: ''')
      if opcao2 == "1":
         deletarcontato()
      print("Você deletou o contato.")

         
   elif opcao=="2":
      deletarContato()
   elif opcao=="3":
      buscarContato()
   elif opcao=="4":
      tarefas()
   elif opcao=="5":
      deletarTarefas()
   elif opcao=="6":
      compromissos()
   elif opcao=="7":
      deletarCompromissos()
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
   print("Buscar contato pelo id:")
def tarefas():
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
      print("Erro ao cadastrar contato.")
   print("Anotar tarefas. ")
def deletarTarefas():
   print("Excluir tarefas!")  
def compromissos():
   print("Anotar Compromissos. ")
def deletarCompromissos():
   print("Apagar compromissos!")

def main():
   while True:
      menu()
main()