import unittest
import os
import json
import unittest.mock
from unittest.mock import patch
from src.keyword import (
    load_keywords,
    save_keywords,
    get_keywords_by_adgroup_id,
    search_keywords,
    filter_keywords_by_status,
    bulk_update_keyword_status,
)

class TestKeyword(unittest.TestCase):
    def setUp(self):
        self.test_keywords_path = "test_keywords.json"
        self.keywords_data = [
            {"id": 1001, "name": "连衣裙", "status": "Active", "adgroup_id": 101},
            {"id": 1002, "name": "T恤", "status": "Active", "adgroup_id": 102},
            {"id": 2001, "name": "智能手机", "status": "Paused", "adgroup_id": 201},
            {"id": 3001, "name": "品牌", "status": "Active", "adgroup_id": 301},
        ]
        with open(self.test_keywords_path, 'w') as f:
            json.dump(self.keywords_data, f)

    def tearDown(self):
        if os.path.exists(self.test_keywords_path):
            os.remove(self.test_keywords_path)

    @patch('src.keyword.requests.get')
    def test_load_keywords_real_api(self, mock_get):
        with open('config/app_config.json', 'w') as f:
            json.dump({"use_mock_api": False}, f)

        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = self.keywords_data
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        keywords = load_keywords()
        self.assertEqual(keywords, self.keywords_data)

    def test_load_keywords_mock_api(self):
        with open('config/app_config.json', 'w') as f:
            json.dump({"use_mock_api": True}, f)

        keywords = load_keywords()
        self.assertEqual(keywords[0]['name'], "连衣裙")

    def test_save_keywords(self):
        new_keywords = self.keywords_data + [{"id": 4001, "name": "测试关键词", "status": "Draft", "adgroup_id": 401}]
        save_keywords(self.test_keywords_path, new_keywords)
        with open(self.test_keywords_path, 'r') as f:
            loaded_keywords = json.load(f)
        self.assertEqual(loaded_keywords, new_keywords)

    def test_get_keywords_by_adgroup_id(self):
        results = get_keywords_by_adgroup_id(self.keywords_data, 101)
        self.assertEqual(len(results), 1)

    def test_search_keywords(self):
        results = search_keywords(self.keywords_data, "手机")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "智能手机")

    def test_filter_keywords_by_status(self):
        results = filter_keywords_by_status(self.keywords_data, "Paused")
        self.assertEqual(len(results), 1)

    def test_bulk_update_keyword_status(self):
        updated_keywords = bulk_update_keyword_status(self.keywords_data, [1001, 3001], "Paused")
        self.assertEqual(updated_keywords[0]["status"], "Paused")
        self.assertEqual(updated_keywords[3]["status"], "Paused")

if __name__ == "__main__":
    unittest.main()
