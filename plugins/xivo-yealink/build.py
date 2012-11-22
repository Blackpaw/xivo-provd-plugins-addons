# -*- coding: UTF-8 -*-

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
                '--include', '/templates/M7/T32.tpl',
                '--include', '/templates/M7/T38.tpl',
                '--include', '/templates/M7/base.tpl',
                '--include', '/templates/common/M7/base.tpl',
                '--exclude', '/templates/*',
                'common/', path])
    
    check_call(['rsync', '-rlp', '--exclude', '.*',
                '70.0/', path])
