import unittest
from main import get_result


class TestAPI(unittest.TestCase):
    def test_bad_request(self):
        self.assertEqual('400 BR', get_result([]))


if __name__ == '__main__':
    unittest.main()
