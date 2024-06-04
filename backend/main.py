from flask import Flask, jsonify
from flask_cors import CORS
from routes.home import home_route
from routes.charSheet import sheet_route

# inicializar
app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})
CORS(app, resources={r'/*':{'origins': 'http://localhost:8080', "allow_headers": "Access-Crontrol_Allow-Origin"}})

#rotas

#home
app.register_blueprint(home_route) 
#ficha 
app.register_blueprint(sheet_route, url_prefix='/sheets')

#rodar

if __name__ == "__main__":
    app.run(debug=True)