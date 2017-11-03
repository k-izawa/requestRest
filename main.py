from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/good')
def good():
  name = "Good"
  return name

if __name__ == '__main__':
  app.run()
