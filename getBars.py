'''
Created on Apr 12, 2014

@author: Rishi Josan
'''

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
