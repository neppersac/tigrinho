from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "sua_chave_secreta"

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Aqui você pode adicionar a lógica de autenticação
        if username == "admin" and password == "1234":  # Exemplo simples
            flash("Login bem-sucedido!", "success")
            return redirect(url_for('index'))
        else:
            flash("Usuário ou senha incorretos.", "danger")
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
