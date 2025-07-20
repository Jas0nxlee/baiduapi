import unittest
import os
import csv
from src.batch import batch_import_from_csv, batch_export_to_csv

class TestBatch(unittest.TestCase):
    def setUp(self):
        self.test_import_path = "test_import.csv"
        self.test_export_path = "test_export.csv"
        self.test_data = [
            {"col1": "a", "col2": "b"},
            {"col1": "c", "col2": "d"},
        ]
        with open(self.test_import_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.test_data[0].keys())
            writer.writeheader()
            writer.writerows(self.test_data)

    def tearDown(self):
        if os.path.exists(self.test_import_path):
            os.remove(self.test_import_path)
        if os.path.exists(self.test_export_path):
            os.remove(self.test_export_path)

    def test_batch_import_from_csv(self):
        imported_data = batch_import_from_csv(self.test_import_path)
        self.assertEqual(imported_data, self.test_data)

    def test_batch_export_to_csv(self):
        batch_export_to_csv(self.test_data, self.test_export_path)
        with open(self.test_export_path, 'r') as f:
            reader = csv.reader(f)
            rows = list(reader)
            self.assertEqual(len(rows), 3)
            self.assertEqual(rows[0], ["col1", "col2"])
            self.assertEqual(rows[1], ["a", "b"])

if __name__ == "__main__":
    unittest.main()
