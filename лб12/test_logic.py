import tempfile
import unittest
from logic import (
    add_record,
    delete_record,
    find_records,
    set_completed,
    statistics,
    validate_records,
)
from storage import load_records, save_records
class TestLogic(unittest.TestCase):
    def setUp(self):
        self.sample_records = [
            {
                "id": 1,
                "title": "Борщ",
                "category": "Первые блюда",
                "amount": 4,
                "completed": False,
            },
            {
                "id": 2,
                "title": "Паста Карбонара",
                "category": "Вторые блюда",
                "amount": 2,
                "completed": True,
            },
        ]

    def test_validate_records_valid(self):
        self.assertTrue(validate_records(self.sample_records))

    def test_validate_records_invalid_id(self):
        invalid_data = [
            {
                "id": -1,
                "title": "Суп",
                "category": "Первые блюда",
                "amount": 2,
                "completed": False,
            }
        ]
        self.assertFalse(validate_records(invalid_data))

    def test_add_record(self):
        records = []
        rec = add_record(records, "Оливье", "Салаты", 6)
        self.assertEqual(rec["id"], 1)
        self.assertEqual(rec["title"], "Оливье")
        self.assertFalse(rec["completed"])
        self.assertEqual(len(records), 1)

    def test_find_records(self):
        found = find_records(self.sample_records, "борщ")
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0]["id"], 1)

    def test_set_completed(self):
        res = set_completed(self.sample_records, 1, True)
        self.assertTrue(res)
        self.assertTrue(self.sample_records[0]["completed"])

    def test_delete_record(self):
        res = delete_record(self.sample_records, 1)
        self.assertTrue(res)
        self.assertEqual(len(self.sample_records), 1)
        self.assertEqual(self.sample_records[0]["id"], 2)

    def test_statistics(self):
        stats = statistics(self.sample_records)
        self.assertEqual(stats["total_count"], 2)
        self.assertEqual(stats["completed_count"], 1)
        self.assertEqual(stats["uncompleted_count"], 1)
        self.assertEqual(stats["total_amount"], 6)

    def test_storage_temp_file(self):
        with tempfile.NamedTemporaryFile(
            mode="w+", delete=False, encoding="utf-8"
        ) as tmp:
            save_records(tmp.name, self.sample_records)
            loaded = load_records(tmp.name)
            self.assertEqual(loaded, self.sample_records)
if __name__ == "main":
    unittest.main()