import unittest
from unittest.mock import patch
import json
import unittest.mock
from src.account import get_account_info, display_account_info
import io

class TestAccount(unittest.TestCase):
    @patch('src.account.requests.get')
    def test_get_account_info_real_api(self, mock_get):
        # Set use_mock_api to False to test the real API call path
        with open('config/app_config.json', 'w') as f:
            json.dump({"use_mock_api": False}, f)

        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = {
            "balance": 2000.0,
            "budget": 1000.0,
            "region": "US",
            "domain": "test.com",
            "status": "Inactive"
        }
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        account_data = get_account_info()
        self.assertEqual(account_data["balance"], 2000.0)
        self.assertEqual(account_data["status"], "Inactive")

    def test_get_account_info_mock_api(self):
        # Set use_mock_api to True to test the mock API call path
        with open('config/app_config.json', 'w') as f:
            json.dump({"use_mock_api": True}, f)

        account_data = get_account_info()
        self.assertEqual(account_data["balance"], 1000.0)
        self.assertEqual(account_data["status"], "Active")

    def test_display_account_info(self):
        account_data = {
            "balance": 1000.0,
            "budget": 500.0,
            "region": "CN",
            "domain": "example.com",
            "status": "Active"
        }
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            display_account_info(account_data)
            output = mock_stdout.getvalue()
            self.assertIn("Balance: 1000.0", output)
            self.assertIn("Status: Active", output)

if __name__ == "__main__":
    unittest.main()
