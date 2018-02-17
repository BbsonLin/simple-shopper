from app.extensions import ma

from .models import Store


class StoreSchema(ma.ModelSchema):
    class Meta:
        model = Store
        exclude = ('checks', )
