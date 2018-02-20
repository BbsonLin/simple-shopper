import json

from app.extensions import db, CRUDModel


class Store(db.Model, CRUDModel):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(db.String(50))
    value = db.Column(db.String(50))

    # One-to-many
    checks = db.relationship('Check', back_populates='store')

    def __repr__(self):
        return ("<{class_name}("
                "id='{self.id}',"
                "name='{self.value}',"
                ")>".format(class_name=self.__class__.__name__, self=self))

    @staticmethod
    def insert_default():
        stores = json.load(open('./seeds/stores.json'))
        for store in stores:
            Store.create(**store)
