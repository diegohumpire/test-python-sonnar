import unittest
import main


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            return s.split(2)


class TestMyMethod(unittest.TestCase):

    def test_my_method(self):
        self.assertEqual(main.test_sonnar(), "wolas wolas")


if __name__ == '__main__':
    unittest.main()
