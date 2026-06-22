from flask import Blueprint, render_template
from app.services.srv_cidades import lista_cidades

# cidades = Blueprint('cidades'), __name__, url_prefix="/cidades")
cidades = Blueprint('cidades', __name__)

@cidades.route("/")
def homepage():
    dados = lista_cidades()
    return render_template("home.html", lista_cidades=dados)