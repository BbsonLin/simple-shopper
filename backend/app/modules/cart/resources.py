from flask import abort, request, current_app
from flask_restplus import Namespace, Resource, reqparse

from .models import Order
from .schemas import OrderSchema

ns = Namespace('cart', description='Cart APIs')

order_argparser = reqparse.RequestParser()
order_argparser.add_argument('id', type=int, store_missing=False)


@ns.route('')
class OrderApi(Resource):

    def get(self):
        args = order_argparser.parse_args()
        current_app.logger.debug('Order GET request: {}'.format(args))
        order_schema = OrderSchema()

        order_obj = Order.list(**args)
        if isinstance(order_obj, list):
            return order_schema.dump(order_obj, many=True)
        else:
            return order_schema.dump(order_obj)

    def post(self):
        args = order_argparser.parse_args()
        current_app.logger.debug('Order POST request: {}'.format(args))
        order_schema = OrderSchema()
        order_obj = Order.create()
        return order_schema.dump(order_obj)
