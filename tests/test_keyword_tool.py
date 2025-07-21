import unittest
from src.keyword_tool import recommend_keywords, expand_keywords

class TestKeywordTool(unittest.TestCase):
    def test_recommend_keywords(self):
        recommendations = recommend_keywords("手机")
        self.assertIn("手机 价格", recommendations)
        self.assertIn("购买 手机", recommendations)
        self.assertIn("最好的 手机", recommendations)

    def test_expand_keywords(self):
        expanded = expand_keywords("手机")
        self.assertIn("手机", expanded)
        self.assertIn("最新款 手机", expanded)
        self.assertIn("手机 推荐", expanded)
        self.assertIn("最新款 手机 推荐", expanded)

if __name__ == "__main__":
    unittest.main()
