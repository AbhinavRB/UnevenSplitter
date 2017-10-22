from flask import Flask
from flask import request
import split as sp

app = Flask(__name__)

@app.route('/split', methods=['POST'])
def handler():
	total = request.form['total']
	num_sharers = request.form['num_sharers']
	claimed_items = request.form['items']

	splitter = sp.Splitter(total, num_sharers, claimed_items)
	return splitter.split()