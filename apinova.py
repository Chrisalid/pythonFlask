# from builtins import Exception, IndexError
from flask import Flask, json, jsonify, request
import os
app = Flask(__name__)

tasks = [{'id': 0,
          'responsavel': 'Chris',
          'tarefa': 'Pragram in Python',
          'status': 'In Progress'},
         {'id': 1,
          'responsavel': 'Josue',
          'tarefa': 'Program in C',
          'status': 'Fail'}]


@app.route('/')
def begin():
    return 'Hello '+os.system.__name__


@app.route('/tasks/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def task_list_index(id):
    if request.method == 'GET':
        try:
            response = tasks[id]
        except IndexError:
            message = f'Person ID {id} does not exist!'
            response = {'status': 'error', 'message': message}
        except Exception:
            message = 'Error Unknown'
            response = {'status': 'error', 'message': message}
        return jsonify(response)
    elif request.method == 'PUT':
        data = json.loads(request.data)
        print(data)
        tasks[id]['status'] = data
        return jsonify(tasks[id])
    elif request.method == 'DELETE':
        tasks.pop(id)
        return jsonify({'status': 'sucess', 'message': 'User Deleted!'})


@app.route('/tasks/', methods=['GET', 'POST'])
def tasks_list():
    if request.method == 'POST':
        data = json.loads(request.data)
        identity = len(tasks)
        data['id'] = identity
        tasks.append(data)
        return jsonify(tasks[identity])
    elif request.method == 'GET':
        return jsonify(tasks)


if __name__ == '__main__':
    app.run(debug=True)
