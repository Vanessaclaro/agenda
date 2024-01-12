import pytest
from agenda import cadastrarContato
def test_cadastrarContato(mocker, capsys):
    
 mocker.patch('builtins.input', side_effect=['João', 'joao@email.com', '123456789', 'Rua A'])
    
cadastrarContato()

captured = capsys.readouterr()
assert('Contato gravado com sucesso')


