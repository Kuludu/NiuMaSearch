from flask import Flask, make_response, render_template, request, g

from searcher.bool_searcher import BoolSearcher
from searcher.phase_searcher import PhraseSearcher
from utils.text_loader import load_text
from utils.text_scorer import score_text

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
    texts, results = g.searcher.search(query)
    scored_results = score_text(texts, results, query)
    scored_results.sort(key=lambda x: x['score'], reverse=True)

    resp = make_response(render_template('result.html', results=scored_results))

    return resp


def load_searcher():
    if 'searcher' not in g:
        texts = load_text()
        g.searcher = BoolSearcher(texts)


if __name__ == '__main__':
    app.run()
