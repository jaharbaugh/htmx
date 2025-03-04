from markdowntoblocks import *
import unittest

class TestMarkdownToBlocks(unittest.TestCase):
    def test_extra_new_lines(self):
        text = '''# Heading

                Paragraph line 1
                Paragraph line 2


                * Item 1
                * Item 2'''
        blocks = markdown_to_blocks(text)
        expected = [
                    "# Heading",
                    "Paragraph line 1\nParagraph line 2",
                    "* Item 1\n* Item 2"
                    ]
        self.assertEqual(blocks, expected)
    def test_normal_case(self):
        text='''# This is a heading

                This is a paragraph of text. It has some **bold** and *italic* words inside of it.

                * This is the first list item in a list block
                * This is a list item
                * This is another list item'''
        blocks = markdown_to_blocks(text)
        expected = [
                    "# This is a heading",
                    "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                    "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
                    ]
        self.assertEqual(blocks, expected)

class TestBlockToBlockType(unittest.TestCase):
    def test_valid_heading(self):
        result = block_to_block_type("# Title")
        expected = BlockType.HEADING
        self.assertEqual(result, expected)
    def test_invalid_heading(self):
        result = block_to_block_type("#Title")
        expected = BlockType.PARAGRAPH
        self.assertEqual(result, expected)
    def test_multi_hash(self):
        result=block_to_block_type("###### Title")
        expected = BlockType.HEADING
        self.assertEqual(result, expected)
    def test_code_block(self):
        result = block_to_block_type("```\nsome code\n```")
        self.assertEqual(result, BlockType.CODE)
    def test_quote_block(self):
        result = block_to_block_type("> first line\n> second line")
        self.assertEqual(result, BlockType.QUOTE)
    def test_valid_ordered_list(self):
        result = block_to_block_type('1. a thing\n2. a second thing\n3. a third thing')
        expected = BlockType.OLIST
        self.assertEqual(result, expected)
    def test_mixed_unordered_list(self):
        result = block_to_block_type('* a thing\n- a second thing\n* a third thing')
        expected = BlockType.ULIST
        self.assertEqual(result, expected)
    def test_wrong_list(self):
        result = block_to_block_type(' 1. a thing\n3. a third thing\n2. a second thing')
        expected= BlockType.PARAGRAPH
        self.assertEqual(result, expected)  