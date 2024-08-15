import unittest

from markdown_block_converter import *

class TestMarkdownBlockConverter(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"

        block1 = "# This is a heading"
        block2 = "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
        block3 = "* This is the first list item in a list block\n* This is a list item\n* This is another list item" 

        ans = [block1, block2, block3]
        res = markdown_to_blocks(text)

        self.assertEqual(ans, res)

    def test_markdown_to_blocks_excessive_new_line(self):
        text = "# This is a heading\n\n\n\n\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"

        block1 = "# This is a heading"
        block2 = "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
        block3 = "* This is the first list item in a list block\n* This is a list item\n* This is another list item" 

        ans = [block1, block2, block3]
        res = markdown_to_blocks(text)

        self.assertEqual(ans, res)


if __name__ == "__main__":
    unittest.main()