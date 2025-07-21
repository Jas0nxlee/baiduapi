import requests
from src.config import load_config
import json

API_BASE_URL = "https://api.baidu.com"

def load_keywords():
    """
    Gets keywords from the Baidu API or a mock source.
    """
    app_config = load_config('config/app_config.json')
    if app_config.get("use_mock_api", False):
        with open('data/keywords/keywords.json', 'r') as f:
            return json.load(f)

    api_config = load_config('config/api_config.json')
    headers = {
        "Authorization": f"Bearer {api_config['api_key']}:{api_config['api_secret']}"
    }
    response = requests.get(f"{API_BASE_URL}/api/v1/keywords", headers=headers)
    response.raise_for_status()
    return response.json()

def save_keywords(file_path, keywords):
    """将关键词数据保存到 JSON 文件。"""
    with open(file_path, 'w') as f:
        json.dump(keywords, f, indent=4)

def get_keywords_by_adgroup_id(keywords, adgroup_id):
    """根据单元ID获取关键词。"""
    return [kw for kw in keywords if kw['adgroup_id'] == adgroup_id]

def display_keywords(keywords):
    """在控制台中显示关键词列表。"""
    print("关键词:")
    for keyword in keywords:
        print(f"  ID: {keyword['id']}, 名称: {keyword['name']}, 状态: {keyword['status']}")

def search_keywords(keywords, keyword_str):
    """根据关键词搜索关键词。"""
    return [kw for kw in keywords if keyword_str.lower() in kw['name'].lower()]

def filter_keywords_by_status(keywords, status):
    """根据状态筛选关键词。"""
    return [kw for kw in keywords if kw['status'].lower() == status.lower()]

def bulk_update_keyword_status(keywords, ids, status):
    """批量更新关键词状态。"""
    for keyword in keywords:
        if keyword['id'] in ids:
            keyword['status'] = status
    return keywords
