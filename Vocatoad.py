#!flask/bin/python
import pathlib, sys
from flask import Flask, jsonify, abort, make_response
#from flask_bcrypt import Bcrypt

currentPath = pathlib.Path(__file__).parent.absolute()
rootpath = currentPath
vocalizationfilePath = rootpath.joinpath("vocalizations").absolute()
outputfilePath = rootpath.joinpath("vocalizations").absolute()

app = Flask(__name__)

#bcrypt = Bcrypt(app)

from VocatoadViews import *

app.register_blueprint(vocatoad)