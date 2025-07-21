import json

def load_ocpc_packages(file_path):
    """从 JSON 文件加载oCPC投放包数据。"""
    with open(file_path, 'r') as f:
        return json.load(f)

def save_ocpc_packages(file_path, packages):
    """将oCPC投放包数据保存到 JSON 文件。"""
    with open(file_path, 'w') as f:
        json.dump(packages, f, indent=4)

def create_ocpc_package(packages, name, target_cpa):
    """创建新的oCPC投放包。"""
    new_id = max([p['id'] for p in packages]) + 1 if packages else 1
    new_package = {
        "id": new_id,
        "name": name,
        "target_cpa": target_cpa,
    }
    packages.append(new_package)
    return new_package

def get_ocpc_package_by_id(packages, package_id):
    """根据ID获取oCPC投放包。"""
    for package in packages:
        if package['id'] == package_id:
            return package
    return None
