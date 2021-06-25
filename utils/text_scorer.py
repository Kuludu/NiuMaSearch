import string
from collections import Counter
from math import log


def score_text(texts, results, query):
    for punctuation in string.punctuation:
        if punctuation in query:
            return results

    query_c = dict(Counter(query.split()))
    d_c = len(texts['content'])

    for result in results:
        score = 0

        for key, value in query_c.items():
            df = len(texts['ir'][key])
            tf = value
            idf = log(d_c / df)
            tf_idf = tf * idf

            score += tf_idf * len(texts['content'][result['docID']]['p_table'][key])

        result['score'] = round(score, 3)

    return results
