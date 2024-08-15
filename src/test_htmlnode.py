import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
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

    def test_no_tag(self):
        node1 = LeafNode(tag=None, value="Hello World")
        res = "Hello World"

        self.assertEqual(node1.to_html(), res)


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        l1 = LeafNode("b", "Bold text")
        l2 = LeafNode(None, "Normal text")
        l3 = LeafNode("i", "italic text")
        l4 = LeafNode(None, "Normal text")

        children = [l1, l2, l3, l4]
        pNode = ParentNode(children=children, tag="p")

        res = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'

        self.assertEqual(pNode.to_html(), res)

    def test_to_html_a_tag(self):
        l1 = LeafNode("b", "Bold text")
        l2 = LeafNode(None, "Normal text")
        l3 = LeafNode("i", "italic text")
        l4 = LeafNode(None, "Normal text")

        children = [l1, l2, l3, l4]
        pNode = ParentNode(children=children, tag="a", props={"href":"site.com"})

        res = '<a href="site.com"><b>Bold text</b>Normal text<i>italic text</i>Normal text</a>'

        self.assertEqual(pNode.to_html(), res)