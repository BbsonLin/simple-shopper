from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate(db=db)


def init_app(app):
    for extension in (db, ma, migrate):
        extension.init_app(app)


class CRUDModel(object):

    @classmethod
    def list(m_cls, **kwargs):
        many = kwargs.pop('many', False)
        obj_list = m_cls.query.filter_by(**kwargs).all()
        if len(obj_list) > 1 or many is True:
            return obj_list
        elif len(obj_list) == 1:
            return obj_list[0]
        else:
            return None

    @classmethod
    def create(m_cls, **kwargs):
        new = m_cls(**kwargs)
        db.session.add(new)
        db.session.commit()
        return new

    def update(self, **kwargs):
        for kwarg in kwargs:
            update_value = kwargs.get(kwarg)
            if update_value:
                setattr(self, kwarg, update_value)
        db.session.commit()
        return self

    @classmethod
    def delete(m_cls, ids):
        if ids:
            obj_list = list()
            for id in ids:
                obj = m_cls.query.filter_by(id=id).first()
                db.session.delete(obj)
                obj_list.append({'id': obj.id})
            db.session.commit()
            return obj_list
        else:
            raise AttributeError('Please set the required fields')
