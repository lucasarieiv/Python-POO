from pessoa import Pessoa

# /pessoa
# POST body = {nome: 'Lucas', idade: 21}

_args = {'nome': 'Lucas', 'idade': 21}


pessoa = Pessoa(_args['nome'], _args['idade'])

print(pessoa.save())
