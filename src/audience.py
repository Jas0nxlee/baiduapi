import json

def load_audiences(file_path):
    """从 JSON 文件加载人群数据。"""
    with open(file_path, 'r') as f:
        return json.load(f)

def save_audiences(file_path, audiences):
    """将人群数据保存到 JSON 文件。"""
    with open(file_path, 'w') as f:
        json.dump(audiences, f, indent=4)

def create_audience(audiences, name, description):
    """创建新的人群。"""
    new_id = max([a['id'] for a in audiences]) + 1 if audiences else 1
    new_audience = {
        "id": new_id,
        "name": name,
        "description": description,
    }
    audiences.append(new_audience)
    return new_audience

def get_audience_by_id(audiences, audience_id):
    """根据ID获取人群。"""
    for audience in audiences:
        if audience['id'] == audience_id:
            return audience
    return None
