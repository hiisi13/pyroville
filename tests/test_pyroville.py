#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pyroville
----------------------------------

Tests for `pyroville` module.
"""

import unittest
import json
from mock import patch, Mock
from pyroville import Pyroville, PlayerResource


class TestPyroville(unittest.TestCase):

    api_key = 'key'
    site_id = 'siteid'
    player_email = 'a@a.com'

    def setUp(self):
        self.player = Pyroville(self.api_key, self.site_id, sandbox=True) \
            .set_player(self.player_email)
        self.credit_url =  \
            'http://sandbox.badgeville.com/cairo/v1/{0}' \
            '/sites/{1}/players/{2}/activities' \
            .format(self.api_key, self.site_id, self.player_email)

    def test_set_player_returns_playerresource(self):
        self.assertTrue(isinstance(self.player, PlayerResource))

    def test_player_credit_makes_get_request(self):
        mock_get = Mock()
        with patch('requests.get', mock_get):
            self.player.credit({'verb': 'test'})
        self.assertEqual(len(mock_get.mock_calls), 1)

    def test_player_credit_requests_url(self):
        mock_get = Mock()
        with patch('requests.get', mock_get):
            self.player.credit({'verb': 'test'})
        request_url = mock_get.call_args_list[0][0][0]
        self.assertEqual(request_url, self.credit_url)

    def test_player_credit_passes_data(self):
        activity = {'verb': 'test'}
        mock_get = Mock()
        with patch('requests.get', mock_get):
            self.player.credit(activity)
        expected_params = {'do': 'create', 'data': json.dumps(activity)}
        mock_get.assert_called_once_with(self.credit_url,
                                         params=expected_params)

    def test_player_credit_makes_request_for_each_activity(self):
        activity, n = {'verb': 'test'}, 5
        mock_get = Mock()
        with patch('requests.get', mock_get):
            for i in range(n):
                self.player.credit(activity)
        self.assertEqual(len(mock_get.mock_calls), n)

    def test_pyroville_init_with_prod_env(self):
        piroville = Pyroville(self.api_key, self.site_id)
        self.assertTrue(piroville.base_api_url.startswith('http://api.v2'))

    def test_pyroville_init_with_sandbox_env(self):
        piroville = Pyroville(self.api_key, self.site_id, sandbox=True)
        self.assertTrue(piroville.base_api_url.startswith('http://sandbox'))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
