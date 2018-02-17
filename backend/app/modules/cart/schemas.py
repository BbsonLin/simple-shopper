from app.extensions import ma
from app.modules.product.schemas import ProductSchema

from .models import Order, OrderDetail


class OrderSchema(ma.ModelSchema):
    class Meta:
        model = Order


class OrderDetailSchema(ma.ModelSchema):
    class Meta:
        model = OrderDetail

    product = ma.Nested(ProductSchema, many=True)
