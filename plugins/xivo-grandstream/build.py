# -*- coding: UTF-8 -*-

# Depends on the following external programs:
#  -rsync

from subprocess import check_call


@target('1.0.5.14', 'xivo-grandstream-1.0.5.14')
def build_1_0_5_12(path):
    check_call(['rsync', '-rlp', '--exclude', '.*',
                '--include', '/templates/*',
                'common/', path])

    check_call(['rsync', '-rlp', '--exclude', '.*',
                '1.0.5.14/', path])
