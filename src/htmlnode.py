class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, tNode):
        return (
                self.tag == tNode.tag
                and self.value == tNode.value
                and self.children == tNode.children
                and self.props == tNode.props
            )
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        
        s = ""
        for prop in self.props:
            s += f' {prop}="{self.props[prop]}"'

        return s
    
    def __repr_(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag,value,None,props)


    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value

        href = super().props_to_html()
        return f'<{self.tag}{href}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag,None,children,props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag not initialized")
        
        if self.children == None:
            raise ValueError("Children not initialized")

        s = f"<{self.tag}>"
        for leafNode in self.children:
            s += leafNode.to_html()

        s += f"</{self.tag}>"

        return s

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"