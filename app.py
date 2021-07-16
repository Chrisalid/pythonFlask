from builtins import Exception, IndexError
from flask import Flask, json, jsonify, request
app = Flask(__name__)

pessoas = [
    {'id': 0,
     'nome': 'Chris',
     'doce': 'Chocolate'},
    {'id': 1,
     'nome': 'Maira',
     'doce': ['Chocolate', 'Bom-Bom', 'Chiclete']}
]


@app.route('/')
def hello():
    return 'Olá Mundo'


@app.route('/<int:id>')
def new(id):
    return jsonify({'id': id, 'nome': 'Chris', 'profissao': 'Programador'})


@app.route('/somar/<int:valor1>/<int:valor2>', methods=['GET'])
def somar(valor1, valor2):
    return jsonify({'soma': valor1 + valor2})


@app.route('/pes/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def pes(id):
    if request.method == 'GET':
        try:
            response = pessoas[id]
        except IndexError:
            message = f'Person ID {id} does not exist!'
            response = {'status': 'error', 'message': message}
        except Exception:
            message = 'Error Unknown'
            response = {'status': 'error', 'message': message}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        pessoas[id] = dados
        return jsonify(pessoas[id])
    elif request.method == 'DELETE':
        pessoas.pop(id)
        return jsonify({'status': 'sucess', 'message': 'Usuário Deletado!'})


@app.route('/pes/', methods=['GET', 'POST'])
def listapes():
    if request.method == 'POST':
        dados = json.loads(request.data)
        identify = len(pessoas)
        dados['id'] = identify
        pessoas.append(dados)
        return jsonify(pessoas[identify])
    elif request.method == 'GET':
        return jsonify(pessoas)


if __name__ == '__main__':
    app.run(debug=True)
