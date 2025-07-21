import unittest
import os
import csv
from src.analysis import generate_summary_report, generate_csv_report

class TestAnalysis(unittest.TestCase):
    def setUp(self):
        self.campaigns = [
            {"id": 1, "name": "夏季促销", "status": "Active"},
            {"id": 2, "name": "新品推广", "status": "Paused"},
        ]
        self.adgroups = [
            {"id": 101, "name": "连衣裙", "status": "Active", "campaign_id": 1},
            {"id": 201, "name": "手机", "status": "Paused", "campaign_id": 2},
        ]
        self.keywords = [
            {"id": 1001, "name": "连衣裙", "status": "Active", "adgroup_id": 101},
            {"id": 2001, "name": "智能手机", "status": "Paused", "adgroup_id": 201},
        ]
        self.creatives = [
            {"id": 10001, "title": "夏季连衣裙", "status": "Active", "adgroup_id": 101},
            {"id": 20001, "title": "智能手机", "status": "Paused", "adgroup_id": 201},
        ]
        self.test_csv_path = "test_report.csv"

    def tearDown(self):
        if os.path.exists(self.test_csv_path):
            os.remove(self.test_csv_path)

    def test_generate_summary_report(self):
        summary = generate_summary_report(self.campaigns, self.adgroups, self.keywords, self.creatives)
        self.assertEqual(summary["total_campaigns"], 2)
        self.assertEqual(summary["active_campaigns"], 1)
        self.assertEqual(summary["total_adgroups"], 2)
        self.assertEqual(summary["active_adgroups"], 1)
        self.assertEqual(summary["total_keywords"], 2)
        self.assertEqual(summary["active_keywords"], 1)
        self.assertEqual(summary["total_creatives"], 2)
        self.assertEqual(summary["active_creatives"], 1)

    def test_generate_csv_report(self):
        data = [{"col1": "a", "col2": "b"}, {"col1": "c", "col2": "d"}]
        generate_csv_report(data, self.test_csv_path)
        with open(self.test_csv_path, 'r') as f:
            reader = csv.reader(f)
            rows = list(reader)
            self.assertEqual(len(rows), 3)
            self.assertEqual(rows[0], ["col1", "col2"])
            self.assertEqual(rows[1], ["a", "b"])

if __name__ == "__main__":
    unittest.main()
