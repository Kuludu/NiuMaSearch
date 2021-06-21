import os
import string

from utils.stop_word_loader import load_stop_words

ROOT_DIR = os.path.abspath("./")
STOP_WORDS = load_stop_words()


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
