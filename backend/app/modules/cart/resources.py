from flask import abort, request, current_app
from flask_restplus import Namespace, Resource, reqparse

from .models import Order, OrderDetail, Check
from .schemas import OrderSchema, OrderDetailSchema, CheckSchema

ns = Namespace('cart', description='Cart APIs')

order_argparser = reqparse.RequestParser()
order_argparser.add_argument('id', type=int, store_missing=False)

order_patch_argparser = reqparse.RequestParser()
order_patch_argparser.add_argument('id', type=int, store_missing=False)
order_patch_argparser.add_argument('userId', type=int, store_missing=False)
order_patch_argparser.add_argument('methodId', type=int, store_missing=False)
order_patch_argparser.add_argument('storeId', type=int, store_missing=False)
order_patch_argparser.add_argument('statusId', type=int, store_missing=False)


@ns.route('')
class OrderApi(Resource):

    def get(self):
        args = order_argparser.parse_args()
        current_app.logger.debug('Order GET request: {}'.format(args))
        order = Order.list(**args, many=True)
        order_schema = OrderSchema(many=True)

        return order_schema.dump(order)

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

    def patch(self):
        args = order_patch_argparser.parse_args()
        current_app.logger.debug('Order PATCH request: {}'.format(args))
        order_id = args.get('id')

        if order_id is not None:
            check_obj = Check.query.filter_by(id=order_id, status_id=args['statusId']).first()
            if check_obj:
                abort(400, 'This check has already exist')
            else:
                check_obj = Check.query.filter_by(id=order_id).first()
                update_check_obj = check_obj.update(**args)
                order_schema = OrderSchema()
                order_obj = Order.query.filter_by(id=order_id).first()
                return order_schema.dump(order_obj)
