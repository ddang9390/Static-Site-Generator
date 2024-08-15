# Static-Site-Generator

Explanation:
Textnode:
A node meant to represent different types of inline text. Will be necessary for parsing Markdown text and outputting it as HTML

Examples of such text include:
- Normal text
- Bold text
- Italic text
- Links
- Images


HTMLNode:
Represents a node in the HTML document tree

Examples:
- <p> tag and its contents
- <a> tag and its contents

Leafnode:
A type of HTMLNode that represents a single HTML tag with no children

Example:
<p>This is a paragraph</p>

ParentNode:
Handles the nesting of HTML nodes inside of one another. Any HTML node that is not a leaf node is a parent node