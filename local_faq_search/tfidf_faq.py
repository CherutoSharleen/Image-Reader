from __future__ import annotations

import json
import math
import re
from collections import Counter
from pathlib import Path


TOKEN_PATTERN = re.compile(r"[a-z0-9']+")


def tokenize(text: str) -> list[str]:
    return TOKEN_PATTERN.findall(text.lower())


def _cosine(a: dict[str, float], b: dict[str, float]) -> float:
    overlap = set(a) & set(b)
    dot = sum(a[t] * b[t] for t in overlap)
    norm_a = math.sqrt(sum(v * v for v in a.values()))
    norm_b = math.sqrt(sum(v * v for v in b.values()))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / norm_a / norm_b


def search_faq(path: Path, query: str, top_k: int = 2) -> list[tuple[str, float]]:
    faq = json.loads(path.read_text(encoding="utf-8"))
    docs = [f"{row['question']} {row['answer']}" for row in faq]
    tokens_per_doc = [tokenize(d) for d in docs]
    df: dict[str, int] = {}
    for tokens in tokens_per_doc:
        for token in set(tokens):
            df[token] = df.get(token, 0) + 1
    n = len(docs)
    idf = {t: math.log((1 + n) / (1 + c)) + 1 for t, c in df.items()}

    def to_vector(tokens: list[str]) -> dict[str, float]:
        counts = Counter(tokens)
        length = len(tokens) or 1
        return {t: (c / length) * idf.get(t, 0.0) for t, c in counts.items()}

    query_vec = to_vector(tokenize(query))
    scored: list[tuple[str, float]] = []
    for row, tokens in zip(faq, tokens_per_doc):
        score = _cosine(query_vec, to_vector(tokens))
        scored.append((row["question"], score))
    scored.sort(key=lambda item: item[1], reverse=True)
    return scored[:top_k]


def search_with_answers(path: Path, query: str, top_k: int = 2) -> list[tuple[str, str, float]]:
    faq = json.loads(path.read_text(encoding="utf-8"))
    ranked = search_faq(path, query, top_k=top_k)
    lookup = {row["question"]: row["answer"] for row in faq}
    return [(question, lookup[question], score) for question, score in ranked]


def highlight_terms(text: str, query: str) -> str:
    tokens = set(tokenize(query))
    words = text.split()
    highlighted = []
    for word in words:
        clean = re.sub(r"[^a-z0-9']", "", word.lower())
        if clean in tokens and clean:
            highlighted.append(f"[{word}]")
        else:
            highlighted.append(word)
    return " ".join(highlighted)
