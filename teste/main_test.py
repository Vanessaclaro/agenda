from agenda import cadastrarContato
def test_cadastrarContato():
    contato=cadastrarContato('')

    assert contato.nome=='Vanessa'
    assert contato.email=='va@gmail.com'
    



