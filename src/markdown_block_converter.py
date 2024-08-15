
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