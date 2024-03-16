import unittest


from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("tag", "value", [HTMLNode()], {"href": "https://www.google.com"})
        node2 = HTMLNode("tag", "value", [HTMLNode()], {"href": "https://www.google.com"})
        self.assertEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("tag", "value", [HTMLNode()], {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(
            'href="https://www.google.com" target="_blank"', node.props_to_html()
        )



if __name__ == "__main__":
    unittest.main()