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

import logging

common = {}
execfile_('common.py', common)

logger = logging.getLogger('plugin.xivo-fanvil')

MODEL_VERSIONS = {
    u'C62': u'2.3',
}
COMMON_FILES = [
    ('f0C00620000.cfg', u'2012070649327421.z', 'model.tpl')
]


class FanvilPlugin(common['BaseFanvilPlugin']):
    IS_PLUGIN = True

    _MODELS = MODEL_VERSIONS
    _COMMON_FILES = COMMON_FILES

    pg_associator = common['BaseFanvilPgAssociator'](MODEL_VERSIONS, COMMON_FILES)
