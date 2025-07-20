import csv
from io import StringIO

def batch_import_from_csv(file_path):
    """从CSV文件批量导入数据。"""
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)

def batch_export_to_csv(data, filename):
    """将数据批量导出到CSV文件。"""
    if not data:
        return

    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

    with open(filename, 'w', newline='') as f:
        f.write(output.getvalue())
