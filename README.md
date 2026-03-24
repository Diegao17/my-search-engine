# 🎮 VideoGaMex


---

## Project Description

This project consists of a search engine built from scratch in Python. It allows users to search within a collection of real documents related to video games. The system uses text processing, an inverted index, and the BM25 ranking algorithm to return the most relevant results.

---

## Domain

The chosen domain is **Video Games**.

This domain was selected because:

* It provides a large amount of real-world data (Wikipedia, gaming articles)
* It allows meaningful queries such as genres, gameplay mechanics, and game titles
* It makes the search results intuitive and easy to evaluate

---

## Corpus

The corpus was created using a Python scraping script (`scraper.py`) that extracts real content from Wikipedia pages.

Each document includes:

* Title
* Text (minimum 50 words)
* Source URL

The corpus is stored in:

```
corpus.json
```

---

## Search Engine Components

### Text Processing

* Lowercasing
* Tokenization
* Stopword removal
* Stemming

Implemented in:

```
search_engine.py → preprocess()
```

---

### Inverted Index

Maps each term to the documents where it appears along with term frequency.

Implemented in:

```
search_engine.py → build_index()
```

---

### BM25 Ranking

Used to rank documents based on relevance.

Implemented in:

```
search_engine.py → bm25()
```

---

## Web Interface

The application uses **Flask** to provide a web interface where users can:

* Enter a search query
* View ranked results
* See relevance scores
* View system statistics:

  * Total documents
  * Vocabulary size
  * Search time

Main file:

```
app.py
```

---

## Enhancement Implemented

### A: Term Highlighting

Search terms are highlighted in the results using HTML `<mark>` tags.

Example:

```
Query: open world
Result: This is an <mark>open</mark> <mark>world</mark> game...
```

Implemented in:

```
app.py → highlight_text()
```

---

## How to Run the Project

1. Clone the repository:

```
git clone <YOUR_REPO_URL>
cd my-search-engine
```

2. Create virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Download NLTK stopwords:

```
python
import nltk
nltk.download('stopwords')
exit()
```

5. Run the application:

```
python3 app.py
```

6. Open in browser:

```
http://127.0.0.1:5000
```

---

## Notes

* The corpus is built from real data obtained via web scraping
* The search engine operates locally on the indexed data
* BM25 is used for ranking instead of simple keyword matching

---
