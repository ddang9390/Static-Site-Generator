class textNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eg__(t1, t2):
        return (t1.text == t2.text) and (t1.text_type == t2.text_type) and (t1.url == t2.url)

    def __repr__(textNode):
        return "TextNode(" + textNode.text + ", " + textNode.text_type + ", " + textNode.url + ")"

