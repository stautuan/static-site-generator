import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "Click Me", None, {
                        "href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(),
                         ' href="https://www.google.com" target="_blank"')

    def test_no_tag(self):
        node = LeafNode(None, "Knowledge is power")
        self.assertEqual(node.to_html(), "Knowledge is power")

    def test_to_html(self):
        node = LeafNode("p", "Knowledge is power")
        self.assertEqual(node.to_html(), "<p>Knowledge is power</p>")


if __name__ == "__main__":
    unittest.main()
