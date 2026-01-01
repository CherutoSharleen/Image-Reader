# Local FAQ Search

This mini application performs local FAQ retrieval using TF-IDF and cosine similarity.

## Run

```bash
cd local_faq_search
python -c "from pathlib import Path; from tfidf_faq import search_with_answers; print(search_with_answers(Path('faq.json'), 'blurry photos', top_k=2))"
```

## Test

```bash
cd local_faq_search
python -m unittest test_tfidf_faq.py
```

The FAQ data is fictional and synthetic.
