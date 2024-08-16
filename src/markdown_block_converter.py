import re

# Types of blocks
block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

# Split markdown text into blocks
def markdown_to_blocks(markdown):
    result = markdown.split("\n\n")

    # Remove empty blocks
    count = result.count("")
    for i in range(count):
        result.remove("")

    for block in result:
        block = block.strip()

    return result

# Takes block of markdown text and returns the type it is
def block_to_block(markdown):
    str = re.split(r'(\s+)', markdown)

    if len(str) >= 3:
        if (str[0] == '#' or str[0] == '##' or str[0] == '###' or str[0] == '####' or str[0] == '#####' or str[0] == '######')  and str[1] == " ":
            return block_type_heading
        
    if str[0].startswith("```") and str[-1].endswith("```"):
        return block_type_code
    
    if str[0].startswith(">"):
        return block_type_quote
    
    # Check for unordered list
    if (str[0] == "*" or str[0] == "-") and str[1] == " ":
        lines = ''.join(str).split("\n")
        for line in lines:
            if (line[0] != "*" or line[0] != "-") and line[1] != " ":
                return block_type_paragraph
        return block_type_ulist
    
    # Check for ordered list
    if str[0] == "1." and str[1] == " ":
        index = 1
        lines = ''.join(str).split("\n")
        for line in lines:
            if line[0] != f"{index}":
                return block_type_paragraph
            index += 1
        return block_type_olist
    
    return block_type_paragraph
    