from textnode import *
from extractlinks import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
            
        text = old_node.text
        
        # Add the validation RIGHT HERE, before the split
        if text.count(delimiter) % 2 != 0:
            raise ValueError(f"Unmatched delimiter {delimiter}")
        
        segments = text.split(delimiter)
        
        # Rest of your code remains the same...
        if len(segments) == 1:
            new_nodes.append(old_node)
            continue
            
        current_type = TextType.TEXT
        for i, segment in enumerate(segments):
            if segment == "":
                continue
                
            if i % 2 == 0:
                current_type = TextType.TEXT
            else:
                current_type = text_type
                
            new_nodes.append(TextNode(segment, current_type))
            
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        links = extract_markdown_links(node.text)
        
        if not links:
            new_nodes.append(node)
            continue
        
        temp_nodes =[]
        curr_text = node.text
        for link_text, link_url in links:
                parts = curr_text.split(f"[{link_text}]({link_url})", 1)
                if parts[0]:
                    temp_nodes.append(TextNode(parts[0], TextType.TEXT))
                temp_nodes.append(TextNode(link_text, TextType.LINK, link_url))
                if len(parts) > 1:
                    curr_text = parts[1]
        if curr_text:
            temp_nodes.append(TextNode(curr_text, TextType.TEXT))
        new_nodes.extend(temp_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        images = extract_markdown_images(node.text)
        
        if not images:
            new_nodes.append(node)
            continue
        
        temp_nodes =[]
        curr_text = node.text
        for alt_text, image_url in images:
                parts = curr_text.split(f"![{alt_text}]({image_url})", 1)
                if parts[0]:
                    temp_nodes.append(TextNode(parts[0], TextType.TEXT))
                temp_nodes.append(TextNode(alt_text, TextType.IMAGE, image_url))
                if len(parts) > 1:
                    curr_text = parts[1]
        if curr_text:
            temp_nodes.append(TextNode(curr_text, TextType.TEXT))
        new_nodes.extend(temp_nodes)
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    code = split_nodes_delimiter(nodes, "`", TextType.CODE)
    images = split_nodes_image(code)
    links = split_nodes_link(images)
    bold = split_nodes_delimiter(links, "**", TextType.BOLD)
    italics = split_nodes_delimiter(bold, "*", TextType.ITALIC)
    italics_underscore = split_nodes_delimiter(italics, "_", TextType.ITALIC)
    return italics_underscore