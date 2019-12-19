import pytest
from textwrap import dedent
from docutils import nodes
from docutils.core import publish_doctree
from docutils.readers import Reader
from jamproject.transforms import Skill, Tokenize
from jamproject.skills import sentence_length


skill = Skill(sentence_length.apply)


class TokenizeOnlyReader(Reader):
    def get_transforms(self):
        return super().get_transforms() + [Tokenize, skill.get_transform]


def test_safe():
    doctree = publish_doctree("本日は晴天なり", reader=TokenizeOnlyReader())
    paragraph: nodes.paragraph = doctree.children[0]
    assert "report" in paragraph.attributes
    report = paragraph.attributes["report"]
    assert len(report) == 0


def test_failure():
    doctree = publish_doctree("本日は晴天なり" * 20, reader=TokenizeOnlyReader())
    paragraph: nodes.paragraph = doctree.children[0]
    assert "report" in paragraph.attributes
    report = paragraph.attributes["report"]
    assert len(report) == 1
    assert '80' in report[0].body
    assert '140' in report[0].body
