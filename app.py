import os
import sys
import string

from flask import Flask, make_response, render_template, request, url_for

app = Flask(__name__, static_folder='static')

ROOT_DIR = os.path.abspath("./")
sys.path.append(ROOT_DIR)

STOP_WORDS = ['cat', 'rat']


@app.route('/')
def main():
    resp = make_response(render_template('search.html', mode="布尔查询"))

    return resp


@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('content')
    texts = load_text()

    results = bool_query(query, texts)

    resp = make_response(render_template('result.html', results=results))

    return resp


def load_text():
    results = filter(lambda x: '.txt' in x, os.listdir(ROOT_DIR + '/documents'))
    texts = list()
    for result in results:
        text = dict()
        text['title'] = result
        with open(ROOT_DIR + '/documents//' + result, 'r') as f:
            plain_text = f.read()
            text['content'] = plain_text
            cleaned_text = clean_text(plain_text)
            removed_text = remove_stop_word(cleaned_text)
            s_text = removed_text.split()

        text['words'] = list(set(s_text))
        p = dict.fromkeys(text['words'])
        cnt = 1
        for cur in s_text:
            if p[cur] is None:
                p[cur] = list()
            p[cur].append(cnt)
            cnt += 1
        text['p_table'] = p

        texts.append(text)

    return texts


def clean_text(text):
    text = text.replace('\n', '')
    for i in string.punctuation:
        text = text.replace(i, '')

    return text


def remove_stop_word(text):
    for i in STOP_WORDS:
        text = text.replace(i, '')

    return text


def bool_query(query, texts):
    s_query = query.split()

    results = list()

    for text in texts:
        check = 0
        for word in s_query:
            if word in text['words']:
                check += 1
                continue
        if check == len(s_query):
            result = dict()
            result['title'] = text['title']
            result['content'] = text['content']

            results.append(result)

    return results


def merge_p_table(p1, p2):
    return set(p1) & set(p2)


if __name__ == '__main__':
    app.run()
