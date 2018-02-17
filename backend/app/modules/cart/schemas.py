from marshmallow import post_dump
from app.extensions import ma
from app.modules.product.schemas import ProductSchema

from .models import Order, OrderDetail, Check


class OrderSchema(ma.ModelSchema):
    class Meta:
        model = Order


class OrderDetailSchema(ma.ModelSchema):
    class Meta:
        model = OrderDetail

    product = ma.Nested(ProductSchema, many=True)

class CheckSchema(ma.ModelSchema):
    class Meta:
        model = Check
