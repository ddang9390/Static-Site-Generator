from textnode import textNode

def main():
    print("Hello world")
    tNode = textNode("This is a text node", "bold", "https://test.com")
    str = (tNode.__repr__)
    print(str)


main()