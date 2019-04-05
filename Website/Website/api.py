
from datetime import datetime
import json
from flask import render_template, request
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
 
    with open("website/templates/posts.json", "ab+") as f:
            f.seek(-1, os.SEEK_END)
            f.truncate()


    with open("website/templates/posts.json", "a+") as f:
            f.write("\n")
            json_string = json.dump(datastore, f)
            json_string = str(json_string)
            json_string = json_string[:-5]
            json_string = json_string[:1]
            print(json_string)
            f.write(json_string)

    with open("website/templates/posts.json", "ab+") as f:
            f.seek(-1, os.SEEK_END)
            f.truncate()
            countLine = len(f.readlines()) - 1
            linestring = str(f.readline(countLine))

    with open("website/templates/posts.json", "a+") as f:
            f.write(", \n")
            f.write("}")
            data = f.read()
            data = data.replace("{","")
            f.write(data)