import sys;sys.path.append("..")#trabalho bem feito = inveja pesada

from flask import Flask

from config import productionConfig, devConfig
from server import app

def create_app():
    api = Flask(__name__)
    api.register_blueprint(app)
    api.config.from_object(productionConfig(api))

    return api

if __name__=="__main__":
    app=create_app()
    app.config.from_object(devConfig(app))
    app.run(host='127.0.0.1', port=5000)