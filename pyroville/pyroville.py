#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import sys


if sys.version_info[0] > 2:
    basestring = str


def list_or_args(keys, args):
    try:
        iter(keys)
        if isinstance(keys, (basestring, str, dict)):
            keys = [keys]
    except TypeError:
        keys = [keys]
    if args:
        keys.extend(args)
    return keys


class Pyroville(object):

    def __init__(self, api_key, site_id):
        super(Pyroville, self).__init__()
        self.base_api_url = \
            'http://sandbox.badgeville.com/cairo/v1/{0}/sites/{1}' \
            .format(api_key, site_id)

    def set_player(self, email):
        return PlayerResource(email, self.base_api_url)


class PlayerResource(object):

    def __init__(self, email, base_api_url):
        super(PlayerResource, self).__init__()
        self.base_resource_url = '{0}/players/{1}'.format(base_api_url, email)

    def credit(self, activities, *args):
        activities = list_or_args(activities, args)
        credit_url = self.base_resource_url + '/activities'

        for a in activities:
            payload = {'do': 'create', 'data': json.dumps(a)}
            requests.get(credit_url, params=payload)
