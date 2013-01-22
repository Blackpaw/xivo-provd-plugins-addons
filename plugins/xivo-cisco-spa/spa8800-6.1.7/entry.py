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

"""Plugin for Cisco SPA8800 in version 6.1.7."""

common_globals = {}
execfile_('common.py', common_globals)


MODEL_VERSION = {u'SPA8800': u'6.1.7'}


class CiscoPlugin(common_globals['BaseCiscoPlugin']):
    IS_PLUGIN = True
    _COMMON_FILENAMES = ['spa8800.cfg']
    
    pg_associator = common_globals['BaseCiscoPgAssociator'](MODEL_VERSION)
