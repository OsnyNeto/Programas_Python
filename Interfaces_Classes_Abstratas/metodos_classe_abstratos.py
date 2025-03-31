class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod # Usado com contexto de classe
    def criar_de_data_nascimento(cls, nome, ano,mes,dia):
        idade = 2025 - ano
        return cls(nome, idade)
    
    @staticmethod # Usado sem contexto de classe
    def e_maior_idade(idade):
        return idade >= 18
    

pessoa1 = Pessoa("João\t", 25)
print(pessoa1.nome, pessoa1.idade)

pessoa2 = Pessoa.criar_de_data_nascimento("Maria\t", 1977, 1, 1)
print(pessoa2.nome, pessoa2.idade)

print(Pessoa.e_maior_idade(25))
print(Pessoa.e_maior_idade(15))