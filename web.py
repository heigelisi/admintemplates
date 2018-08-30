import flask
import json
from flask import request
from flask import session
import sqlite3
import random
import base64
import re
import time
import os
import sys
import math
app = flask.Flask(__name__)
path = os.path.dirname(sys.argv[0])

@app.route('/index.html')
def index():

	return flask.render_template('system/menu/index.html')


@app.route('/addMenu.html')
def addMenu():

	return flask.render_template('system/menu/addMenu.html')

@app.route('/adminList.html')
def adminList():

	return flask.render_template('system/admin/adminList.html')

@app.route('/addAdmin.html')
def addAdmin():

	return flask.render_template('system/admin/addAdmin.html')

@app.route('/roleList.html')
def roleList():

	return flask.render_template('system/role/roleList.html')
@app.route('/addRole.html')
def addRole():

	return flask.render_template('system/role/addRole.html')


@app.route('/campusList.html')
def campusList():

	return flask.render_template('archives/campus/campusList.html')


@app.route('/addCampus.html')
def addCampus():

	return flask.render_template('archives/campus/addCampus.html')

@app.route('/classTypeList.html')
def classTypeList():
	return flask.render_template('archives/classtype/classTypeList.html')


@app.route('/addClassType.html')
def addClassType():
	return flask.render_template('archives/classtype/addClassType.html')


if __name__ == '__main__':
	app.run(host="0.0.0.0",debug=True,port=8008)