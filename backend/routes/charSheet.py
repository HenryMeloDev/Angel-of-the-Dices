from flask import Blueprint, request, jsonify
from database.database import SHEETS


sheet_route = Blueprint('sheet', __name__)

# listar todas as fichas
@sheet_route.route('/', methods=['GET', 'POST'])
def get_sheets():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        SHEETS.append({
            'id': len(SHEETS) + 1,
            'nome': post_data.get('nome'),
            'origem': post_data.get('origem'),
            'classe': post_data.get('classe'),
            'trilha': post_data.get('trilha'),
            'nivel': post_data.get('nivel'),
        })
        response_object['message'] = 'Ficha criada!'
    else:
        response_object['sheets'] = SHEETS   
    return jsonify(response_object)

# formulario de criação de ficha
@sheet_route.route('/new', methods=['GET'])
def sheet_form():
    pass

# visualizar uma ficha especifica
@sheet_route.route('/<int:sheet_id>', methods=['GET'])
def get_sheet():
    pass

# formulario de editar uma ficha
@sheet_route.route('/<int:sheet_id>/edit', methods=['GET'])
def edit_sheet_form():
    pass

# atualiazar uma ficha
@sheet_route.route('<int:sheet_id>/update', methods=['PUT'])
def update_sheet():
    pass

# deletar uma ficha
@sheet_route.route('<int:sheet_id>/delete', methods=['DELETE'])
def delete_sheet():
    pass