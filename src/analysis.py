import csv
from io import StringIO

def generate_summary_report(campaigns, adgroups, keywords, creatives):
    """生成关键指标的摘要报告。"""
    summary = {
        "total_campaigns": len(campaigns),
        "active_campaigns": len([c for c in campaigns if c['status'] == 'Active']),
        "total_adgroups": len(adgroups),
        "active_adgroups": len([ag for ag in adgroups if ag['status'] == 'Active']),
        "total_keywords": len(keywords),
        "active_keywords": len([kw for kw in keywords if kw['status'] == 'Active']),
        "total_creatives": len(creatives),
        "active_creatives": len([cr for cr in creatives if cr['status'] == 'Active']),
    }
    return summary

def generate_csv_report(data, filename):
    """生成CSV格式的报告。"""
    if not data:
        return

    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

    with open(filename, 'w', newline='') as f:
        f.write(output.getvalue())
