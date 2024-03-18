from textnode import TextNode
from block import *

import os, shutil

def main():
    static_to_public()
    generate_page("content/index.md", "template.html", "public/index.html")

def static_to_public():
    if os.path.exists("public"):
        shutil.rmtree("public")

    if os.path.exists("static"):
        copyFiles("static", "public")

    


def copyFiles(source, destination):
    if not os.path.exists(destination):
         os.mkdir(destination)

    for file in os.listdir(source):
            filePath = os.path.join(source, file)
            destPath = os.path.join(destination, file)
            if os.path.isfile(filePath):
                shutil.copy(filePath, destPath)
            else:
                copyFiles(filePath, destPath)

def extract_title(markdown):
    for line in markdown:

        if line[0] == "#":
            return line
        
    raise Exception("h1 header required")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    from_file = open(from_path).read()
    template_file = open(template_path).read()

    html = markdown_to_html_node(from_file)
    title = ""
    for child in html.children:
        if child.tag == "h1":
            title = child.children[0].value
            break

    html = html.to_html()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)



    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)

main()