from flask import render_template
from flask_restplus import Api as BaseApi


class Api(BaseApi):
    def render_root(self):
        return render_template('index.html')


api = Api(title='AIWill Simple Shopper', doc=None)


def init_app(app, **kwargs):
    api.init_app(app)
