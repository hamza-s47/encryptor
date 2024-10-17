from flask import Flask, render_template
from .controllers.controller import TextEncryptor

app = Flask(__name__)


@app.route('/', methods=['GET'])
def root_route():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
