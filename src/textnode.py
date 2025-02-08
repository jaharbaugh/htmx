from enum import Enum

class TextType(Enum):
    NORMAL = 'normal'
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