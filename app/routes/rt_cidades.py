from flask import Blueprint, render_template
from app.services.srv_cidades import lista_cidades, detalhes_cidade

# cidades = Blueprint('cidades'), __name__, url_prefix="/cidades")
cidades = Blueprint('cidades', __name__)

@cidades.route("/")
def homepage():
    dados = lista_cidades()
    return render_template("home.html", lista_cidades=dados)

@cidades.route("/<int:cidade_id>")
def detalhes(cidade_id):
    detalhes = detalhes_cidade(cidade_id)
    return render_template("detalhes.html", dados=detalhes)