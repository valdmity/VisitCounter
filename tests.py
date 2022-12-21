import unittest
from main import get_result
import server


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


if __name__ == '__main__':
    unittest.main()
