from __future__ import annotations

from pathlib import Path

from tfidf_faq import search_with_answers


def main() -> None:
    base = Path(__file__).resolve().parent
    query = input("Ask an OCR FAQ question: ").strip()
    for question, answer, score in search_with_answers(base / "faq.json", query, top_k=2):
        print(f"- {question} | score={score:.4f}")
        print(f"  {answer}")


if __name__ == "__main__":
    main()
