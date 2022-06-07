from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/stone", methods=['GET', 'POST'])
def stone():
    return "<p>Hello, Stone-World!</p>"

# por padrão, o método será GET. No momento que colocou o método "POST", acessar a página vai causar um erro 405
# pode por vários métodos - forma de array


@app.route("/cliente", methods=['PUT'])
def atualizar_cliente():
    return "<p>Hello, Stone-World!</p>"


@app.route("/veiculo", methods=['DELETE'])
def deletar_veiculo():
    return "<p>Hello, Stone-World!</p>"
