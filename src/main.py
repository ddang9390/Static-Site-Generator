import os, shutil
from html_generator import *

def main():
    print("Hello world")

    shutil.rmtree("public")
    os.mkdir("public")
    static_to_public("./static", "./public")

    #generate_page("./content/index.md", "./template.html", "./public/index.html")

    generate_pages_recursive("./content", "./template.html", "./public")
    

main()