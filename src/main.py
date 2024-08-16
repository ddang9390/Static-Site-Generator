import os, shutil
from html_generator import *

def main():
    print("Hello world")

    shutil.rmtree("public")
    os.mkdir("public")
    static_to_public("./static", "./public")

    generate_page("./content/index.md", "./template.html", "./public/index.html")

def static_to_public(source, dest):
    if not os.path.isfile(source):
        if os.path.exists(dest):
            for p in os.listdir(source):
                if os.path.isfile(p):
                    shutil.copy(p, dest)
                else:
                    static_to_public(os.path.join(source, p), os.path.join(dest, p))
        else:
            os.mkdir(dest)
            static_to_public(source, dest)
    else:
        shutil.copy(source, dest)
    
    

main()