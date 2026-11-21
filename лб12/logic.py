def validate_records(records: list[dict]) -> bool:
    if not isinstance(records, list):
        return False
    seen_ids = set()
    for rec in records:
        if not isinstance(rec, dict):
            return False
        required_keys = {"id", "title", "category", "amount", "completed"}
        if not required_keys.issubset(rec.keys()):
            return False
        rec_id = rec["id"]
        title = rec["title"]
        category = rec["category"]
        amount = rec["amount"]
        completed = rec["completed"]
        if not isinstance(rec_id, int) or rec_id <= 0 or rec_id in seen_ids:
            return False
        seen_ids.add(rec_id)
        if not isinstance(title, str) or not title.strip():
            return False
        if not isinstance(category, str) or not category.strip():
            return False
        if (
            isinstance(amount, bool)
            or not isinstance(amount, int)
            or amount < 0
        ):
            return False
        if not isinstance(completed, bool):
            return False
    return True
def get_next_id(records: list[dict]) -> int:
    if not records:
        return 1
    return max(rec["id"] for rec in records) + 1
def add_record(
    records: list[dict], title: str, category: str, amount: int
) -> dict:
    clean_title = title.strip()
    clean_category = category.strip()
    if not clean_title or not clean_category or amount < 0:
        raise ValueError("Некорректные параметры записи")
    new_record = {
        "id": get_next_id(records),
        "title": clean_title,
        "category": clean_category,
        "amount": amount,
        "completed": False,
    }
    records.append(new_record)
    return new_record
def find_records(records: list[dict], query: str) -> list[dict]:
    query_clean = query.strip().lower()
    if not query_clean:
        return []
    return [
        rec for rec in records if query_clean in rec["title"].lower()
    ]
def set_completed(records: list[dict], record_id: int, completed: bool) -> bool:
    for rec in records:
        if rec["id"] == record_id:
            rec["completed"] = completed
            return True
    return False
def delete_record(records: list[dict], record_id: int) -> bool:
    for i, rec in enumerate(records):
        if rec["id"] == record_id:
            records.pop(i)
            return True
    return False
def statistics(records: list[dict]) -> dict:
    total_count = len(records)
    completed_count = sum(1 for r in records if r["completed"])
    uncompleted_count = total_count - completed_count
    total_amount = sum(r["amount"] for r in records)
    cat_stats = {}
    for r in records:
        cat = r["category"].strip()
        if cat not in cat_stats:
            cat_stats[cat] = {"count": 0, "amount": 0}
        cat_stats[cat]["count"] += 1
        cat_stats[cat]["amount"] += r["amount"]
    sorted_categories = dict(sorted(cat_stats.items(), key=lambda x: x[0]))
    return {
        "total_count": total_count,
        "completed_count": completed_count,
        "uncompleted_count": uncompleted_count,
        "total_amount": total_amount,
        "categories": sorted_categories,
    }