# Static-Site-Generator

This a static site generator built using Python. The generator takes the files from the content folder and uses a template HTML file to generate a static website.

## Instructions on how to use:
1. Place your Markdown and image files in the content folder
2. Run ./main.sh in your terminal
3. Open your browser and paste this URL 'http://localhost:8888'

## Explanation of how it works:

The generator reads the Markdown files in the content folder and the template.html file in the root directory. The Markdown files are converted into an HTML file for each page and they are written to the public directory.

The conversion is done by splitting the text in the Markdown files into different nodes. An exaplantion of what these nodes are can be found below

### Explanation of these different nodes:

1. Textnode:

A node meant to represent different types of inline text. Will be necessary for parsing Markdown text and outputting it as HTML

Examples of such text include:
- Normal text
- Bold text
- Italic text
- Links
- Images


2. HTMLNode:

Represents a node in the HTML document tree

Examples:
- ```<p>``` tag and its contents
- ```<a>``` tag and its contents

3. Leafnode:

A type of HTMLNode that represents a single HTML tag with no children

Example:
```<p>This is a paragraph</p>```

4. ParentNode:

Handles the nesting of HTML nodes inside of one another. Any HTML node that is not a leaf node is a parent node.

Example:
```<div><p>This is a paragraph</p></div>```