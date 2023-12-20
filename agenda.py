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

   print("Deletar contato:::")
def buscarContato():
   print("Buscar contato pelo id:")
def tarefas():
   print("Anotar tarefas. ")
def deletarTarefas():
   print("Excluir tarefas!")  
def compromissos():
   print("Anotar Compromissos. ")
def deletarCompromissos():
   print("Apagar compromissos!")

def main():
   menu()
main()