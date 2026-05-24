from textnode import TextNode, TextType
# from htmlnode import HTMLNode


from htmlnode import ParentNode


def main():
    text_node = TextNode("some text", TextType.TEXT, "dummy.url")
    # html_node = HTMLNode("<a>", "clickable", None, {"href": "123.com", "target": "-blank"})
    # print(text_node)
    parent_node = ParentNode("div", [text_node])
    print(parent_node.to_html())


main()
