from flask import request, json
from flask_restful import Resource

hability_list = ['Python', 'PHP', 'C', 'Java']


class Habilities(Resource):
    def get(self):
        return hability_list

    def post(self):
        if json.loads(request.data) in hability_list:
            message = 'There is already an Hability with this name.'
            return {'status': 'Fail', 'message': message}
        else:
            data = json.loads(request.data)
            hability_list.append(data)
            return data


class Habilities_Index(Resource):
    def get(self, id):
        try:
            response = json.loads(request.data)
        except IndexError:
            message = f'Hability Index {id} Not Found'
            response = {'status': 'error', 'message': message}
        except Exception:
            message = 'Unknown Error'
            response = {'status': 'error', 'message': message}
        return response

    def put(self, id):
        if json.loads(request.data) in hability_list:
            message = 'There is already an Hability with this name.'
            return {'status': 'Fail', 'message': message}
        else:
            hability_list[id] = json.loads(request.data)
            return hability_list[id]

    def delete(self, id):
        hability_list.pop(id)
        return {'status': 'sucess', 'message': 'Hability Deleted'}


class Hability_Name(Resource):
    def get(self, name):
        if name in hability_list:
            return {'status': 'Congratulations', 'message': 'There Is An Hability With This Name!'}  # noqa: E501
        else:
            return {'status': 'Fail', 'message': 'It Has No Hability With That Name!'}  # noqa: E501
