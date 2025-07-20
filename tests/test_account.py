import unittest
from unittest.mock import patch
from src.account import get_account_info, display_account_info
import io

class TestAccount(unittest.TestCase):
    def test_get_account_info(self):
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
