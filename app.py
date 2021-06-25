from flask import Flask, make_response, render_template, request, g

from searcher.bool_searcher import BoolSearcher
from searcher.phase_searcher import PhraseSearcher
from utils.text_loader import load_text
from utils.text_scorer import score_text

app = Flask(__name__, static_folder='static')


@app.route('/')
def main():
    resp = make_response(render_template('search.html'))

    return resp


@app.route('/boolsearch', methods=['POST'])
def bool_search():
    searcher = BoolSearcher(load_text())

    return render_search(searcher)


@app.route('/phrasesearch', methods=['POST'])
def phrase_search():
    searcher = PhraseSearcher(load_text())

    return render_search(searcher)


def render_search(searcher):
    query = request.form.get('content')
    texts, results = searcher.search(query)
    scored_results = score_text(texts, results, query)
    scored_results.sort(key=lambda x: x['score'], reverse=True)

    return make_response(render_template('result.html', results=scored_results))


if __name__ == '__main__':
    app.run()
