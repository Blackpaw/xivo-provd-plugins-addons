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

# Depends on the following external programs:
#  -rsync

from subprocess import check_call

@target('61.0', 'xivo-yealink-61.0')
def build_61_0(path):
    check_call(['rsync', '-rlp', '--exclude', '.*',
                '--exclude', '/templates/T32.tpl',
                '--exclude', '/templates/T38.tpl',
                'common/', path])

    check_call(['rsync', '-rlp', '--exclude', '.*',
                '61.0/', path])

@target('70.0', 'xivo-yealink-70.0')
def build_70_0(path):
    check_call(['rsync', '-rlp', '--exclude', '.*',
                '--exclude', '/templates',
                'common/', path])

    check_call(['rsync', '-rlp', '--exclude', '.*',
                '70.0/', path])
