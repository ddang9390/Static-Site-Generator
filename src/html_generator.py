import shutil, os

from markdown_block_converter import *

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        type = block_to_block(block)
        if type == block_type_heading:
            lst = block.split()
            num = len(lst[0])

            if num == 1:
                return "".join(lst[1:])
            
    raise Exception("h1 header required")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    f = open(from_path, "r")
    fromFile = f.read()
    f.close()

    t = open(template_path, "r")
    templateFile = t.read()
    t.close()

    title = extract_title(fromFile)
    
    node = markdown_to_html_node(fromFile)
    html = node.to_html()

    templateFile = templateFile.replace("{{ Title }}", title)
    templateFile = templateFile.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    
    htmlFile = open(dest_path, "w")
    htmlFile.write(templateFile)

    