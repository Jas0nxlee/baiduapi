import unittest
import os
import json
from src.config import (
    load_config,
    save_config,
    encrypt_api_key,
    decrypt_api_key,
)

class TestConfig(unittest.TestCase):
    def setUp(self):
        self.test_config_path = "test_config.json"

    def tearDown(self):
        if os.path.exists(self.test_config_path):
            os.remove(self.test_config_path)

    def test_load_config_file_not_found(self):
        config = load_config("non_existent_file.json")
        self.assertEqual(config, {})

    def test_save_and_load_config(self):
        config_data = {"key": "value", "number": 123}
        save_config(self.test_config_path, config_data)
        loaded_config = load_config(self.test_config_path)
        self.assertEqual(loaded_config, config_data)

    def test_encrypt_and_decrypt_api_key(self):
        api_key = "my_secret_api_key"
        encrypted_key = encrypt_api_key(api_key)
        decrypted_key = decrypt_api_key(encrypted_key)
        self.assertEqual(decrypted_key, api_key)

if __name__ == "__main__":
    unittest.main()
