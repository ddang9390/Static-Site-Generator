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
    #takes list of old nodes and returns list of new nodes
    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        new_nodes = []

        for node in old_nodes:
            if not isinstance(node, TextNode):
                new_nodes.append(node)
            if node.text_type != text_type_text:
                new_nodes.append(node)
                continue
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
        return matches
    
    
    def split_nodes_image(old_nodes):
        newnodes = []
        for node in old_nodes:
            if node.text_type != text_type_text:
                newnodes.append(node)
                continue
            
            originalText = node.text
            images = Inline.extract_markdown_images(originalText)

            #append if there are no images
            if len(images) == 0:
                newnodes.append(node)
                continue

            #go through each image
            for image in images:
                #split text from image
                sections = originalText.split(f"![{image[0]}]({image[1]})", 1)
                if len(sections) != 2:
                    raise ValueError("Invalid markdown, image section not closed")

                if sections[0] != "":
                    #append the text
                    newnodes.append(TextNode(sections[0], text_type_text))
                #append the image
                newnodes.append(
                    TextNode(
                        image[0],
                        text_type_image,
                        image[1],
                    )
                )
                originalText = sections[1]
            if originalText != "":
                newnodes.append(TextNode(originalText, text_type_text))

        return newnodes
    
    def split_nodes_link(old_nodes):
        newnodes = []
        for node in old_nodes:
            if node.text_type != text_type_text:
                newnodes.append(node)
                continue
            
            originalText = node.text
            links = Inline.extract_markdown_links(originalText)

            #append if there are no links
            if len(links) == 0:
                newnodes.append(node)
                continue

            #go through each link
            for link in links:
                #split text from link
                sections = originalText.split(f"[{link[0]}]({link[1]})", 1)
                if len(sections) != 2:
                    raise ValueError("Invalid markdown")
                
                if sections[0] != "":
                    #append the text
                    newnodes.append(TextNode(sections[0], text_type_text))
                #append the link
                newnodes.append(
                    TextNode(
                        link[0],
                        text_type_link,
                        link[1],
                    )
                )
                originalText = sections[1]

            if originalText != "":
                newnodes.append(TextNode(originalText, text_type_text))

        return newnodes
    
    def text_to_textnodes(text):
        textnodes = [TextNode(text, text_type_text)]
        textnodes = Inline.split_nodes_delimiter(textnodes,"**", text_type_bold)
        textnodes = Inline.split_nodes_delimiter(textnodes,"*", text_type_italic)
        textnodes = Inline.split_nodes_delimiter(textnodes,"`", text_type_code)
        textnodes = Inline.split_nodes_image(textnodes)
        textnodes = Inline.split_nodes_link(textnodes)

        return textnodes
