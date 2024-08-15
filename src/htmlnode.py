from textnode import text_type_bold, text_type_code, text_type_image, text_type_italic, text_type_link, text_type_text

class HTMLNode:
    def __init__(self, tag=text_type_text, value="", children=[], props=map):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        str = ""
        for key in self.props:
            str += f'{key}="{self.pros[key]}" '

        return str
    
    def __eq__(self, node):
        return self.tag == node.tag and self.value == node.value and self.children == node.children and self.props == node.props
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
