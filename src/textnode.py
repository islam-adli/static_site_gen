from enum import Enum
from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other) -> bool:
        return (
            self.text == other.text and self.text_type == other.text_type and self.url == other.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node: TextNode):
    if not isinstance(text_node.text_type, TextType):
        raise Exception("invalid text type")
    if text_node.text_type == TextType.TEXT:
        text_leaf = LeafNode(None, text_node.text, None)
        return text_leaf
    elif text_node.text_type == TextType.BOLD:
        text_leaf = LeafNode("b", text_node.text, None)
        return text_leaf
    elif text_node.text_type == TextType.ITALIC:
        text_leaf = LeafNode("i", text_node.text, None)
        return text_leaf
    elif text_node.text_type == TextType.CODE:
        text_leaf = LeafNode("code", text_node.text, None)
        return text_leaf
    elif text_node.text_type == TextType.LINK:
        text_leaf = LeafNode("a", text_node.text, {"href": text_node.url})
        return text_leaf
    elif text_node.text_type == TextType.IMAGE:
        text_leaf = LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        return text_leaf
