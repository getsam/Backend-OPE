from flask import Flask, render_template, redirect, request, session, flash, url_for
from model.models import Aluno, Usuario

app = Flask(__name__)
app.secret_key = 'sessao'  # Aqui definida uma chave para salvar a sessão do usuario

lista_alunos = []
@app.route('/')
def index():
    return render_template('login.html', titulo='login')

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima= url_for('novo'))) #chama a função login e passa a proxima pagina como parametro
    return render_template('aluno.html', titulo='Novo Aluno')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome'] #name de nome no formulario
    cpf = request.form['cpf']
    telefone = request.form['telefone']
    aluno = Aluno(nome, cpf, telefone)
    lista_alunos.append(aluno)
    return redirect(url_for('login'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')# variavel que foi definida no redirect
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    pass
    #aqui vai a logica que iremos usar para autenticar se o usuario esta no banco de dados 

app.run(debug=True)