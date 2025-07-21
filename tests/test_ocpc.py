import unittest
import os
import json
from src.ocpc import (
    load_ocpc_packages,
    save_ocpc_packages,
    create_ocpc_package,
    get_ocpc_package_by_id,
)

class TestOcpc(unittest.TestCase):
    def setUp(self):
        self.test_packages_path = "test_ocpc_packages.json"
        self.packages_data = [
            {"id": 1, "name": "标准投放包", "target_cpa": 50.0},
            {"id": 2, "name": "高转化投放包", "target_cpa": 80.0},
        ]
        with open(self.test_packages_path, 'w') as f:
            json.dump(self.packages_data, f)

    def tearDown(self):
        if os.path.exists(self.test_packages_path):
            os.remove(self.test_packages_path)

    def test_load_ocpc_packages(self):
        packages = load_ocpc_packages(self.test_packages_path)
        self.assertEqual(packages, self.packages_data)

    def test_save_ocpc_packages(self):
        new_packages = self.packages_data + [{"id": 3, "name": "测试包", "target_cpa": 60.0}]
        save_ocpc_packages(self.test_packages_path, new_packages)
        with open(self.test_packages_path, 'r') as f:
            loaded_packages = json.load(f)
        self.assertEqual(loaded_packages, new_packages)

    def test_create_ocpc_package(self):
        new_package = create_ocpc_package(self.packages_data, "新投放包", 70.0)
        self.assertEqual(new_package["id"], 3)
        self.assertEqual(len(self.packages_data), 3)

    def test_get_ocpc_package_by_id(self):
        package = get_ocpc_package_by_id(self.packages_data, 1)
        self.assertEqual(package["name"], "标准投放包")

if __name__ == "__main__":
    unittest.main()
