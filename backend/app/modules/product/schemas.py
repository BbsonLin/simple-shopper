from app.extensions import ma

from .models import Product, Category


class ProductSchema(ma.ModelSchema):
    class Meta:
        model = Product


class CategorySchema(ma.ModelSchema):
    class Meta:
        model = Category
        exclude = ('products', )
