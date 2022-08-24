from flask import Blueprint

vocatoad = Blueprint('Vocatoad', __name__)
 
@vocatoad.route('/')
@vocatoad.route('/home')
def home():
    return "Welcome to the Vocatoad Home."