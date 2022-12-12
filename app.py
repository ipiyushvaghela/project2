
from flask import Flask

application=Flask(__name__)


@application.route('/')
def home():
    # return render_template('home.html')
    return "<h1>Hello it's working Fine</h1>"

if __name__ == '__main__':
    application.run(debug=True,host='0.0.0.0',port=int("3000"))