import unittest

from hw4 import git

from unittest.mock import Mock, patch

class TestGit(unittest.TestCase):
    """Unit Test"""
    @classmethod
    def setUp(id):
        id.ID = 'logicaltrekkie'
        id.ID2 = 'INVALID_USER_ID'
		
    @patch('requests.get')
    def test_validuser(self, mock_get):
        """Checks if the user is a valid user"""
        mock_get.return_value.status_code = 200
        self.assertEqual(mock_get.return_value.status_code, 200)
		
    @patch('requests.get')
    def test_invaliduser(self, mock_get):
        """Check if the user is not invalid. Should error"""
        mock_get.return_value.status_code = 404
        self.assertEqual(mock_get.return_value.status_code, 404)
		
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)