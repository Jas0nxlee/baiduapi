import requests
from src.config import load_config

API_BASE_URL = "https://api.baidu.com"

def get_account_info():
    """
    Gets account information from the Baidu API or a mock source.
    """
    app_config = load_config('config/app_config.json')
    if app_config.get("use_mock_api", False):
        return {
            "balance": 1000.0,
            "budget": 500.0,
            "region": "CN",
            "domain": "example.com",
            "status": "Active"
        }

    api_config = load_config('config/api_config.json')
    headers = {
        "Authorization": f"Bearer {api_config['api_key']}:{api_config['api_secret']}"
    }
    response = requests.get(f"{API_BASE_URL}/api/v1/accounts", headers=headers)
    response.raise_for_status()
    return response.json()

def display_account_info(account_data):
    """Prints the account information to the console."""
    print("Account Information:")
    for key, value in account_data.items():
        print(f"  {key.capitalize()}: {value}")
