from flask import Flask, json, request  # , jsonify  # , json
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

tasks = [{'id': 0,
          'responsavel': 'Chris',
          'tarefa': 'Pragram in Python',
          'status': 'In Progress'},
         {'id': 1,
          'responsavel': 'Josue',
          'tarefa': 'Program in C',
          'status': 'Fail'}]


class Tasks_List_Index(Resource):
    def get(self, id):
        try:
            response = tasks[id]
        except IndexError:
            message = f'Person ID {id} does not exist!'
            response = {'status': 'error', 'message': message}
        except Exception:
            message = 'Error Unknown'
            response = {'status': 'error', 'message': message}
        return response

    def put(self, id):
        data = json.loads(request.data)
        print(data)
        tasks[id]['status'] = data
        return tasks[id]


api.add_resource(Tasks_List_Index, '/tasks/<int:id>/')


class Tasks(Resource):
    def get(self):
        return tasks
    # def post(self):


api.add_resource(Tasks, '/tasks/')


if __name__ == '__main__':
    app.run(debug=True)
