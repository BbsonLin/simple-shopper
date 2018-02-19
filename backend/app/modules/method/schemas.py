from app.extensions import ma

from .models import Method


class MethodSchema(ma.ModelSchema):
    class Meta:
        model = Method
        exclude = ('checks', )
