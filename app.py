
from flask import Flask

app=Flask(__name__)


@app.route('/')
def home():
    # return render_template('home.html')
    return "<h1>Hello it's working Now DX Factor @</h1>"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int("3000"))