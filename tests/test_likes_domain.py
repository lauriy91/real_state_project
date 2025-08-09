import unittest

from src.likes.domain import FakeLike, toggle_like

class TestLikesDomain(unittest.TestCase):
    def setUp(self):
        self.store = FakeLike()

    def test_like_creates_record(self):
        like_id = toggle_like(self.store, user_id=1, property_id=10)
        self.assertGreater(like_id, 0)

    def test_toggle_removes_existing_like(self):
        first = toggle_like(self.store, user_id=1, property_id=10)
        self.assertGreater(first, 0)
        second = toggle_like(self.store, user_id=1, property_id=10)
        self.assertEqual(second, 0)
        self.assertIsNone(self.store.exists_id(1, 10))

    def test_delete_nonexistent_returns_zero(self):
        self.assertEqual(self.store.delete_like(999), 0)

if __name__ == "__main__":
    unittest.main()


