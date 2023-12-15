
from agenda import cadastrarContato
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
