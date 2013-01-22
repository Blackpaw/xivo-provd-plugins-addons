# -*- coding: utf-8 -*-

# Copyright (C) 2013 Avencall
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

"""Plugin for Yealink phones using the 61.0.XX firmware.

The following Yealink phones are supported:
- T20P
- T22P
- T26P
- T28P

"""

common_globals = {}
execfile_('common.py', common_globals)


MODEL_VERSIONS = {u'T20P': u'9.61.0.148',
                  u'T22P': u'7.61.0.148',
                  u'T26P': u'6.61.0.148',
                  u'T28P': u'2.61.0.148'}
COMMON_FILES = [('y000000000000.cfg', u'2.61.0.148.rom'),
                ('y000000000004.cfg', u'6.61.0.148.rom'),
                ('y000000000005.cfg', u'7.61.0.148.rom'),
                ('y000000000007.cfg', u'9.61.0.148.rom')]


class YealinkPlugin(common_globals['BaseYealinkPlugin']):
    IS_PLUGIN = True
    
    pg_associator = common_globals['BaseYealinkPgAssociator'](MODEL_VERSIONS)

    # Yealink plugin specific stuff
    
    _COMMON_FILES = COMMON_FILES
