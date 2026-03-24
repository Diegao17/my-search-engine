import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    tokens = re.findall(r'\b\w+\b', text)

    tokens = [t for t in tokens if t not in stop_words]
    tokens = [stemmer.stem(t) for t in tokens]

    return tokens

from collections import defaultdict

def build_index(docs):
    index = defaultdict(dict)

    for doc in docs:
        tokens = preprocess(doc['text'])
        freq = defaultdict(int)

        for token in tokens:
            freq[token] += 1

        for token, count in freq.items():
            index[token][doc['id']] = count

    return index

import math

def bm25(query, docs, index, k1=1.5, b=0.75):
    scores = {}
    N = len(docs)

    avgdl = sum(len(preprocess(doc['text'])) for doc in docs) / N
    query_tokens = preprocess(query)

    for token in query_tokens:
        if token not in index:
            continue

        df = len(index[token])
        idf = math.log((N - df + 0.5) / (df + 0.5) + 1)

        for doc_id, freq in index[token].items():
            doc = next(d for d in docs if d['id'] == doc_id)
            dl = len(preprocess(doc['text']))

            score = idf * ((freq * (k1 + 1)) /
                           (freq + k1 * (1 - b + b * (dl / avgdl))))

            scores[doc_id] = scores.get(doc_id, 0) + score

    return sorted(scores.items(), key=lambda x: x[1], reverse=True)