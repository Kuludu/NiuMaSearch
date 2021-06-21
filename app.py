import json

from flask import Flask, make_response, render_template, request

app = Flask(__name__, static_folder='static')


@app.route('/')
def main():
    resp = make_response(render_template('search.html'))

    return resp


@app.route('/search', methods=['POST'])
def search():
    content = request.form.get('content')

    example_results = [
                        {
                            "title": "Example",
                            "content": content
                        },
                        {
                            "title": "Example",
                            "content": content
                        }
                       ]

    resp = make_response(render_template('result.html', results=example_results))

    return resp


if __name__ == '__main__':
    app.run()
