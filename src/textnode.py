from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class textNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, t2):
        return (self.text == t2.text) and (self.text_type == t2.text_type) and (self.url == t2.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def text_node_to_html_node(self):
        lNode = LeafNode(None, "")
        if self.text_type == text_type_bold:
            lNode.tag = "b"
            lNode.value = self.text
        if self.text_type == text_type_code:
            lNode.tag = "code"
            lNode.value = self.text
        if self.text_type == text_type_image:
            lNode.tag = "img"
            lNode.value = ""
            lNode.props = {"src":self.url, "alt":self.text}
        if self.text_type == text_type_italic:
            lNode.tag = "i"
            lNode.value = self.text
        if self.text_type == text_type_link:
            lNode.tag = "a"
            lNode.value = self.text
            lNode.props = {"href":self.url}
        if self.text_type == text_type_text:
            lNode.tag = None
            lNode.value = self.text

        return lNode