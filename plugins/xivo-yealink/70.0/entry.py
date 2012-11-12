# -*- coding: UTF-8 -*-

"""Plugin for Yealink phones using the 70.0.XX firmware.

The following Yealink phones are supported:
- T32P
- T38P

"""

common_globals = {}
execfile_('common.py', common_globals)


MODEL_VERSIONS = {u'T32P': u'32.70.0.100',
                  u'T38P': u'38.70.0.100'}
COMMON_FILES = [('y000000000032.cfg', u'32.70.0.100.rom'),
                ('y000000000038.cfg', u'38.70.0.100.rom')]


class YealinkPlugin(common_globals['BaseYealinkPlugin']):
    IS_PLUGIN = True
    
    pg_associator = common_globals['BaseYealinkPgAssociator'](MODEL_VERSIONS)

    # Yealink plugin specific stuff
    
    _COMMON_FILES = COMMON_FILES
