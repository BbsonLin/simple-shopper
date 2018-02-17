from flask import current_app
from flask_restplus import Namespace, Resource, reqparse

from .schemas import MethodSchema
from .models import Method

ns = Namespace('method')

@ns.route('')
class MethodApi(Resource):

    def get(self):
        method_schema = MethodSchema(many=True)
        methods = Method.query.all()
        return method_schema.dump(methods)
