
from datetime import datetime
from flask import render_template, request
from Website import app

@app.route('/')
@app.route('/dailyposts/create', methods=['POST'])
def create():
    request = request.json
    print(request)
    date = request.form['date']
    content=request.form['content']
    print('Entry created successfully', 'success')     