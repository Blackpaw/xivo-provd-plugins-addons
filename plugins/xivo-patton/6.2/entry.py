# -*- coding: UTF-8 -*-

"""Plugin for Patton gateways using the 6.2 firmware.

The following Patton gateways are supported:
- SN4112
- SN4114
- SN4118

"""

common_globals = {}
execfile_('common.py', common_globals)


MODELS = [u'SN4112', u'SN4114', u'SN4118']
VERSION = u'6.2'

class PattonPlugin(common_globals['BasePattonPlugin']):
    IS_PLUGIN = True

    pg_associator = common_globals['BasePattonPgAssociator'](MODELS, VERSION)

