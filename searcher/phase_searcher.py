class PhraseSearcher:
    def __init__(self, texts):
        self.name = "短语查询"
        self.texts = texts

    def update_texts(self, texts):
        self.texts = texts

    def search(self, query):
        pass
