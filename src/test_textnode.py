import unittest

from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_uneq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_url(self):
        node = TextNode("This is a url test", TextType.LINK, 'https://www.boot.dev')
        node2 = TextNode("This is a url test", TextType.LINK, 'https.www.google.com')
        self.assertNotEqual(node, node2)
if __name__ == "__main__":
    unittest.main()

class TestTextToHTML(unittest.TestCase):
    def test_text_node_to_html_node(self):
        node = TextNode("This is normal text", TextType.TEXT)
        node2 = text_node_to_html_node(node)
        expected = LeafNode(None, 'This is normal text', None)
        self.assertEqual(node2, expected)
    
    def test_b_tag(self):
        node = TextNode("This text is bold", TextType.BOLD, None)
        node2 = text_node_to_html_node(node)
        expected = LeafNode('b', 'This text is bold', None)
        self.assertEqual(node2, expected)
    
    def test_link_tag(self):
        node = TextNode("Click here", TextType.LINK, 'https://www.google.com')
        node2 = text_node_to_html_node(node)
        expected = LeafNode('a', 'Click here', None, {'href': 'https://www.google.com'})
        self.assertEqual(node2, expected)
    
    def test_img_tag(self):
        node = TextNode("Look at this", TextType.IMAGE, 'https://www.google.com')
        node2 = text_node_to_html_node(node)
        expected = LeafNode('img', "", props={'src': 'https://www.google.com', 'alt': 'Look at this' })
        self.assertEqual(node2, expected)
    
    def test_i_tag(self):
        node = TextNode("This text is in italics", TextType.ITALIC, None)
        node2 = text_node_to_html_node(node)
        expected = LeafNode('i', 'This text is in italics', None)
        self.assertEqual(node2, expected)
    
    def test_code_tag(self):
        node = TextNode("This is a bunch of code", TextType.CODE, None)
        node2 = text_node_to_html_node(node)
        expected = LeafNode('code', "This is a bunch of code", None)
        self.assertEqual(node2, expected)
    
    def test_invalid(self):
        with self.assertRaises(Exception):
            node = TextNode('This is invalid', 'spork', None)
            text_node_to_html_node(node)