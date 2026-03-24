import json
from search_engine import build_index, bm25

with open("corpus.json", encoding="utf-8") as f:
    docs = json.load(f)

index = build_index(docs)

query = "open world game"

results = bm25(query, docs, index)

for doc_id, score in results[:5]:
    doc = next(d for d in docs if d['id'] == doc_id)
    print(doc['title'], score)