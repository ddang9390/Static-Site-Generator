from textnode import text_type_bold, text_type_code, text_type_image, text_type_italic, text_type_link, text_type_text

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""

        str = ""
        for key in self.props:
            str += f' {key}="{self.props[key]}"'

        return str
    
    def __eq__(self, node):
        return self.tag == node.tag and self.value == node.value and self.children == node.children and self.props == node.props
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        
        if self.tag == None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"