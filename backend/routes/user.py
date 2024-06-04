from flask import Blueprint

user_route = Blueprint('user', __name__)

@user_route.route('/')
def lista_usuarios():
    pass
@user_route.route('/<int:cliente_id>')
def obter_cliente(cliente_id):
    pass