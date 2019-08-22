class Aluno:
    def __init__(self, nome, cpf, telefone): #atributos pra teste depois iremos incluir mais
        self.__nome = nome #aqui o __ deixa o atributo privado
        self.__cpf = cpf # sendo necessario getter e setter para buscar os atributos, se quiser pode tirar 
        self.__telefone = telefone

class Usuario:
    def __init__(self, nome_user, senha, aluno):
        self.__nome_user = nome_user
        self.__senha = senha
        self.__aluno = Aluno
    