import unittest

from htmlnode import HTMLNode, LeafNode
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
        res = HTMLNode(None, None, None, None)

        self.assertEqual(node1, res)

    def test_props_to_html(self):
        node1 = HTMLNode("test", "test", ["test"], {
            "href": "https://www.google.com", 
            "target": "_blank",
        })
        res = ' href="https://www.google.com" target="_blank"'

        self.assertEqual(node1.props_to_html(), res)

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node1 = LeafNode("test", "test", {"key":"value"})
        node2 = LeafNode("test", "test", {"key":"value"})

        self.assertEqual(node1, node2)

    def test_not_eq(self):
        node1 = LeafNode("test", "tesgrdgt", {"key":"value"})
        node2 = LeafNode("test", "test", {"key":"value"})

        self.assertNotEqual(node1, node2)

    def test_blank(self):
        node1 = LeafNode("tag", "val")
        res = LeafNode("tag", "val", None)

        self.assertEqual(node1, res)

    def test_to_html_p_tag(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        res = "<p>This is a paragraph of text.</p>"

        self.assertEqual(node1.to_html(), res)

    def test_to_html_a_tag(self):
        node1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        res = '<a href="https://www.google.com">Click me!</a>'

        self.assertEqual(node1.to_html(), res)