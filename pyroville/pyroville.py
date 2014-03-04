#!/usr/bin/env python
# -*- coding: utf-8 -*-


def list_or_args(keys, args):
    try:
        iter(keys)
        if isinstance(keys, (basestring, str)):
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
        self.base_api_url = base_api_url

    def credit(self, activities, *args):
        activities = list_or_args(activities, args)

        for a in activities:
            pass
