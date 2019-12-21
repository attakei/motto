"""Core custom transforms for docutils
"""
from docutils import nodes
from docutils.transforms import Transform
from janome.tokenizer import Tokenizer
from . import Report, TokenRepository


class TokenizeTransform(Transform):
    """Content tokenize transform.

    At paragraph and title, tokenize internal content and bind as attribute.
    """

    default_priority = 90  # Used before other transforms of jamproject

    def apply(self):
        tokenizer = Tokenizer()  # TODO: Performance issue
        for node in self.document.traverse(nodes.paragraph):
            source = node.astext()
            node["tokens"] = TokenRepository(tokenizer.tokenize(source))


class InitializeReportTransform(Transform):
    """
    """

    default_priority = 91  # Used soon after Tokeninze

    def apply(self):
        for node in self.document.traverse(nodes.paragraph):
            node["report"] = Report()