import unittest
from collections import defaultdict
from unittest.mock import patch, mock_open

from solution import get_animals_count_by_letter, write_to_csv


class TestAnimalCount(unittest.TestCase):
    @patch('httpx.get')
    def test_get_animals_count_by_letter(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.content = '''
        <html>
            <body>
                <a class="CategoryTreeLabel" href="/wiki/А">А</a>
                <a class="CategoryTreeLabel" href="/wiki/Б">Б</a>
                <a class="CategoryTreeLabel" href="/wiki/А">А</a>
                <a class="CategoryTreeLabel" href="/wiki/В">В</a>
            </body>
        </html>
        '''
        mock_get.return_value = mock_response

        result = get_animals_count_by_letter()
        expected_result = defaultdict(int, {'А': 2, 'Б': 1, 'В': 1})
        self.assertEqual(result, expected_result)

    @patch('builtins.open', new_callable=mock_open)
    def test_write_to_csv(self, mock_file):
        test_data = {'А': 2, 'Б': 1, 'В': 1}

        write_to_csv(test_data)
        mock_file.assert_called_once_with('beasts.csv', mode='w', newline='', encoding='utf-8')
        mock_file().write.assert_has_calls([
            unittest.mock.call('А,2\r\n'),
            unittest.mock.call('Б,1\r\n'),
            unittest.mock.call('В,1\r\n')
        ])


if __name__ == '__main__':
    unittest.main()
