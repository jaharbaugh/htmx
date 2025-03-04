from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    ULIST = 'unordered_list'
    OLIST = 'ordered_list'

def markdown_to_blocks(text):
    blocks = text.split('\n')
    new_blocks =[]
    current_block = []
    for block in blocks:
        block = block.strip()
        if block != '':
            current_block.append(block)
        if block == '' and current_block !=[]:
            new_blocks.append('\n'.join(current_block))
            current_block = []
    if current_block:
        new_blocks.append('\n'.join(current_block))
    return new_blocks

def block_to_block_type(block):
    if block.startswith("#"):
        heading_num = 0
        for char in block:
            if char == '#':
                heading_num +=1
            else:
                break
        if heading_num <=6 and heading_num >=1:
            if block[heading_num] == ' ':
                return BlockType.HEADING
        return BlockType.PARAGRAPH
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif block.startswith(">"):
        lines = block.split('\n')
        all_lines_are_quotes = all(line.startswith('>') for line in lines)
        if all_lines_are_quotes: 
            return BlockType.QUOTE
        return BlockType.PARAGRAPH
    elif block.startswith("* ") or block.startswith("- "):
        lines = block.split('\n')
        stripped_lines = []
        for line in lines:
             stripped_lines.append(line.strip())
        for line in stripped_lines:
            if not (line.startswith("* ") or line.startswith("- ")):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    elif block.startswith('1. '):
        lines = block.split('\n')
        expected_number = 1
        stripped_lines = []
        for line in lines:
            stripped_lines.append(line.strip())
        for line in stripped_lines:
            if not line.startswith(f"{expected_number}. "):
                return BlockType.PARAGRAPH
            expected_number += 1
        return BlockType.OLIST
    else:
        return BlockType.PARAGRAPH
        

