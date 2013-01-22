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

"""Plugin for Cisco SPA phones using the 7.4.8 firmware.

The following Cisco phones are supported:
- SPA301
- SPA303
- SPA501G
- SPA502G
- SPA504G
- SPA508G
- SPA509G
- SPA525G

The following Cisco expansion module are supported:
- SPA500S

"""

common_globals = {}
execfile_('common.py', common_globals)


PSN = [u'301', u'303', u'501G', u'502G', u'504G', u'508G', u'509G', u'525G',
       u'525G2']
MODELS = [u'SPA' + psn for psn in PSN]
MODEL_VERSION = dict((model, u'7.4.8a') for model in MODELS)
MODEL_VERSION[u'SPA525G'] = MODEL_VERSION[u'SPA525G2'] = u'7.4.8'


class CiscoPlugin(common_globals['BaseCiscoPlugin']):
    IS_PLUGIN = True
    # similar to spa508G.cfg (G is uppercase)
    _COMMON_FILENAMES = ['spa' + psn.encode('ascii') + '.cfg' for psn in PSN]
    
    pg_associator = common_globals['BaseCiscoPgAssociator'](MODEL_VERSION)
