import unittest

from textnode import textNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = textNode("This is a text node", "bold", "url")
        node2 = textNode("This is a text node", "bold", "url")
        self.assertEqual(node1, node2)

    def test_not_eq(self):
        node1 = textNode("This is a text node", "bbfdbfdold", "url")
        node2 = textNode("This is a text node", "bold", "url")
        self.assertNotEqual(node1, node2)

    def test_blank_url(self):
        node1 = textNode("This is a text node", "bbfdbfdold", "")
        node2 = textNode("This is a text node", "bold", None)
        self.assertNotEqual(node1, node2)

    def test_repr(self):
        node1 = textNode("This is a text node", "bold", "https://test.com")
        str = node1.__repr__()
        res = 'TextNode(This is a text node, bold, https://test.com)'

        self.assertEqual(str, res)

if __name__ == "__main__":
    unittest.main()