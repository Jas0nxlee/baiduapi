import json

def load_creatives(file_path):
    """从 JSON 文件加载创意数据。"""
    with open(file_path, 'r') as f:
        return json.load(f)

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
