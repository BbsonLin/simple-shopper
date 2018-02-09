from app.extensions import ma

from .models import Product


class ProductSchema(ma.ModelSchema):
    class Meta:
        model = Product
