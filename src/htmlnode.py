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
        s = []
        for prop in self.props:
            s.append(f'{prop}="{self.props[prop]}"')

        return " ".join(s)
    
    def __repr_(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"