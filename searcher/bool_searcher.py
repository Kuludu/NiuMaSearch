class BoolSearcher:
    def __init__(self, texts):
        self.name = "布尔查询"
        self.texts = texts

    def update_texts(self, texts):
        self.texts = texts

    def search(self, query):
        s_query = query.split()

        results = list()

        for text in self.texts:
            check = 0
            for word in s_query:
                if word in text['words']:
                    check += 1
                    continue
            if check == len(s_query):
                result = dict()
                result['title'] = text['title']
                result['content'] = text['content']
                result['score'] = 0

                results.append(result)

        return results
