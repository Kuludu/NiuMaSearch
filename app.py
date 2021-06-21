from flask import Flask, make_response, render_template, request, g

from searcher.bool_searcher import BoolSearcher
from utils.text_loader import load_text

app = Flask(__name__, static_folder='static')


@app.route('/')
def main():
    load_searcher()

    resp = make_response(render_template('search.html', mode=g.searcher.name))

    return resp


@app.route('/search', methods=['POST'])
def search():
    load_searcher()

    query = request.form.get('content')

    results = g.searcher.search(query)

    resp = make_response(render_template('result.html', results=results))

    return resp


def load_searcher():
    if 'searcher' not in g:
        texts = load_text()
        g.searcher = BoolSearcher(texts)


if __name__ == '__main__':
    app.run()
