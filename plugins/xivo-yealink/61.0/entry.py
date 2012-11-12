# -*- coding: UTF-8 -*-

"""Plugin for Yealink phones using the 61.0.XX firmware.

The following Yealink phones are supported:
- T20P
- T22P
- T26P
- T28P

"""

common_globals = {}
execfile_('common.py', common_globals)


MODEL_VERSIONS = {u'T20P': u'9.61.0.85',
                  u'T22P': u'7.61.0.80',
                  u'T26P': u'6.61.0.83',
                  u'T28P': u'2.61.0.80'}
COMMON_FILES = [('y000000000000.cfg', u'2.61.0.80.rom'),
                ('y000000000004.cfg', u'6.61.0.83.rom'),
                ('y000000000005.cfg', u'7.61.0.80.rom'),
                ('y000000000007.cfg', u'9.61.0.85.rom')]


class YealinkPlugin(common_globals['BaseYealinkPlugin']):
    IS_PLUGIN = True
    
    pg_associator = common_globals['BaseYealinkPgAssociator'](MODEL_VERSIONS)

    # Yealink plugin specific stuff
    
    _COMMON_FILES = COMMON_FILES
