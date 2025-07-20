import json

def load_campaigns(file_path):
    """从 JSON 文件加载计划数据。"""
    with open(file_path, 'r') as f:
        return json.load(f)

def save_campaigns(file_path, campaigns):
    """将计划数据保存到 JSON 文件。"""
    with open(file_path, 'w') as f:
        json.dump(campaigns, f, indent=4)

def display_campaigns(campaigns):
    """在控制台中显示计划列表。"""
    print("推广计划:")
    for campaign in campaigns:
        print(f"  ID: {campaign['id']}, 名称: {campaign['name']}, 状态: {campaign['status']}")

def search_campaigns(campaigns, keyword):
    """根据关键词搜索计划。"""
    return [c for c in campaigns if keyword.lower() in c['name'].lower()]

def filter_campaigns_by_status(campaigns, status):
    """根据状态筛选计划。"""
    return [c for c in campaigns if c['status'].lower() == status.lower()]

def bulk_update_campaign_status(campaigns, ids, status):
    """批量更新计划状态。"""
    for campaign in campaigns:
        if campaign['id'] in ids:
            campaign['status'] = status
    return campaigns
