import unittest

from solution import strict


class TestStrictDecorator(unittest.TestCase):
    def test_sum_two_with_correct_types(self):
        @strict
        def sum_two(a: int, b: int) -> int:
            return a + b

        self.assertEqual(sum_two(1, 2), 3)
        self.assertEqual(sum_two(-1, 1), 0)

    def test_sum_two_with_incorrect_types(self):
        @strict
        def sum_two(a: int, b: int) -> int:
            return a + b

        with self.assertRaises(TypeError):
            sum_two(1, 2.4)

        with self.assertRaises(TypeError):
            sum_two(1.5, 2)

        with self.assertRaises(TypeError):
            sum_two("1", 2)

        with self.assertRaises(TypeError):
            sum_two(1, "2")

    def test_function_with_different_types(self):
        @strict
        def concat_strings(a: str, b: str) -> str:
            return a + b

        self.assertEqual(concat_strings("hello", " world"), "hello world")

        with self.assertRaises(TypeError):
            concat_strings("hello", 123)

        with self.assertRaises(TypeError):
            concat_strings(123, " world")

    def test_function_with_mixed_types(self):
        @strict
        def mixed_types(a: int, b: str) -> str:
            return str(a) + b

        self.assertEqual(mixed_types(10, " apples"), "10 apples")

        with self.assertRaises(TypeError):
            mixed_types(10.5, " apples")

        with self.assertRaises(TypeError):
            mixed_types(10, 123)


if __name__ == '__main__':
    unittest.main()
