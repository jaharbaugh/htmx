from extract_title import *
import unittest

class TestExtractTitle(unittest.TestCase):
    def test_normal_case(self):
        text = '''
                # Title
                More text'''
        expected = 'Title'
        extracted = extract_title(text)
        self.assertEqual(expected, extracted)
    def test_title_in_middle(self):
        text = '''Some text
                # Title
                More text'''
        expected = 'Title'
        extracted = extract_title(text)
        self.assertEqual(expected, extracted)
    def test_no_title(self):
        text = '''
                Some text
                More text'''
        with self.assertRaises(Exception):
            extract_title(text)
    def test_multiple_headers(self):
        text = '''
                # Title
                ## Smaller Title
                Some text'''
        expected = 'Title'
        extracted = extract_title(text)
        self.assertEqual(expected, extracted)
    def test_multiple_titles(self):
        text = '''
                # Title
                # Second Title
                Some text'''
        expected = 'Title'
        extracted = extract_title(text)
        self.assertEqual(expected, extracted)