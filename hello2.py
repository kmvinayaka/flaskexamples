from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
   return "Hello, Welcome to Flask"

@app.route('/')
def hello():
   return "Welcome to Flask"

if __name__ == '__main__':
   
   app.run(debug = True)
