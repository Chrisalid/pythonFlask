from flask import Flask, jsonify, json
from flask_restful import Resource, Api 
app = Flask(__name__)
api = Api(app)


class Desenvolvedor(Resource):
    def get(self):
        return {'nome': 'Chris'}


if __name__ == '__main__':
    app.run()
