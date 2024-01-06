from flask import Flask
from flask import request
app = Flask(__name__)




@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 
    else:
        return 