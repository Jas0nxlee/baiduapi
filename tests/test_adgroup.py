import unittest
import os
import json
import unittest.mock
from unittest.mock import patch
from src.adgroup import (
    load_adgroups,
    save_adgroups,
    get_adgroups_by_campaign_id,
    search_adgroups,
    filter_adgroups_by_status,
    bulk_update_adgroup_status,
)

class TestAdgroup(unittest.TestCase):
    def setUp(self):
        self.test_adgroups_path = "test_adgroups.json"
        self.adgroups_data = [
            {"id": 101, "name": "夏季促销-连衣裙", "status": "Active", "campaign_id": 1},
            {"id": 102, "name": "夏季促销-T恤", "status": "Active", "campaign_id": 1},
            {"id": 201, "name": "新品推广-手机", "status": "Paused", "campaign_id": 2},
            {"id": 301, "name": "品牌宣传-通用", "status": "Active", "campaign_id": 3},
        ]
        with open(self.test_adgroups_path, 'w') as f:
            json.dump(self.adgroups_data, f)

    def tearDown(self):
        if os.path.exists(self.test_adgroups_path):
            os.remove(self.test_adgroups_path)

    @patch('src.adgroup.requests.get')
    def test_load_adgroups_real_api(self, mock_get):
        with open('config/app_config.json', 'w') as f:
            json.dump({"use_mock_api": False}, f)

        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = self.adgroups_data
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        adgroups = load_adgroups()
        self.assertEqual(adgroups, self.adgroups_data)

    def test_load_adgroups_mock_api(self):
        with open('config/app_config.json', 'w') as f:
            json.dump({"use_mock_api": True}, f)

        adgroups = load_adgroups()
        self.assertEqual(adgroups[0]['name'], "夏季促销-连衣裙")

    def test_save_adgroups(self):
        new_adgroups = self.adgroups_data + [{"id": 401, "name": "测试单元", "status": "Draft", "campaign_id": 4}]
        save_adgroups(self.test_adgroups_path, new_adgroups)
        with open(self.test_adgroups_path, 'r') as f:
            loaded_adgroups = json.load(f)
        self.assertEqual(loaded_adgroups, new_adgroups)

    def test_get_adgroups_by_campaign_id(self):
        results = get_adgroups_by_campaign_id(self.adgroups_data, 1)
        self.assertEqual(len(results), 2)

    def test_search_adgroups(self):
        results = search_adgroups(self.adgroups_data, "手机")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "新品推广-手机")

    def test_filter_adgroups_by_status(self):
        results = filter_adgroups_by_status(self.adgroups_data, "Paused")
        self.assertEqual(len(results), 1)

    def test_bulk_update_adgroup_status(self):
        updated_adgroups = bulk_update_adgroup_status(self.adgroups_data, [101, 301], "Paused")
        self.assertEqual(updated_adgroups[0]["status"], "Paused")
        self.assertEqual(updated_adgroups[3]["status"], "Paused")

if __name__ == "__main__":
    unittest.main()
