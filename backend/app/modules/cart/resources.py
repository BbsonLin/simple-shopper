from flask import abort, request, current_app
from flask_restplus import Namespace, Resource, reqparse

from .models import Order, OrderDetail, Check
from .schemas import OrderSchema, OrderDetailSchema, CheckSchema

ns = Namespace('cart', description='Cart APIs')

order_argparser = reqparse.RequestParser()
order_argparser.add_argument('user', type=int, store_missing=False)
order_argparser.add_argument('method', type=int, store_missing=False)
order_argparser.add_argument('store', type=int, store_missing=False)


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
        args = request.get_json()
        current_app.logger.debug('Order POST request: {}'.format(args))
        order_schema = OrderSchema()
        order_obj = Order.create()
        order_detail = args.pop('products', [])
        for detail in order_detail:
            order_detail_schema = OrderDetailSchema()
            order_detail_obj = OrderDetail.create(**detail, order_id=order_obj.id)

        check_schema = CheckSchema()
        check_obj = Check.create(**args, order_id=order_obj.id)

        return order_schema.dump(order_obj)
