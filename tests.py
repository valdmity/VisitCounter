import unittest
from main import get_result
import server
import database as db
from datetime import datetime


class TestAPI(unittest.TestCase):
    def test_bad_request(self):
        self.assertEqual('400 BR', get_result([]))
    
    def test_should_return_smth_statistics(self):
        self.assertTrue(len(get_result(['', '-s', '-a']).split('\n')) > 0)
    
    def test_should_handle_help_command(self):
        self.assertTrue(len(get_result(['', '-h'])) > 0)


class TestServer(unittest.TestCase):
    def test_server(self):
        self.assertTrue(server.app is not None)

    def test_browser_parser(self):
        firefox = 'Mozilla/5.0 Gecko/20100101 Firefox/47.0'
        edge = 'Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59'
        safari = 'Version/13.1.1 Mobile/15E148 Safari/604.1'
        self.assertEqual(server.parse_browser(firefox), 'Firefox')
        self.assertEqual(server.parse_browser(edge), 'Edge')
        self.assertEqual(server.parse_browser(safari), 'Safari')

    def test_should_not_change_id(self):
        id = '5'
        self.assertEqual(id, server.get_user_id(id))

    def test_should_return_new_id_for_zero_id(self):
        self.assertNotEqual('0', server.get_user_id('0'))


class TestDataBase(unittest.TestCase):
    def setUp(self):
        self.db_file_path = db.DATABASE_FILE_PATH
        db.DATABASE_FILE_PATH = "TEST_db.txt"
        db.clean_db()

    def check_db_records_count(self, expected_count: int):
        self.assertEqual(expected_count, len(db.get_all_ids()))

    def check_db_records(self, expected_records: list[tuple[str, str, str]]):
        records = db.get_all_values()
        self.assertEqual(expected_records, records)

    def test_single_add_to_base(self):
        record = ("69", "*current_time*", "Amigo")
        db.add_to_db(*record)
        self.check_db_records([record])

    def test_multi_add_to_base(self):
        records = [("69", "*current_time*", "Amigo"), ("1", "1", "1"), ("2", "a_few_years_ago", "Chrome")]
        for record in records:
            db.add_to_db(*record)
        self.check_db_records(records)

    def test_get_values_count_visits_by_time(self):
        records = [("1", "2021-12-21 19:28:10", "Amigo"), ("2", "2021-12-21 19:28:10", "1"),
                   ("3", "2022-12-21 19:28:10", "Chrome"), ("3", "2022-12-21 19:28:15", "Chrome")]
        for record in records:
            db.add_to_db(*record)
        self.assertEqual({('1', '0'), ('3', '2'), ('2', '0')}, set(db.get_values_count_visits_by_time(
            datetime.strptime("2022-12-21 10:00:00", '%Y-%m-%d %H:%M:%S'))))

    def tearDown(self):
        db.DATABASE_FILE_PATH = self.db_file_path


if __name__ == '__main__':
    unittest.main()
