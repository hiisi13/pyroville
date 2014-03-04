#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json


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
            'http://sandbox.badgeville.com/cairo/v1/{}/sites/{}' \
            .format(api_key, site_id)

    def set_player(self, email):
        return PlayerResource(email, self.base_api_url)


class PlayerResource(object):

    def __init__(self, email, base_api_url):
        super(PlayerResource, self).__init__()
        self.base_resource_url = '{}/players/{}'.format(base_api_url, email)

    def credit(self, activities, *args):
        activities = list_or_args(activities, args)
        credit_url = self.base_resource_url + '/activities'

        for a in activities:
            payload = {'do': 'create', 'data': json.dumps(a)}
            requests.get(credit_url, params=payload)
