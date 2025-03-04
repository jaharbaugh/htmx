import unittest

from split_nodes import *

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(split_nodes_delimiter([], "`", TextType.TEXT), [])

    def test_no_delimiter(self):
        node = TextNode("This is some text", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([node], "`", TextType.TEXT),
            [TextNode("This is some text", TextType.TEXT)]
        )
    def test_working_delimiters(self):
        node = TextNode("hello **bold** world", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([node], '**', TextType.BOLD),
            [
             TextNode('hello ', TextType.TEXT), 
             TextNode('bold', TextType.BOLD), 
             TextNode(' world', TextType.TEXT)
            ]
        )
    def test_unmatched_delimiter(self):
        node = TextNode("Hello *italic world", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "*", TextType.ITALIC)

    def test_no_text(self):
        node = TextNode("Already bold text", TextType.BOLD)
        self.assertEqual(
            split_nodes_delimiter([node], "**", TextType.BOLD),
            [TextNode("Already bold text", TextType.BOLD)]
        )
class TestSplitNodesImage(unittest.TestCase):
    def test_single_image(self):
        node = TextNode("Look at this ![thing](https://www.google.com)", TextType.TEXT)
        self.assertEqual(split_nodes_image([node]), 
                         [
                             TextNode('Look at this ', TextType.TEXT),
                             TextNode('thing', TextType.IMAGE, 'https://www.google.com')
                         ])
    def test_multiple_images(self):
        nodes=[
            TextNode('Look at this ![thing](https://www.google.com) and check out this ![other thing](https://www.bing.com)',
                     TextType.TEXT),
            TextNode('Now look at this ![thingy](https://www.ask.com)',
                     TextType.TEXT)
        ]
        self.assertEqual(split_nodes_image(nodes),
                         [
                            TextNode("Look at this ", TextType.TEXT),
                            TextNode("thing", TextType.IMAGE, "https://www.google.com"),
                            TextNode(" and check out this ", TextType.TEXT),
                            TextNode("other thing", TextType.IMAGE, "https://www.bing.com"),
                            TextNode("Now look at this ", TextType.TEXT),
                            TextNode("thingy", TextType.IMAGE, "https://www.ask.com")
                         ])
    def test_no_images(self):
        node = TextNode("Here's some text", TextType.TEXT)
        self.assertEqual(split_nodes_image([node]), [node])

    def test_not_TEXT(self):
        node = TextNode("Here's some text", TextType.BOLD)
        self.assertEqual(split_nodes_image([node]), [node])

class TestSplitNodesLink(unittest.TestCase):
    def test_single_link(self):
        node = TextNode("Look at this [thing](https://www.google.com)", TextType.TEXT)
        self.assertEqual(split_nodes_link([node]), 
                         [
                             TextNode('Look at this ', TextType.TEXT),
                             TextNode('thing', TextType.LINK, 'https://www.google.com')
                         ])
    def test_multiple_links(self):
        nodes=[
            TextNode('Look at this [thing](https://www.google.com) and check out this [other thing](https://www.bing.com)',
                     TextType.TEXT),
            TextNode('Now look at this [thingy](https://www.ask.com)',
                     TextType.TEXT)
        ]
        self.assertEqual(split_nodes_link(nodes),
                         [
                            TextNode("Look at this ", TextType.TEXT),
                            TextNode("thing", TextType.LINK, "https://www.google.com"),
                            TextNode(" and check out this ", TextType.TEXT),
                            TextNode("other thing", TextType.LINK, "https://www.bing.com"),
                            TextNode("Now look at this ", TextType.TEXT),
                            TextNode("thingy", TextType.LINK, "https://www.ask.com")
                         ])
    def test_no_link(self):
        node = TextNode("Here's some text", TextType.TEXT)
        self.assertEqual(split_nodes_link([node]), [node])

    def test_not_TEXT(self):
        node = TextNode("Here's some text", TextType.BOLD)
        self.assertEqual(split_nodes_link([node]), [node])

class TestTextToTextNodes(unittest.TestCase):
    def test_all_in_one(self):
        text = 'This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        self.assertEqual(text_to_textnodes(text),
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ])