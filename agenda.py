listaContato=[]

def menu():
   opcao=input('''
====================================
            Agenda Pessoal
Menu:
[1]Cadastrar contato
[2]Deletar contato
[3]Buscar contato pelo id
[4]Tarefas
[5]Compromissos
[6]Deletar tarefas
[7]Deletar Compromissos
=====================================
    Escolha uma opção acima.''')
   if opcao=="1":
      cadastrarContato()
   elif opcao=="2":
      deletarContato()
   else:
      buscarContatoPeloId()
def cadastrarContato():
   nome=input("Escreva o nome do contato. ")
   email=input("Digite o email do contato. ")
   telefone=input("Digite o número do contato. ")
   endereco=input("Digite o endereço do contato. ")
   try:
      agenda=open("agenda.txt","a")
      dados=f'{nome};{email};{telefone};{endereco}'
   except:
      print("Erro ao cadastrar contato.")

def deletarContato():
   print("Deletar contato:")
def buscarContatoPeloId():
   print("Buscar contato pelo id:")
  
def main():
   menu()
main()