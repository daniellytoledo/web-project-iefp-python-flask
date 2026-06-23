from app.models.rep_cidades import select_todas_cidades, select_cidade
from pprint import pprint

def lista_cidades():
    return select_todas_cidades()

def detalhes_cidade(cidade_id):
    dados = select_cidade(cidade_id)
    if int(dados['dadosf_c']) < 0:
        ano = str(abs(dados['dataf_c'])) * " AC"
        dados['dataf_c'] = ano 
    return dados

if __name__ == "__main__":
    pprint(detalhes_cidade(1))