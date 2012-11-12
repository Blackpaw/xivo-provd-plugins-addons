# -*- coding: UTF-8 -*-

# Depends on the following external programs:
#  -rsync

from subprocess import check_call


@target('01.133', 'xivo-panasonic-01.133')
def build_01_133(path):
    check_call(['rsync', '-rlp', '--exclude', '.*',
                '--include', '/templates/*',
                'common/', path])

    check_call(['rsync', '-rlp', '--exclude', '.*',
                '01.133/', path])
