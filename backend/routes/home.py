from flask import Blueprint, render_template, abort

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    user = {'username': 'Pedro', 'usertitle': 'Mestre', 'userlname': 'Moedas'}
    return(user)