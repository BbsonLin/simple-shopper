from marshmallow import post_dump
from app.extensions import ma
from app.modules.product.schemas import ProductSchema

from .models import Order, OrderDetail, Check


class OrderDetailSchema(ma.ModelSchema):
    class Meta:
        model = OrderDetail

class CheckSchema(ma.ModelSchema):
    class Meta:
        model = Check

class OrderSchema(ma.ModelSchema):
    class Meta:
        model = Order

    order_details = ma.Nested(OrderDetailSchema, many=True)
    checks = ma.Nested(CheckSchema, many=True)
