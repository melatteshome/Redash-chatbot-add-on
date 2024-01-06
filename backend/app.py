from flask import Flask
from flask import request
import langchain_intergation.langchain_connection as langchain_

app = Flask(__name__)
 



@app.route('/', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        return 0
    else:
        return langchain.getResponse()