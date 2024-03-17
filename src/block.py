block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

from htmlnode import ParentNode
from inline import Inline
from textnode import TextNode

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    result = []
    for block in blocks:
        if block == "":
            continue
        result.append(block.strip())

    return result

def block_to_block_type(block):
    block_len = len(block)
    if block_len == 0:
        return block_type_paragraph
    
    if block[0] == "#":
        return block_type_heading
    if block[0] == ">":
        return block_type_quote
    if block[0] == "*" or block[0] == "-":
        return block_type_unordered_list
    if block_len > 1:
        if block[0] == "1" and block[1] == ".":
            return block_type_ordered_list
        if block[0] == "`":
            for line in block:
                if line[0] == "`":
                    return block_type_code

    return block_type_paragraph

def text_to_children(text):
    text_nodes = Inline.text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = TextNode.text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def block_paragraph_to_html_code(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    return ParentNode("p", text_to_children(paragraph))

def block_heading_to_html_code(block):
    s = ""
    headNum = 0
    for line in block:
        if line == "#":
            headNum += 1
        else:
            break

    fullText = block[headNum+1:]
    children = text_to_children(fullText)


    return  ParentNode(f"h{headNum}", children)

def block_code_to_html_code(block):
    lines = block[4:-3]
    paragraph = " ".join(lines)
    initial = ParentNode("code", text_to_children(paragraph))

    return ParentNode("pre", [initial])

def block_quote_to_html_code(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def block_unordered_list_to_html_code(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def block_ordered_list_to_html_code(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return block_paragraph_to_html_code(block)
    if block_type == block_type_heading:
        return block_heading_to_html_code(block)
    if block_type == block_type_code:
        return block_code_to_html_code(block)
    if block_type == block_type_ordered_list:
        return block_ordered_list_to_html_code(block)
    if block_type == block_type_unordered_list:
        return block_unordered_list_to_html_code(block)
    if block_type == block_type_quote:
        return block_quote_to_html_code(block)
    raise ValueError("Invalid block type")

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)