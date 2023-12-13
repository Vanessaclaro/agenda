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
   idContato=input("Escolha o id do contato")
   nome=input("Escreva o nome do contato. ")
   telefoneinput("Digite o número do contato. ")
   return print(f'Cadastrar um contato: ') 
def deletarContato():
   print("Deletar contato:")
def buscarContatoPeloId():
   print("Buscar contato pelo id:")
  
def main():
   menu()
main()