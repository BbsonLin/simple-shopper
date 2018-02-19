import json

from app.extensions import db, CRUDModel


class Method(db.Model, CRUDModel):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(db.String(50))
    value = db.Column(db.String(50))

    # One-to-many
    checks = db.relationship('Check', back_populates='method')

    def __repr__(self):
        return ("<{class_name}("
                "id='{self.id}',"
                "name='{self.value}',"
                ")>".format(class_name=self.__class__.__name__, self=self))

    @staticmethod
    def insert_default():
        methods = json.load(open('./seeds/methods.json'))
        for method in methods:
            method_obj = Method.create(**method)
