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

	valid_input, e = validate_input(total, num_sharers, claimed_items)
	if not valid_input:
		return json.dumps(e)
		
	splitter = sp.Splitter(total, num_sharers, claimed_items)
	return splitter.calc_split()	

def validate_input(total, num_sharers, claimed_items):

	error_msg = ""

	if total < 0:
		error_msg += "The total amount you entered is invalid. "

	if num_sharers < 1:
		error_msg += "At least one sharer is required. "

	if error_msg: 
		return False, {"error": error_msg}

	return True, {}
