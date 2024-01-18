from agenda import cadastrarContato
def test_cadastrarContato():
    contato=cadastrarContato('Vanessa','va@gamil.com',899999,'rua n48')

    assert contato.nome=='Vanessa'
    assert contato.email=='va@gmail.com'
    



