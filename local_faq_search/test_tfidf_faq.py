import unittest
from pathlib import Path

from tfidf_faq import search_faq, search_with_answers


class FaqSearchTests(unittest.TestCase):
    def test_blur_query_matches_blurry_question(self) -> None:
        path = Path(__file__).resolve().parent / "faq.json"
        top_question = search_faq(path, "blurry OCR photos", top_k=1)[0][0]
        self.assertIn("blurry", top_question.lower())

    def test_answer_is_returned_with_ranked_question(self) -> None:
        path = Path(__file__).resolve().parent / "faq.json"
        question, answer, _ = search_with_answers(path, "store extracted text", top_k=1)[0]
        self.assertIn("store extracted text", question.lower())
        self.assertIn("metadata", answer.lower())


if __name__ == "__main__":
    unittest.main()
