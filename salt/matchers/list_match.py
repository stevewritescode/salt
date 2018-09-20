
# -*- coding: utf-8 -*-
'''
This is the default list matcher.
'''
from __future__ import absolute_import, print_function, unicode_literals

from salt.ext import six  # pylint: disable=3rd-party-module-not-gated


def match(tgt):
    '''
    Determines if this host is on the list
    '''
    if isinstance(tgt, six.string_types):
        tgt = tgt.split(',')
    return bool(__opts__['id'] in tgt)
