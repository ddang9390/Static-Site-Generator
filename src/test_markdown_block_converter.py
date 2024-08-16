import unittest

from markdown_block_converter import *
from htmlnode import *

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

    def test_block_to_block_paragraph(self):
        block = "This is a paragraph of text. It has some **bold** and *italic* words inside of it."

        res = block_to_block(block)
        self.assertEqual(res, block_type_paragraph)

    def test_block_to_block_paragraph(self):
        block1 = "# This is a heading"
        block2 = "## This is a heading"
        block3 = "### This is a heading"
        block4 = "#### This is a heading"
        block5 = "##### This is a heading"
        block6 = "###### This is a heading"

        res = block_to_block(block1)
        self.assertEqual(res, block_type_heading) 
        res = block_to_block(block2)
        self.assertEqual(res, block_type_heading)
        res = block_to_block(block3)
        self.assertEqual(res, block_type_heading)
        res = block_to_block(block4)
        self.assertEqual(res, block_type_heading) 
        res = block_to_block(block5)
        self.assertEqual(res, block_type_heading) 
        res = block_to_block(block6)
        self.assertEqual(res, block_type_heading) 

    def test_block_to_block_unordered(self):
        block = "* This is the first list item in a list block\n* This is a list item\n* This is another list item"

        res = block_to_block(block)
        self.assertEqual(res, block_type_ulist)
                         
    def test_block_to_block_ordered(self):
        block = "1. This is the first list item in a list block\n2. This is a list item\n3. This is another list item"

        res = block_to_block(block)
        self.assertEqual(res, block_type_olist)

    def test_block_to_block_code(self):
        block = "```This is a code```"

        res = block_to_block(block)
        self.assertEqual(res, block_type_code)

    def test_block_to_block_quote(self):
        block = ">This is a quote"

        res = block_to_block(block)
        self.assertEqual(res, block_type_quote)

    def test_heading_to_html_node(self):
        block6 = "###### This is a heading\n\n### This is a heading\n\n# This is a heading"

        res = markdown_to_html_node(block6)
        
        lNode1 = LeafNode(tag="h6", value="This is a heading")
        lNode2 = LeafNode(tag="h3", value="This is a heading")
        lNode3 = LeafNode(tag="h1", value="This is a heading")
        ans = ParentNode(tag="div", children=[lNode1, lNode2, lNode3])

        self.assertEqual(res, ans)

    def test_paragraph_and_quote_to_html_node(self):
        block6 = "This is a paragraph\n\nThis is a paragraph\n\nThis is a paragraph\n\n>This is a quote"

        res = markdown_to_html_node(block6)
        
        lNode1 = LeafNode(tag="p", value="This is a paragraph")
        lNode2 = LeafNode(tag="p", value="This is a paragraph")
        lNode3 = LeafNode(tag="p", value="This is a paragraph")
        lNode4 = LeafNode(tag="blockquote", value="This is a quote")
        ans = ParentNode(tag="div", children=[lNode1, lNode2, lNode3, lNode4])
        
        self.assertEqual(res, ans)

    def test_ulist_to_html_node(self):
        block = "* This is the first list item in a list block\n* This is a list item\n* This is another list item"

        res = markdown_to_html_node(block)

        lNode1 = LeafNode(tag="li", value="This is the first list item in a list block")
        lNode2 = LeafNode(tag="li", value="This is a list item")
        lNode3 = LeafNode(tag="li", value="This is another list item")

        listNode = ParentNode(tag="ul", children=[lNode1, lNode2, lNode3])

        ans = ParentNode(tag="div", children=[listNode])
        self.assertEqual(res, ans)

    def test_olist_to_html_node(self):
        block = "1. This is the first list item in a list block\n2. This is a list item\n3. This is another list item"

        res = markdown_to_html_node(block)

        lNode1 = LeafNode(tag="li", value="This is the first list item in a list block")
        lNode2 = LeafNode(tag="li", value="This is a list item")
        lNode3 = LeafNode(tag="li", value="This is another list item")

        listNode = ParentNode(tag="ol", children=[lNode1, lNode2, lNode3])

        ans = ParentNode(tag="div", children=[listNode])
        self.assertEqual(res, ans)
                         
if __name__ == "__main__":
    unittest.main()