import unittest
import os
import json
import unittest.mock
from unittest.mock import patch
from src.campaign import (
    load_campaigns,
    save_campaigns,
    search_campaigns,
    filter_campaigns_by_status,
    bulk_update_campaign_status,
)

class TestCampaign(unittest.TestCase):
    def setUp(self):
        self.test_campaigns_path = "test_campaigns.json"
        self.campaigns_data = [
            {"id": 1, "name": "夏季促销", "status": "Active"},
            {"id": 2, "name": "新品推广", "status": "Paused"},
            {"id": 3, "name": "品牌宣传", "status": "Active"},
        ]
        with open(self.test_campaigns_path, 'w') as f:
            json.dump(self.campaigns_data, f)

    def tearDown(self):
        if os.path.exists(self.test_campaigns_path):
            os.remove(self.test_campaigns_path)

    @patch('src.campaign.requests.get')
    def test_load_campaigns_real_api(self, mock_get):
        with open('config/app_config.json', 'w') as f:
            json.dump({"use_mock_api": False}, f)

        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = self.campaigns_data
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        campaigns = load_campaigns()
        self.assertEqual(campaigns, self.campaigns_data)

    def test_load_campaigns_mock_api(self):
        with open('config/app_config.json', 'w') as f:
            json.dump({"use_mock_api": True}, f)

        campaigns = load_campaigns()
        self.assertEqual(campaigns[0]['name'], "夏季促销计划")

    def test_save_campaigns(self):
        new_campaigns = self.campaigns_data + [{"id": 4, "name": "测试计划", "status": "Draft"}]
        save_campaigns(self.test_campaigns_path, new_campaigns)
        with open(self.test_campaigns_path, 'r') as f:
            loaded_campaigns = json.load(f)
        self.assertEqual(loaded_campaigns, new_campaigns)

    def test_search_campaigns(self):
        results = search_campaigns(self.campaigns_data, "促销")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "夏季促销")

    def test_filter_campaigns_by_status(self):
        results = filter_campaigns_by_status(self.campaigns_data, "Active")
        self.assertEqual(len(results), 2)

    def test_bulk_update_campaign_status(self):
        updated_campaigns = bulk_update_campaign_status(self.campaigns_data, [1, 3], "Paused")
        self.assertEqual(updated_campaigns[0]["status"], "Paused")
        self.assertEqual(updated_campaigns[2]["status"], "Paused")

if __name__ == "__main__":
    unittest.main()
