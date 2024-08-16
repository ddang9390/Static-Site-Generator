import unittest

from html_generator import *

class TestHTMLGenerator(unittest.TestCase):
    def test_extract_title(self):
        res = extract_title("# Hello")
        ans = "Hello"

        self.assertEqual(res, ans)


if __name__ == "__main__":
    unittest.main()