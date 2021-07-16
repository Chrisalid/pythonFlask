from flask import Flask, json, request
from flask_restful import Resource, Api
from habilities import Habilities, Habilities_Index, Hability_Name
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
    '''Find Tasks Through Indexes

    After finding the task, make one
    of the GET, PUT or DELETE requests.
    '''
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

    def delete(self, id):
        tasks.pop(id)
        return {'status': 'sucess', 'message': 'User Deleted!'}


class Tasks(Resource):
    '''Returns The Tasks List

    Return tasks and perform a GET or POST request.
    '''
    def get(self):
        return tasks

    def post(self):
        data = json.loads(request.data)
        id = len(tasks)
        data['id'] = id
        tasks.append(data)
        return tasks[id]


api.add_resource(Tasks_List_Index, '/tasks/<int:id>/')
api.add_resource(Tasks, '/tasks/')
api.add_resource(Habilities, '/habilities/')
api.add_resource(Habilities_Index, '/habilities/<int:id>/')
api.add_resource(Hability_Name, '/habilities/<name>/')


if __name__ == '__main__':
    app.run(debug=True)
