import unittest

from markdown_converter import *

class TestMarkdownConverter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = textNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)

        res = [
            textNode("This is text with a ", text_type_text),
            textNode("code block", text_type_code),
            textNode(" word", text_type_text),
        ]

        self.assertEqual(new_nodes, res)

    def test_split_nodes_delimiter_multiple_bold(self):
        node = textNode("This is **text** with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)

        res = [
            textNode("This is ", text_type_text),
            textNode("text", text_type_bold),
            textNode(" with a ", text_type_text),
            textNode("bolded", text_type_bold),
            textNode(" word", text_type_text),
        ]

        self.assertEqual(new_nodes, res)


if __name__ == "__main__":
    unittest.main()