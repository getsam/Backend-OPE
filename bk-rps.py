from flask import Flask, render_template, redirect, request, session, flash, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login')
def login():
    proxima = request.args.get('proxima')# variavel que foi definida no redirect
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    pass
    #aqui vai a logica que iremos usar para autenticar se o usuario esta no banco de dados 

app.run(debug=True)