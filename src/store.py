import json

def load_stores(file_path):
    """从 JSON 文件加载门店数据。"""
    with open(file_path, 'r') as f:
        return json.load(f)

def save_stores(file_path, stores):
    """将门店数据保存到 JSON 文件。"""
    with open(file_path, 'w') as f:
        json.dump(stores, f, indent=4)

def create_store(stores, name, address):
    """创建新的门店。"""
    new_id = max([s['id'] for s in stores]) + 1 if stores else 1
    new_store = {
        "id": new_id,
        "name": name,
        "address": address,
    }
    stores.append(new_store)
    return new_store

def get_store_by_id(stores, store_id):
    """根据ID获取门店。"""
    for store in stores:
        if store['id'] == store_id:
            return store
    return None

def update_store(stores, store_id, name, address):
    """更新门店信息。"""
    for store in stores:
        if store['id'] == store_id:
            store['name'] = name
            store['address'] = address
            return store
    return None

def delete_store(stores, store_id):
    """删除门店。"""
    stores[:] = [s for s in stores if s.get('id') != store_id]
    return stores
