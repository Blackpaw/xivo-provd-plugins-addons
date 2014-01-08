# -*- coding: utf-8 -*-

# Copyright (C) 2013-2014 Avencall
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
