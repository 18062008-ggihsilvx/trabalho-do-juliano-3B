
from flask import Flask, render_template,request

app = Flask(__name__)

USUARIO_CORRETO = "adm"
SENHA_CORRETA = "1234"


@app.route("/")
def idex():
    return render_template("login.html")


@app.route("/login", methods=["post"])
def login():
    usuario = request.form.get("email")
    senha = request.form.get("password")

    if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
        return "<h1>Login efetuado com sucesso! Bem vindo</h1>"
    else:
        return   "<h1Usuario ou enhaincoretos. Tente novamente. <h1>"
    if __name__ == "__main__":
        app.run(debug=True)     

