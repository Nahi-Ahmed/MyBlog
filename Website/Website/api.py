
from datetime import datetime
import json
from flask import render_template, request, jsonify
from Website import app
import os
import sys
import re
import linecache




@app.route('/')
@app.route('/dailyposts/create', methods=['GET','POST'])
def create():
    payload = request.data
    datastore = json.loads(payload)
    print(datastore)

    with open("website/templates/posts.txt", "a+") as f:
            f.write("\n")
            json_string = json.dump(datastore, f)
            json_string = str(json_string)
            json_string = json_string[:-5]
            json_string = json_string[:1]
            print(json_string)
            f.write(json_string)

@app.route('/')
@app.route('/dailyposts/get', methods=['GET'])
def get():
    with open("website/templates/posts.txt", "r") as f:
        payloadString = '{'
        index = 1
        for line in f:
            payloadString +=  '"'+str(index)+'": ' + str(line) + ","
            index = index + 1
        payloadString + "}"
    payloadString = payloadString[:-1]

    payloadString = payloadString + "}"
    
    print(payloadString)

    return jsonify(payloadString)

##payloadString + "}"