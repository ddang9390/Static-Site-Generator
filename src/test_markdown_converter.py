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

    def test_extract_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        res = extract_markdown_images(text)
        ans = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

        self.assertEqual(res, ans)

    def test_extract_links(self):
        text = "This is text with a link [to site](https://www.site.com) and [to youtube](https://www.youtube.com/)"
        res = extract_markdown_links(text)
        ans = [("to site", "https://www.site.com"), ("to youtube", "https://www.youtube.com/")]

        self.assertEqual(res, ans)

if __name__ == "__main__":
    unittest.main()