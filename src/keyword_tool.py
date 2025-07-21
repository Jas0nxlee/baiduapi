def recommend_keywords(base_keyword):
    """
    根据给定的关键词推荐相关关键词。
    这是一个简单的模拟实现。
    """
    recommendations = [
        f"{base_keyword} 价格",
        f"购买 {base_keyword}",
        f"最好的 {base_keyword}",
    ]
    return recommendations

def expand_keywords(base_keyword, prefixes=None, suffixes=None):
    """
    拓展关键词。
    这是一个简单的模拟实现。
    """
    if prefixes is None:
        prefixes = ["", "最新款 "]
    if suffixes is None:
        suffixes = ["", " 推荐"]

    expanded = []
    for prefix in prefixes:
        for suffix in suffixes:
            expanded.append(f"{prefix}{base_keyword}{suffix}".strip())
    return list(set(expanded))
