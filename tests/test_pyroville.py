#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pyroville
----------------------------------

Tests for `pyroville` module.
"""

import unittest

from pyroville import Pyroville, PlayerResource


class TestPyroville(unittest.TestCase):

    def setUp(self):
        self.pyroville = Pyroville('', '')

    def test_set_player_returns_playerresource(self):
        self.assertIsInstance(
            self.pyroville.set_player('a@a.com'), PlayerResource)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
