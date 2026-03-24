from flask import Flask, render_template, request
import json
import time
import re
from search_engine import build_index, bm25

app = Flask(__name__)

# 🔹 Función para resaltar términos
def highlight_text(text, query):
    if not query:
        return text

    words = query.lower().split()

    for word in words:
        # Escapa caracteres especiales para evitar errores en regex
        safe_word = re.escape(word)
        pattern = re.compile(rf"({safe_word})", re.IGNORECASE)
        text = pattern.sub(r"<mark>\1</mark>", text)

    return text


# 🔹 Cargar documentos
with open('corpus.json', encoding='utf-8') as f:
    docs = json.load(f)

# 🔹 Construir índice
index = build_index(docs)


@app.route('/', methods=['GET', 'POST'])
def home():
    results = []
    query = ""
    search_time = 0

    if request.method == 'POST':
        query = request.form.get('query', '').strip()

        if query:  # 🔥 evita buscar vacío
            start = time.time()
            ranked = bm25(query, docs, index)
            end = time.time()

            search_time = round(end - start, 4)

            for doc_id, score in ranked[:10]:
                doc = next(d for d in docs if d['id'] == doc_id)

                highlighted_text = highlight_text(doc['text'][:300], query)

                results.append({
                    'title': doc['title'],
                    'text': highlighted_text,
                    'score': round(score, 2)
                })

    return render_template(
        'index.html',
        results=results,
        query=query,
        total_docs=len(docs),
        vocab_size=len(index),
        search_time=search_time
    )


if __name__ == '__main__':
    app.run(debug=True)