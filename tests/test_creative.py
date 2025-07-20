import unittest
import os
import json
from src.creative import (
    load_creatives,
    save_creatives,
    get_creatives_by_adgroup_id,
    search_creatives,
    filter_creatives_by_status,
    bulk_update_creative_status,
)

class TestCreative(unittest.TestCase):
    def setUp(self):
        self.test_creatives_path = "test_creatives.json"
        self.creatives_data = [
            {"id": 10001, "title": "夏季连衣裙", "status": "Active", "adgroup_id": 101},
            {"id": 10002, "title": "纯棉T恤", "status": "Active", "adgroup_id": 102},
            {"id": 20001, "title": "智能手机", "status": "Paused", "adgroup_id": 201},
            {"id": 30001, "title": "品牌宣传", "status": "Active", "adgroup_id": 301},
        ]
        with open(self.test_creatives_path, 'w') as f:
            json.dump(self.creatives_data, f)

    def tearDown(self):
        if os.path.exists(self.test_creatives_path):
            os.remove(self.test_creatives_path)

    def test_load_creatives(self):
        creatives = load_creatives(self.test_creatives_path)
        self.assertEqual(creatives, self.creatives_data)

    def test_save_creatives(self):
        new_creatives = self.creatives_data + [{"id": 40001, "title": "测试创意", "status": "Draft", "adgroup_id": 401}]
        save_creatives(self.test_creatives_path, new_creatives)
        with open(self.test_creatives_path, 'r') as f:
            loaded_creatives = json.load(f)
        self.assertEqual(loaded_creatives, new_creatives)

    def test_get_creatives_by_adgroup_id(self):
        results = get_creatives_by_adgroup_id(self.creatives_data, 101)
        self.assertEqual(len(results), 1)

    def test_search_creatives(self):
        results = search_creatives(self.creatives_data, "手机")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "智能手机")

    def test_filter_creatives_by_status(self):
        results = filter_creatives_by_status(self.creatives_data, "Paused")
        self.assertEqual(len(results), 1)

    def test_bulk_update_creative_status(self):
        updated_creatives = bulk_update_creative_status(self.creatives_data, [10001, 30001], "Paused")
        self.assertEqual(updated_creatives[0]["status"], "Paused")
        self.assertEqual(updated_creatives[3]["status"], "Paused")

if __name__ == "__main__":
    unittest.main()
