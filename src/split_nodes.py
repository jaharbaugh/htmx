from textnode import *
from extractlinks import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        nodes = node.text.split(delimiter)
        temp_nodes = []        
        if len(nodes) % 2 == 0:
            raise ValueError("Delimiters are unmatched")
        for i, text in enumerate(nodes):
            if i%2 == 0:
                temp_nodes.append(TextNode(text, TextType.TEXT))
            else:
                temp_nodes.append(TextNode(text, text_type))

            
        new_nodes.extend(temp_nodes)

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        links = extract_markdown_links(node.text)
        
        if not links:
            return [node]
        
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
            return [node]
        
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