
from datetime import datetime
import json
from flask import render_template, request
from Website import app

@app.route('/')
@app.route('/dailyposts/create', methods=['GET','POST'])
def create():
    payload = request.data
    datastore = json.loads(payload)
    print(datastore)
    print('Entry created successfully', 'success')
    date = datastore["date"]
    content = datastore["content"]
    print(date)

    with open("/Website/posts.json", "a+") as f:
            f.write(date)
            f.write("\n")
            f.write(content)
            f.write("\n")
        
    