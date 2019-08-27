from flask import Flask, render_template, redirect, request, session, flash, url_for


app = Flask(__name__)

app.secret_key = 'sessao'  # Aqui definida uma chave para salvar a sessão do usuario

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

lista = []
aluno = Aluno('samuel',121212,12121221)
lista.append(aluno)

@app.route('/admin')
def admin():
    return render_template('lista.html', titulo='usuarios', usuarios=lista)  

@app.route('/')
def index():
    return render_template('login.html', titulo='login')

@app.route('/novo')
def novo():
  #chama a função login e passa a proxima pagina como parametro
    return render_template('aluno.html', titulo='Novo Aluno')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome'] #name de nome no formulario
    cpf = request.form['cpf']
    telefone = request.form['telefone']
    aluno = Aluno(nome, cpf, telefone)
    lista_alunos.append(aluno)
    return render_template('aluno.html')

@app.route('/login')
def login():
    proxima = request.args.get('proxima')# variavel que foi definida no redirect
    return render_template('login.html', proxima=proxima)

@app.route('/auth', methods=['POST'])
def autenticar():
    
    

app.run(debug=True)