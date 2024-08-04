import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "Click Me", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_no_tag(self):
        node = LeafNode(None, "Knowledge is power")
        self.assertEqual(node.to_html(), "Knowledge is power")

    def test_to_html(self):
        node = LeafNode("p", "Knowledge is power")
        self.assertEqual(node.to_html(), "<p>Knowledge is power</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("p", "Journey before destination")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><p>Journey before destination</p></div>")

    def test_to_html_many_children(self):
        node = ParentNode("p", [LeafNode("i", "One ring"), LeafNode(None, "to rule them all")])
        self.assertEqual(node.to_html(), "<p><i>One ring</i>to rule them all</p>")


if __name__ == "__main__":
    unittest.main()
