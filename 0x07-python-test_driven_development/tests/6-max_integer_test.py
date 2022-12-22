
Sign up
AgeseVictor
/
alx-higher_level_programming
Public
Code
Issues
Pull requests
Actions
Projects
Security
Insights
alx-higher_level_programming/0x07-python-test_driven_development/tests/6-max_integer_test.py
@AgeseVictor
AgeseVictor hopeful
 1 contributor
Executable File  98 lines (76 sloc)  3.04 KB
#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer([..])"""
    def test_None(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([]), None)

    def test_no_arg(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer(), None)

    def test_similar_values(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([4, 4, 4]), 4)

    def test_single_value(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([99]), 99)

    def test_ascending_values(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([2, 7, 9]), 9)

    def test_descending_values(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([8, 3, 1]), 8)

    def test_random_values(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([13, 3, 24]), 24)

    def test_nan(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([8, float('nan'), 99]), 99)

    def test_tuples(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer((24, 45)), 45)

    def test_listoflists(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([[], [6], [2, 9]]), [6])

    def test_negative_values(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([-3, -24, -99]), -3)

    def test_strings(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer("abcdefgh"), 'h')

    def test_floats(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(8.8)

    def test_ints(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(88)

    def test_strings(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer(["", "a", "ze"]), 'ze')

    def test_inf(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([99, float('inf'),
                                     float('-inf')]), float('inf'))

    def test_dict(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([{"num": 34, 1: "a"}, {"num": 55, 2: "b"}])

    def test_mixed_list(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([24, "a"])

    def test_mixed_listoflists(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([[], [8], [12], 54, "six"])

    def test_undefined(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(NameError):
            max_integer(none)

if __name__ == '__main__':
    unittest.main()
