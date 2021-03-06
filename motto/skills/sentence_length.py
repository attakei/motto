"""This skill-module return message if sentence length is more than X.
"""
import re
from motto.core import Message, SkillParams, Sentence
from motto.skill import SkillBase


default_config = {"max_length": 80}


class Skill(SkillBase):
    def proc(self, sentence: Sentence, params: SkillParams):
        config = dict(default_config)
        config.update(params)
        spacing_token = re.compile(r"\s+")
        length = sum(
            [
                len(t.surface)
                for t in sentence._tokens
                if not spacing_token.match(t.surface)
            ]
        )
        if length > int(config["max_length"]):
            return Message(
                f"Sentence length is too long. expected: {config['max_length']}, actually: {length}"
            )
