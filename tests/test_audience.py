import unittest
import os
import json
from src.audience import (
    load_audiences,
    save_audiences,
    create_audience,
    get_audience_by_id,
)

class TestAudience(unittest.TestCase):
    def setUp(self):
        self.test_audiences_path = "test_audiences.json"
        self.audiences_data = [
            {"id": 1, "name": "高意向用户", "description": "访问过价格页"},
            {"id": 2, "name": "老客", "description": "30天内购买过"},
        ]
        with open(self.test_audiences_path, 'w') as f:
            json.dump(self.audiences_data, f)

    def tearDown(self):
        if os.path.exists(self.test_audiences_path):
            os.remove(self.test_audiences_path)

    def test_load_audiences(self):
        audiences = load_audiences(self.test_audiences_path)
        self.assertEqual(audiences, self.audiences_data)

    def test_save_audiences(self):
        new_audiences = self.audiences_data + [{"id": 3, "name": "新客", "description": "首次访问"}]
        save_audiences(self.test_audiences_path, new_audiences)
        with open(self.test_audiences_path, 'r') as f:
            loaded_audiences = json.load(f)
        self.assertEqual(loaded_audiences, new_audiences)

    def test_create_audience(self):
        new_audience = create_audience(self.audiences_data, "测试人群", "这是一个测试")
        self.assertEqual(new_audience["id"], 3)
        self.assertEqual(len(self.audiences_data), 3)

    def test_get_audience_by_id(self):
        audience = get_audience_by_id(self.audiences_data, 1)
        self.assertEqual(audience["name"], "高意向用户")

if __name__ == "__main__":
    unittest.main()
