from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

@app.route('/test/')
def test_page():
    return 'This is a test page.'

if __name__ == '__main__':
    app.run()

@app.route('<name>')
def name_page(name):
    return "Hello, {name}".format(name=name)

app.run()