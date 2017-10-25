from flask import Flask
from flask import request
from flask import render_template

import json
import split as sp

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return render_template('splitter.html')

@app.route('/split', methods=['POST'])
def handler():
	
	data = request.get_json()
	
	total = data['total']
	num_sharers = data['num_sharers']
	claimed_items = data['items']
		
	splitter = sp.Splitter(total, num_sharers, claimed_items)
	return splitter.calc_split()	
