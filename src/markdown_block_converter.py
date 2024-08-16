import re

from htmlnode import *
from markdown_inline_converter import text_to_textnodes

# Types of blocks
block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

# Split markdown text into blocks
def markdown_to_blocks(markdown):
    result = markdown.split("\n\n")

    # Remove empty blocks
    count = result.count("")
    for i in range(count):
        result.remove("")

    for block in result:
        block = block.strip()

    return result

# Takes block of markdown text and returns the type it is
def block_to_block(markdown):
    str = re.split(r'(\s+)', markdown)

    if len(str) >= 3:
        if (str[0] == '#' or str[0] == '##' or str[0] == '###' or str[0] == '####' or str[0] == '#####' or str[0] == '######')  and str[1] == " ":
            return block_type_heading
        
    if str[0].startswith("```") and str[-1].endswith("```"):
        return block_type_code
    
    # Check for blockquote
    if str[0].startswith(">"):
        lines = ''.join(str).split("\n")

        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    
    # Check for unordered list
    if (str[0] == "*" or str[0] == "-") and str[1] == " ":
        lines = ''.join(str).split("\n")
        for line in lines:
            if (line[0] != "*" or line[0] != "-") and line[1] != " ":
                return block_type_paragraph
        return block_type_ulist
    
    # Check for ordered list
    if str[0] == "1." and str[1] == " ":
        index = 1
        lines = ''.join(str).split("\n")
        for line in lines:
            if line[0] != f"{index}":
                return block_type_paragraph
            index += 1
        return block_type_olist
    
    return block_type_paragraph
    

def markdown_to_html_node(markdown):
    markdown = markdown.lstrip()
    blocks = markdown_to_blocks(markdown)
    pNodeChildren = []
    pNode = ParentNode(tag="div", children=[])

    for block in blocks:
        type = block_to_block(block)
        lst = block.split()
        if type == block_type_heading:
            num = len(lst[0])
            val = " ".join(lst[1:])
            children = text_to_children(val)
            for child in children:
                child.tag = f"h{num}"
            
            pNodeChildren.extend(children)

        if type == block_type_code:
            val = " ".join(lst)
            children = text_to_children(val)

            lNode = p_node_maker(children, "code")
            pNodeChildren.append(lNode)

        if type == block_type_paragraph:
            val = " ".join(lst)
            children = text_to_children(val)

            lNode = p_node_maker(children, "p")
            pNodeChildren.append(lNode)

        if type == block_type_quote:
            lst = block.split("\n")

            val = ""

            index = 0
            for line in lst:
                if index != 0:
                    val += line[1:]
                else:
                    val += line[2:]
                index += 1
            children = text_to_children(val) 
            lNode = p_node_maker(children, "blockquote")
            pNodeChildren.append(lNode)


        if type == block_type_ulist:
            listNode = ParentNode(tag="ul", children=[])
            for line in block.split("\n"):
                val = line[2:]
                children = text_to_children(val)

                # lNode = p_node_maker(children, "ul")
                # pNodeChildren.append(lNode)
                listNode.children.append(ParentNode("li", children))

            pNodeChildren.append(listNode)

        if type == block_type_olist:
            listNode = ParentNode(tag="ol", children=[])
            for line in block.split("\n"):
                val = line[3:]
                children = text_to_children(val)

                #lNode = p_node_maker(children, "ol")
                #pNodeChildren.append(lNode)
                listNode.children.append(ParentNode("li", children))

            pNodeChildren.append(listNode)

    pNode.children = pNodeChildren
    return pNode


def text_to_children(text):
    tNodes = text_to_textnodes(text)
    children = []

    for tNode in tNodes:
        node = tNode.text_node_to_html_node()
        children.append(node)

    return children

def p_node_maker(children, tag):
    if tag == "ul" or tag == "ol":
        for child in children:
            child.tag = "li"
    pNode = ParentNode(tag=tag, children=children)

    return pNode

