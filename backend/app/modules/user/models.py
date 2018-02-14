from app.extensions import db, CRUDModel


class User(db.Model, CRUDModel):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))

    # One-to-many
    checks = db.relationship('Check', back_populates='User')

    def __repr__(self):
        return ("<{class_name}("
                "id='{self.id}',"
                "name='{self.name}',"
                ")>".format(class_name=self.__class__.__name__, self=self))
