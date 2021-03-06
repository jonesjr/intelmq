# -*- coding: utf-8 -*-

import unittest

import intelmq.lib.test as test
from intelmq.bots.parsers.cleanmx.parser_phishing import \
    CleanMXPhishingParserBot


class TestCleanMXPhishingParserBot(test.BotTestCase, unittest.TestCase):
    """
    A TestCase for CleanMXPhishingParserBot.
    """

    @classmethod
    def set_bot(cls):
        cls.bot_reference = CleanMXPhishingParserBot
        cls.default_input_message = {'__type': 'Report', 'raw': 'Cg=='}

    def test_empty(self):
        self.run_bot()

if __name__ == '__main__':  # pragma: no cover
    unittest.main()
