import requests
from src.config import load_config
import json

API_BASE_URL = "https://api.baidu.com"

def load_creatives():
    """
    Gets creatives from the Baidu API or a mock source.
    """
    app_config = load_config('config/app_config.json')
    if app_config.get("use_mock_api", False):
        with open('data/creatives/creatives.json', 'r') as f:
            return json.load(f)

    api_config = load_config('config/api_config.json')
    headers = {
        "Authorization": f"Bearer {api_config['api_key']}:{api_config['api_secret']}"
    }
    response = requests.get(f"{API_BASE_URL}/api/v1/creatives", headers=headers)
    response.raise_for_status()
    return response.json()

def save_creatives(file_path, creatives):
    """将创意数据保存到 JSON 文件。"""
    with open(file_path, 'w') as f:
        json.dump(creatives, f, indent=4)

def get_creatives_by_adgroup_id(creatives, adgroup_id):
    """根据单元ID获取创意。"""
    return [cr for cr in creatives if cr['adgroup_id'] == adgroup_id]

def display_creatives(creatives):
    """在控制台中显示创意列表。"""
    print("创意:")
    for creative in creatives:
        print(f"  ID: {creative['id']}, 标题: {creative['title']}, 状态: {creative['status']}")

def search_creatives(creatives, keyword):
    """根据关键词搜索创意。"""
    return [cr for cr in creatives if keyword.lower() in cr['title'].lower()]

def filter_creatives_by_status(creatives, status):
    """根据状态筛选创意。"""
    return [cr for cr in creatives if cr['status'].lower() == status.lower()]

def bulk_update_creative_status(creatives, ids, status):
    """批量更新创意状态。"""
    for creative in creatives:
        if creative['id'] in ids:
            creative['status'] = status
    return creatives
