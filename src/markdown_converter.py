import re
from textnode import *

imageRegex = r"!\[(.*?)\]\((.*?)\)"
linkRegex = r"(?<!!)\[(.*?)\]\((.*?)\)"


# Takes a TextNode and split it into multiple nodes based on the syntax
# NOTE - currently won't be able to handle multiple levels of nesting of inline elements
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            result.append(node)
        else:
            lst = node.text.split(delimiter)
            if len(lst) % 2 == 0:
                raise Exception("Invalid Markdown syntax, please add a closing tag")
            
            for index, str in enumerate(lst):
                if index % 2 == 0:
                    node = textNode(text=str, text_type=text_type_text)
                    result.append(node)
                else:
                    node = textNode(text=str, text_type=text_type)
                    result.append(node)

    return result

# Takes markdown text and returns list of tuples
# Each tuple in list contains alt text and URL of image
def extract_markdown_images(text):
    return re.findall(imageRegex, text)


# Takes markdown text and returns list of tuples
# Each tuple in list contains anchor text and URL of link
def extract_markdown_links(text):
    return re.findall(linkRegex, text)