import re

def extract_markdown_images(text):
    if len(text) == 0:
        raise Exception("Invalid text")
    
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
     

def extract_markdown_links(text):
    if len(text) == 0:
        raise Exception("Invalid text")
    
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
