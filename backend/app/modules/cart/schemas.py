from app.extensions import ma

from .models import Order


class OrderSchema(ma.ModelSchema):
    class Meta:
        model = Order
