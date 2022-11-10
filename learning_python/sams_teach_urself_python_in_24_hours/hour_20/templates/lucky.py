from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def lucky():
    lucky_num = 7
    return render_template('lucky.html', lucky_num=lucky_num)

if __name__=='__main__':
    app.run()