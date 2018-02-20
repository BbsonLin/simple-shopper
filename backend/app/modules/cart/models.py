import json, time

from app.extensions import db, CRUDModel
from app.modules.user.models import User
from app.modules.store.models import Store
from app.modules.method.models import Method


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

    @classmethod
    def create(order_cls, **kwargs):
        new_order = order_cls(**kwargs)
        db.session.add(new_order)
        db.session.commit()
        return new_order


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

    @classmethod
    def list(order_detail_cls, **kwargs):
        many = kwargs.pop('many', False)
        order_detail_list = order_detail_cls.query.filter_by(**kwargs).all()
        if len(order_detail_list) > 1 or many is True:
            return order_detail_list
        elif len(order_detail_list) == 1:
            return order_detail_list[0]
        else:
            return None

    @classmethod
    def create(order_detail_cls, **kwargs):
        product_id = kwargs.get('id')
        if product_id:
            kwargs['product_id'] = kwargs.pop('id')
            kwargs.pop('name')
            kwargs.pop('price')
            new_order_detail = order_detail_cls(**kwargs)
            db.session.add(new_order_detail)
            db.session.commit()
            return new_order_detail
        else:
            raise AttributeError('Please set the required fields')



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

    @classmethod
    def list(check_cls, **kwargs):
        order_id = kwargs.pop('id', None)
        if order_id:
            return Check.query.filter_by(**kwargs).all()
        else:
            return None

    @classmethod
    def create(check_cls, **kwargs):
        order_id = kwargs.get('order_id')
        if order_id:
            kwargs['update_time'] = time.time()
            kwargs['user_id'] = kwargs.pop('userId')
            kwargs['method_id'] = kwargs.pop('methodId')
            kwargs['status_id'] = kwargs.pop('statusId')
            kwargs['store_id'] = kwargs.pop('storeId')
            new_check = check_cls(**kwargs)
            db.session.add(new_check)
            db.session.commit()
            return new_check
        else:
            raise AttributeError('Please set the required fields')

    def update(self, **kwargs):
        update_check_obj = Check(user_id=self.user_id, method_id=self.method_id,
                                 store_id=self.store.id, order_id=self.order_id,
                                 total=self.total, update_time=time.time(), status_id=kwargs['statusId'])
        db.session.add(update_check_obj)
        db.session.commit()
        return update_check_obj


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

    @staticmethod
    def insert_default():
        status = json.load(open('./seeds/status.json'))
        for s in status:
            status_obj = Status.create(**s)
