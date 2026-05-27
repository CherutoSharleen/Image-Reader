import unittest
from pathlib import Path

from tfidf_faq import highlight_terms, overlap_terms, search_faq, search_with_answers


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

    def test_highlight_terms_marks_query_words(self) -> None:
        highlighted = highlight_terms("OCR fails on blurry photos", "blurry OCR")
        self.assertIn("[OCR]", highlighted)
        self.assertIn("[blurry]", highlighted.lower())

    def test_overlap_terms(self) -> None:
        overlaps = overlap_terms("OCR fails on blurry photos", "blurry OCR setup")
        self.assertEqual(overlaps, ["blurry", "ocr"])


if __name__ == "__main__":
    unittest.main()
