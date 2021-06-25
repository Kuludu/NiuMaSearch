class BoolSearcher:
    def __init__(self, texts):
        self.name = "布尔查询"
        self.texts = texts

    def update_texts(self, texts):
        self.texts = texts

    def search(self, query):
        results = list()

        s_query = query.split()
        phrase = ['!', '&', '|', '(', ')']
        eval_query = str()
        for q in s_query:
            if q not in phrase:
                eval_query += '"' + q + '" in word'
            elif q == '&':
                eval_query += ' and '
            elif q == '|':
                eval_query += ' or '
            elif q == '!':
                eval_query += ' not '
            else:
                eval_query += q

        print(eval_query)

        for key, text in self.texts['content'].items():
            word = text['words']
            if eval(eval_query):
                result = dict()
                result['docID'] = key
                result['title'] = text['title']
                result['content'] = text['content']
                result['score'] = 0

                results.append(result)

        return self.texts, results
