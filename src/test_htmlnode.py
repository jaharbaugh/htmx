import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_empty(self):
        node=HTMLNode(None, None, None, None)
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})
    def test_props_to_html(self):
        node = HTMLNode(tag='a', value=None, children=None, props={
            'href': "https://www.google.com",
            'target': "_blank"
        })
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
    def test_node_with_value(self):
        node = HTMLNode(tag="p", value="Hello, World!", children=None, props=None)
        self.assertEqual(node.tag, 'p')
        self.assertEqual(node.value, 'Hello, World!')
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

class TestLeafNode(unittest.TestCase):
    def test_noTag(self):
        node = LeafNode(None, "Just some stuff", props=None)
        self.assertEqual(node.to_html(), "Just some stuff")
    def test_tag_p(self):
        node = LeafNode('p', "Standard stuff here")
        self.assertEqual(node.to_html(), "<p>Standard stuff here</p>")
    def test_tag_link(self):
        node = LeafNode('a', "Click here", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click here</a>')
    def test_value_none(self):
        node = LeafNode('p', None)
        with self.assertRaises(ValueError):
            node.to_html()    