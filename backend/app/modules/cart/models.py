from app.extensions import db, CRUDModel
from app.modules.user.models import User


class Order(db.Model, CRUDModel):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # One-to-Many
    order_details = db.relationship('OrderDetail', back_populates='order')
    checks = db.relationship('Check', back_populates='order')

    def __repr__(self):
        return ("<{class_name}("
                "id='{self.id}',"
                ")>".format(class_name=self.__class__.__name__, self=self))

    @classmethod
    def list(order_cls, **kwargs):
        order_id = kwargs.pop('id', None)
        if order_id:
            return Order.query.filter_by(id=order_id).all()
        else:
            return None


class OrderDetail(db.Model, CRUDModel):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.Integer)
    subtotal = db.Column(db.Integer)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    # Many-to-one
    order = db.relationship('Order', back_populates='order_details')
    product = db.relationship('Product', back_populates='order_details')

    def __repr__(self):
        return ("<{class_name}("
                "id='{self.id}',"
                ")>".format(class_name=self.__class__.__name__, self=self))


class Check(db.Model, CRUDModel):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    update_time = db.Column(db.Integer, default=0)
    total = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    method_id = db.Column(db.Integer, db.ForeignKey('method.id'))
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'))
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))

    # Many-to-one
    user = db.relationship('User', back_populates='checks')
    method = db.relationship('Method', back_populates='checks')
    status = db.relationship('Status', back_populates='checks')
    store = db.relationship('Store', back_populates='checks')
    order = db.relationship('Order', back_populates='checks')

    def __repr__(self):
        return ("<{class_name}("
                "id='{self.id}',"
                ")>".format(class_name=self.__class__.__name__, self=self))


class Method(db.Model, CRUDModel):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))

    # One-to-many
    checks = db.relationship('Check', back_populates='method')

    def __repr__(self):
        return ("<{class_name}("
                "id='{self.id}',"
                "name='{self.name}',"
                ")>".format(class_name=self.__class__.__name__, self=self))


class Status(db.Model, CRUDModel):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))

    # One-to-many
    checks = db.relationship('Check', back_populates='status')

    def __repr__(self):
        return ("<{class_name}("
                "id='{self.id}',"
                "name='{self.name}',"
                ")>".format(class_name=self.__class__.__name__, self=self))


class Store(db.Model, CRUDModel):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))

    # One-to-many
    checks = db.relationship('Check', back_populates='store')

    def __repr__(self):
        return ("<{class_name}("
                "id='{self.id}',"
                "name='{self.name}',"
                ")>".format(class_name=self.__class__.__name__, self=self))
