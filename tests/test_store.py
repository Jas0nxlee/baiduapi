import unittest
import os
import json
from src.store import (
    load_stores,
    save_stores,
    create_store,
    get_store_by_id,
    update_store,
    delete_store,
)

class TestStore(unittest.TestCase):
    def setUp(self):
        self.test_stores_path = "test_stores.json"
        self.stores_data = [
            {"id": 1, "name": "北京总店", "address": "北京市海淀区"},
            {"id": 2, "name": "上海分店", "address": "上海市浦东新区"},
        ]
        with open(self.test_stores_path, 'w') as f:
            json.dump(self.stores_data, f)

    def tearDown(self):
        if os.path.exists(self.test_stores_path):
            os.remove(self.test_stores_path)

    def test_load_stores(self):
        stores = load_stores(self.test_stores_path)
        self.assertEqual(stores, self.stores_data)

    def test_save_stores(self):
        new_stores = self.stores_data + [{"id": 3, "name": "广州分店", "address": "广州市天河区"}]
        save_stores(self.test_stores_path, new_stores)
        with open(self.test_stores_path, 'r') as f:
            loaded_stores = json.load(f)
        self.assertEqual(loaded_stores, new_stores)

    def test_create_store(self):
        new_store = create_store(self.stores_data, "深圳分店", "深圳市南山区")
        self.assertEqual(new_store["id"], 3)
        self.assertEqual(len(self.stores_data), 3)

    def test_get_store_by_id(self):
        store = get_store_by_id(self.stores_data, 1)
        self.assertEqual(store["name"], "北京总店")

    def test_update_store(self):
        updated_store = update_store(self.stores_data, 1, "北京旗舰店", "北京市朝阳区")
        self.assertEqual(updated_store["name"], "北京旗舰店")
        self.assertEqual(self.stores_data[0]["address"], "北京市朝阳区")

    def test_delete_store(self):
        delete_store(self.stores_data, 1)
        self.assertEqual(len(self.stores_data), 1)
        self.assertEqual(self.stores_data[0]["id"], 2)

if __name__ == "__main__":
    unittest.main()
