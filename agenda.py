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
   nome=input(f'Digite o nome do contato: ').upper()
   agenda=open("agenda.txt","r")
   for contato in agenda:
      if nome in contato.split(";")[0].upper():
         print(contato)
   agenda.close()
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
def compromissos():
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
   print("Apagar compromissos!")

def main():
   while True:
      menu()
main()