# -*- coding: UTF-8 -*-

import logging

common = {}
execfile_('common.py', common)

logger = logging.getLogger('plugin.xivo-grandstream')


MODELS = [u'GXP1405', u'GXP1160']
VERSION = u'1.0.5.12'


class GrandstreamPlugin(common['BaseGrandstreamPlugin']):
    IS_PLUGIN = True

    _MODELS = MODELS

    pg_associator = common['BaseGrandstreamPgAssociator'](MODELS, VERSION)
