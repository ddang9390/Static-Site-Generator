import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

from block import (
    markdown_to_blocks
)

class TestBlock(unittest.TestCase):
    def test_markdown_to_blocks(self):
        block1 = "This is **bolded** paragraph"
        block2 = "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line"
        block3 = "* This is a list\n* with items"
        input = f"{block1}\n\n{block2}\n\n{block3}"
        
        result = markdown_to_blocks(input)
        ans = [block1, block2, block3]

        self.assertEqual(result,ans)