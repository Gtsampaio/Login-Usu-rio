from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'Senha-Secreta'


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	msg_erro = ''
	if request.method == 'POST':
		usuario = request.form.get('usuario')
		senha = request.form.get('senha')
		if usuario == 'gustavo' and senha == 'sampaio123':
			session['usuario'] = 'gustavo'
			return redirect('/area_logada')
		else:
			msg_erro = 'Usuário e/ou senha inválidos'
	return render_template('login.html', erro=msg_erro)


@app.route('/area_logada')
def area_logada():
	if 'usuario' in session:
		nome_usuario = ''
		media_usuario = 0.0
		if session['usuario'] == 'gustavo':
			nome_usuario = 'Gustavo Sampaio'
			media_usuario = 10
		return render_template('area_logada.html', nome=nome_usuario, media=media_usuario)
	else:
		return redirect('/login')


@app.route('/sair')
def sair():
	session.clear()
	return redirect('/login')


if __name__ == '__main__':
	app.run(debug=True)