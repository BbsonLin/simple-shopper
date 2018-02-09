from flask import current_app
from flask_restplus import Namespace, Resource, reqparse

from app.modules.product.models import Category
from .schemas import ProductSchema

ns = Namespace('product')

product_argparser = reqparse.RequestParser()
product_argparser.add_argument('name', type=str, store_missing=False)


@ns.route('')
class ProductApi(Resource):

    def get(self):
        args = product_argparser.parse_args()
        current_app.logger.debug('Product GET request: {}'.format(args))
        cat = Category.list(**args)
        product_schema = ProductSchema(many=True)
        if cat:
            return product_schema.dump(cat.products)

        return 'Product GET'
