import unittest
from unittest.mock import patch

from task2.solution import count_animals_by_letter, save_to_csv


class TestAnimalFunctions(unittest.TestCase):

    def test_count_animals_by_letter(self):
        names = ["Животное_1", "Животное_2", "Антилопа", "Барсук"]

        counts = count_animals_by_letter(names)
        expected_counts = {"Ж": 2, "А": 1, "Б": 1}

        self.assertEqual(counts, expected_counts)

    @patch("pandas.DataFrame")
    def test_save_to_csv(self, mock_to_csv):
        data = {"Ж": 2, "А": 1, "Б": 1}

        save_to_csv(data, "beasts.csv")

        mock_to_csv.assert_called_once_with(sorted(data.items()), columns=["Word", "Count"])


if __name__ == "__main__":
    unittest.main()
