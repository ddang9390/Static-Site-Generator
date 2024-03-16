import unittest


from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("tag", "value", [HTMLNode()], {"href": "https://www.google.com"})
        node2 = HTMLNode("tag", "value", [HTMLNode()], {"href": "https://www.google.com"})
        self.assertEqual(node, node2)

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        l1 = LeafNode("p", "This is a paragraph of text.")
        l2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        
        ans1 = "<p>This is a paragraph of text.</p>"
        ans2 = '<a href="https://www.google.com">Click me!</a>'

        self.assertEqual(l1.to_html(), ans1)
        self.assertEqual(l2.to_html(), ans2)

if __name__ == "__main__":
    unittest.main()