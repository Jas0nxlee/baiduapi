import requests
from src.config import load_config
import json

API_BASE_URL = "https://api.baidu.com"

def load_adgroups():
    """
    Gets adgroups from the Baidu API or a mock source.
    """
    app_config = load_config('config/app_config.json')
    if app_config.get("use_mock_api", False):
        with open('data/adgroups/adgroups.json', 'r') as f:
            return json.load(f)

    api_config = load_config('config/api_config.json')
    headers = {
        "Authorization": f"Bearer {api_config['api_key']}:{api_config['api_secret']}"
    }
    response = requests.get(f"{API_BASE_URL}/api/v1/adgroups", headers=headers)
    response.raise_for_status()
    return response.json()

def save_adgroups(file_path, adgroups):
    """将单元数据保存到 JSON 文件。"""
    with open(file_path, 'w') as f:
        json.dump(adgroups, f, indent=4)

def get_adgroups_by_campaign_id(adgroups, campaign_id):
    """根据计划ID获取单元。"""
    return [ag for ag in adgroups if ag['campaign_id'] == campaign_id]

def display_adgroups(adgroups):
    """在控制台中显示单元列表。"""
    print("推广单元:")
    for adgroup in adgroups:
        print(f"  ID: {adgroup['id']}, 名称: {adgroup['name']}, 状态: {adgroup['status']}")

def search_adgroups(adgroups, keyword):
    """根据关键词搜索单元。"""
    return [ag for ag in adgroups if keyword.lower() in ag['name'].lower()]

def filter_adgroups_by_status(adgroups, status):
    """根据状态筛选单元。"""
    return [ag for ag in adgroups if ag['status'].lower() == status.lower()]

def bulk_update_adgroup_status(adgroups, ids, status):
    """批量更新单元状态。"""
    for adgroup in adgroups:
        if adgroup['id'] in ids:
            adgroup['status'] = status
    return adgroups
