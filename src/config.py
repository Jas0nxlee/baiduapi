import json
import os
from cryptography.fernet import Fernet

# Generate a key for encryption and decryption.
# In a real application, you would want to store this key securely.
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def load_config(file_path):
    """Loads a JSON configuration file."""
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r') as f:
        return json.load(f)

def save_config(file_path, config):
    """Saves a configuration to a JSON file."""
    with open(file_path, 'w') as f:
        json.dump(config, f, indent=4)

def encrypt_api_key(api_key):
    """Encrypts an API key."""
    return cipher_suite.encrypt(api_key.encode()).decode()

def decrypt_api_key(encrypted_api_key):
    """Decrypts an API key."""
    return cipher_suite.decrypt(encrypted_api_key.encode()).decode()
