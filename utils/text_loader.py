import os
import string
import jieba

from zhon.hanzi import punctuation as chinesepunctuation
from utils.stop_word_loader import load_stop_words

ROOT_DIR = os.path.abspath("./")
STOP_WORDS = load_stop_words()


def load_text():
    results = filter(lambda x: '.txt' in x, os.listdir(ROOT_DIR + '/documents'))
    texts = dict()
    texts['content'] = dict()
    total_words = set()
    docID = 1
    for result in results:
        text = dict()
        text['title'] = result
        with open(ROOT_DIR + '/documents//' + result, 'r') as f:
            plain_text = f.read()
            text['content'] = plain_text
            cleaned_text = clean_text(plain_text)
            removed_text = remove_stop_word(cleaned_text)
            s_text = list(jieba.cut(removed_text))
            s_text = list(filter(lambda x: x != ' ', s_text))

        text['words'] = list(set(s_text))
        total_words |= set(s_text)
        p = dict.fromkeys(text['words'])
        cnt = 1
        for cur in s_text:
            if p[cur] is None:
                p[cur] = list()
            p[cur].append(cnt)
            cnt += 1
        text['p_table'] = p
        text['len'] = len(s_text)

        texts['content'][docID] = text
        docID += 1

    texts['ir'] = gen_ir(texts['content'], list(total_words))

    return texts


def clean_text(text):
    text = text.replace('\n', '')
    for i in string.punctuation:
        text = text.replace(i, '')

    for i in chinesepunctuation:
        text = text.replace(i, '')

    return text


def remove_stop_word(text):
    for i in STOP_WORDS:
        text = text.replace(i, '')

    return text


def gen_ir(texts, total_words):
    ir = dict.fromkeys(total_words)

    for word in total_words:
        ir[word] = list()
        index = 1
        for text in texts.values():
            if word in text['words']:
                ir[word].append(index)
            index += 1

    return ir
