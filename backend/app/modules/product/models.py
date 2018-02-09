import json

from app.extensions import db, CRUDModel


class Category(db.Model, CRUDModel):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))

    # One-to-Many
    products = db.relationship('Product', back_populates='category')

    def __repr__(self):
        return ("<{class_name}("
                "id='{self.id}', "
                "name='{self.name}"
                ")>".format(class_name=self.__class__.__name__, self=self))


class Product(db.Model, CRUDModel):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))
    image = db.Column(db.String(200))
    price = db.Column(db.Integer)
    discount = db.Column(db.Float)
    stock = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    # Many-to-One
    category = db.relationship('Category', back_populates='products')

    def __repr__(self):
        return ("<{class_name}("
                "id='{self.id}', "
                "name='{self.name}"
                ")>".format(class_name=self.__class__.__name__, self=self))

    @staticmethod
    def insert_default():
        categories = json.load(open('./products.json'))
        for cat_name, products in categories.items():
            cat_obj = Category.create(name=cat_name)
            for p in products:
                product_obj = Product.create(**p, category_id=cat_obj.id)
