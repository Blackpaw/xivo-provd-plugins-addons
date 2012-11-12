# -*- coding: UTF-8 -*-

import logging

common = {}
execfile_('common.py', common)

logger = logging.getLogger('plugin.xivo-panasonic')


MODELS = [u'KX-UT113', u'KX-UT123', u'KX-UT133', u'KX-UT136']
VERSION = u'01.133'


class PanasonicPlugin(common['BasePanasonicPlugin']):
    IS_PLUGIN = True

    _MODELS = MODELS

    pg_associator = common['BasePanasonicPgAssociator'](MODELS, VERSION)
