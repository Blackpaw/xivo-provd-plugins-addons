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


# target(<target_id>, <pg_id>)
# any error raised will be considered a build error
# Pre: pg_dir is initially empty
# Pre: current directory is the one of the bplugin
@target('2.6.0.2019', 'xivo-aastra-2.6.0.2019')
def build_2_6_0_2019(path):
    check_call(['rsync', '-rlp', '--exclude', '.*',
                '--exclude', '/templates/6739i.tpl',
                'common/', path])

    check_call(['rsync', '-rlp', '--exclude', '.*',
                '2.6.0.2019/', path])


@target('3.2.2.1136', 'xivo-aastra-3.2.2.1136')
def build_3_2_2_1136(path):
    check_call(['rsync', '-rlp', '--exclude', '.*',
                '--exclude', '/templates/6751i.tpl',
                'common/', path])

    check_call(['rsync', '-rlp', '--exclude', '.*',
                '3.2.2.1136/', path])


@target('3.2.2.6268', 'xivo-aastra-3.2.2.6268')
def build_3_2_2_6268(path):
    check_call(['rsync', '-rlp', '--exclude', '.*',
                '--include', '/templates/6735i.tpl',
                '--include', '/templates/6737i.tpl',
                '--include', '/templates/base.tpl',
                '--exclude', '/templates/*',
                'common/', path])

    check_call(['rsync', '-rlp', '--exclude', '.*',
                '3.2.2.6268/', path])
