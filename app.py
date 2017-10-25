from flask import Flask
from flask import request
from flask import render_template
from flask import url_for

import json
import split as sp

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return render_template('splitter.html')

@app.route('/split', methods=['POST'])
def handler():

	# data = request.form['data']
	# return data

	total = request.form['total']
	num_sharers = request.form['num_sharers']
	claimed_items = request.form['items']	
	print(total)
	return 1
	
	# total = data.total
	# num_sharers = data.num_sharers
	# claimed_items = data.items

	# splitter = sp.Splitter(total, num_sharers, claimed_items)
	# return splitter.calc_split()
	# return 1