import json

from flask import Flask, make_response, render_template

app = Flask(__name__, static_folder='static')


@app.route('/')
def main():
    resp = make_response(render_template('result.html'))
    # resp = make_response(render_template('search.html'))

    return resp


@app.route('/search', methods=['POST'])
def search():
    resp = make_response(render_template('result.html'))

    return resp


if __name__ == '__main__':
    app.run()
