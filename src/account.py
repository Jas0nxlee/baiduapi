import json

def get_account_info():
    """
    Simulates a call to the Baidu API to get account information.
    In a real application, this would make a network request.
    """
    # This is mock data that mimics the structure of the Baidu API response.
    mock_account_data = {
        "balance": 1000.0,
        "budget": 500.0,
        "region": "CN",
        "domain": "example.com",
        "status": "Active"
    }
    return mock_account_data

def display_account_info(account_data):
    """Prints the account information to the console."""
    print("Account Information:")
    for key, value in account_data.items():
        print(f"  {key.capitalize()}: {value}")
