from flask import Flask # classe para instanciar a aplicação web
import os

def criar_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SK', 'dev-inseguro')

# importar blueprints
# from app.routes.rt_cidades import cidades

# registrar bluebrints
# app.register_blueprint(cidades)

    return app