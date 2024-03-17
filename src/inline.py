from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

import re

class Inline:
    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        new_nodes = []

        for node in old_nodes:
            if not isinstance(node, TextNode):
                new_nodes.append(node)
            if node.text_type != text_type_text:
                new_nodes.append(node)
                
            new_node = []
            text = node.text.split(delimiter)
            if len(text) % 2 == 0:
                raise ValueError("Invalid markdown")
            
            for i in range(len(text)):
                if text[i] == "":
                    continue
                if i % 2 != 0:
                    new_node.append(TextNode(text[i], text_type))
                else:
                    new_node.append(TextNode(text[i], text_type_text))

            new_nodes.extend(new_node)
            
        return new_nodes
        
    #take raw text and extract alt text and url of images
    def extract_markdown_images(text):
        matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
        return matches
    
    #extracts markdown links from images
    def extract_markdown_links(text):
        matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
        print(f"Matches = {matches}")
        return matches