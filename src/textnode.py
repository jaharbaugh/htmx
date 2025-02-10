from enum import Enum
from htmlnode import *
class TextType(Enum):
    TEXT = 'normal'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        if isinstance(text_type, TextType):
            self.text_type = text_type
        else:
            self.text_type = TextType(text_type)        
        self.url = url

    def __eq__(self, obj2):
        if self.text == obj2.text and self.text_type == obj2.text_type and self.url == obj2.url:
            return True
        else:
            return False
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    match(text_node.text_type):
        case TextType.TEXT:
            return LeafNode(None, text_node.text, None)
        case TextType.BOLD:
            return LeafNode("b", text_node.text, None)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text, None)
        case TextType.CODE:
            return LeafNode('code', text_node.text, None)
        case TextType.LINK:
            return LeafNode("a", text_node.text, props={'href':text_node.url})
        case TextType.IMAGE:
            return LeafNode('img', "", props={'src': text_node.url, 'alt': text_node.text})
        case _:
            raise Exception("not a valid text type")