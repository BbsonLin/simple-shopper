from marshmallow import post_dump
from app.extensions import ma
from app.modules.product.schemas import ProductSchema
from app.modules.method.schemas import MethodSchema
from app.modules.store.schemas import StoreSchema

from .models import Order, OrderDetail, Check, Status


class OrderDetailSchema(ma.ModelSchema):
    class Meta:
        model = OrderDetail

class StatusSchema(ma.ModelSchema):
    class Meta:
        model = Status

class CheckSchema(ma.ModelSchema):
    class Meta:
        model = Check

    method = ma.Nested(MethodSchema)
    store = ma.Nested(StoreSchema)
    status = ma.Nested(StatusSchema)

class OrderSchema(ma.ModelSchema):
    class Meta:
        model = Order

    order_details = ma.Nested(OrderDetailSchema, many=True)
    checks = ma.Nested(CheckSchema, many=True)
