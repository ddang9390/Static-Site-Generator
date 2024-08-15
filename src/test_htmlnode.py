import unittest

from htmlnode import HTMLNode
from textnode import text_type_bold, text_type_code, text_type_image, text_type_italic, text_type_link, text_type_text


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode("test", "test", ["test"], {"key":"value"})
        node2 = HTMLNode("test", "test", ["test"], {"key":"value"})

        self.assertEqual(node1, node2)

    def test_not_eq(self):
        node1 = HTMLNode("test", "tedrgdrgdrst", ["test"], {"key":"value"})
        node2 = HTMLNode("test", "test", ["test"], {"key":"value"})

        self.assertNotEqual(node1, node2)


    def test_repr(self):
        node1 = HTMLNode("test", "test", ["test"], {"key":"value"})
        str = node1.__repr__()
        res = "HTMLNode(test, test, ['test'], {'key': 'value'})"

        self.assertEqual(str, res)

    def test_blank(self):
        node1 = HTMLNode()
        res = HTMLNode(text_type_text, "", [], map)

        self.assertEqual(node1, res)