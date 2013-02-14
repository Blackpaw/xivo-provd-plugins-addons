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


@target('1.0.5.15', 'xivo-grandstream-1.0.5.15')
def build_1_0_5_12(path):
    check_call(['rsync', '-rlp', '--exclude', '.*',
                '--include', '/templates/*',
                'common/', path])

    check_call(['rsync', '-rlp', '--exclude', '.*',
                '1.0.5.15/', path])

@target('1.0.1.40', 'xivo-grandstream-1.0.1.40')
def build_1_0_5_12(path):
    check_call(['rsync', '-rlp', '--exclude', '.*',
                '--include', '/templates/*',
                'common/', path])

    check_call(['rsync', '-rlp', '--exclude', '.*',
                '1.0.1.40/', path])
