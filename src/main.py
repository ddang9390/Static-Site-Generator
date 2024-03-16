from textnode import TextNode

def main():
    tNode = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(tNode.__repr__())


main()