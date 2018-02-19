from flask import current_app
from flask_restplus import Namespace, Resource, reqparse

from .schemas import StoreSchema
from .models import Store

ns = Namespace('store')

@ns.route('')
class StoreApi(Resource):

    def get(self):
        store_schema = StoreSchema(many=True)
        stores = Store.list()
        return store_schema.dump(stores)
