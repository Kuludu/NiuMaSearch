def position_intersect(p1, p2, k=3):
    answer = list()
    k1, k2 = [key for key in p1], [key for key in p2]
    i, j = 0, 0
    while i < len(p1) and j < len(p2):
        if k1[i] == k2[j]:
            li = list()
            pp1, pp2 = p1[k1[i]], p2[k2[j]]
            i1, j1 = 0, 0
            while i1 < len(pp1):
                while j1 < len(pp2):
                    if abs(pp1[i1] - pp2[j1]) <= k:
                        li.append(pp2[j1])
                    elif pp2[j1] > pp1[i1]:
                        break
                    j1 += 1
                while li and abs(li[0] - pp1[i1]) > k:
                    del (li[0])
                for n in range(len(li)):
                    answer.append([k1[i], li[n]])
                i1 += 1
            i += 1
            j += 1
        elif k1[i] > k2[j]:
            j += 1
        else:
            i += 1

    return answer


class PhraseSearcher:
    def __init__(self, texts):
        self.name = "短语查询（k=3）"
        self.texts = texts

    def update_texts(self, texts):
        self.texts = texts

    def search(self, query):
        s_query = query.split()

        results = list()

        for word in s_query:
            if word not in self.texts['ir'].keys():
                return self.texts, results

        current_irs = dict.fromkeys(self.texts['ir'][s_query[0]])
        for key in current_irs.keys():
            current_irs[key] = self.texts['content'][key]['p_table'][s_query[0]]

        for word in s_query:
            next_ir = dict.fromkeys(self.texts['ir'][word])
            for key in next_ir.keys():
                next_ir[key] = self.texts['content'][key]['p_table'][word]

            res = position_intersect(current_irs, next_ir)
            current_irs = dict.fromkeys([x[0] for x in res])
            for key in current_irs.keys():
                current_irs[key] = [x[1] for x in res]

        docIDs = [x[0] for x in res]
        docIDs = list(set(docIDs))

        for docID in docIDs:
            result = dict()
            result['docID'] = docID
            result['title'] = self.texts['content'][docID]['title']
            result['content'] = self.texts['content'][docID]['content']
            result['score'] = 0

            results.append(result)

        return self.texts, results
