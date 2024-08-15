import unittest

from textnode import *


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

    def test_text_to_text(self):
        tNode = textNode("text", text_type_text, None)
        res = "text"

        lNode = tNode.text_node_to_html_node()
        self.assertEqual(lNode.to_html(), res)

    def test_text_to_bold(self):
        tNode = textNode("text", text_type_bold, None)
        res = "<b>text</b>"

        lNode = tNode.text_node_to_html_node()
        self.assertEqual(lNode.to_html(), res)

    def test_text_to_italic(self):
        tNode = textNode("text", text_type_italic, None)
        res = "<i>text</i>"

        lNode = tNode.text_node_to_html_node()
        self.assertEqual(lNode.to_html(), res)

    def test_text_to_code(self):
        tNode = textNode("text", text_type_code, None)
        res = "<code>text</code>"

        lNode = tNode.text_node_to_html_node()
        self.assertEqual(lNode.to_html(), res)

    def test_text_to_link(self):
        tNode = textNode("text", text_type_link, "site.com")
        res = '<a href="site.com">text</a>'

        lNode = tNode.text_node_to_html_node()
        self.assertEqual(lNode.to_html(), res)

    def test_text_to_image(self):
        tNode = textNode("text", text_type_image, "site.com")
        res = '<img src="site.com" alt="text"></img>'

        lNode = tNode.text_node_to_html_node()
        self.assertEqual(lNode.to_html(), res)

if __name__ == "__main__":
    unittest.main()