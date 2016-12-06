# -*- coding: utf-8 -*-

# Copyright 2013-2016 The Wazo Authors  (see the AUTHORS file)
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

import errno
import logging
import re
import os.path
from operator import itemgetter
from provd import tzinform
from provd import synchronize
from provd.devices.config import RawConfigError
from provd.plugins import StandardPlugin, FetchfwPluginHelper, \
    TemplatePluginHelper
from provd.devices.pgasso import IMPROBABLE_SUPPORT, COMPLETE_SUPPORT, \
    FULL_SUPPORT, BasePgAssociator, UNKNOWN_SUPPORT
from provd.servers.http import HTTPNoListingFileService
from provd.util import norm_mac, format_mac
from twisted.internet import defer, threads
from subprocess import call

common = {}
execfile_('common.py', common)

logger = logging.getLogger('plugin.xivo-grandstream')


MODELS = [u'GXP2000']
VERSION = u'1.2.5.3'

class BaseGrandstreamHTTPDeviceInfoExtractorGXP2000(object):

    # Grandstream GXP2000 (gxp2000e.bin:1.2.5.3/boot55e.bin:1.1.6.9) DevId 000b822726c8

    #_UA_REGEX = re.compile(r'^Grandstream Model HW (\w+) SW ([^ ]+) DevId ([^ ]+)')
    _UA_REGEX = re.compile(r'^Grandstream (\w+) .*:([^ ]+)\) DevId ([^ ]+)')

    def extract(self, request, request_type):
        return defer.succeed(self._do_extract(request))

    def _do_extract(self, request):
        ua = request.getHeader('User-Agent')
        if ua:
            return self._extract_from_ua(ua)
        return None

    def _extract_from_ua(self, ua):
        m = self._UA_REGEX.match(ua)

        if m:
            raw_model, raw_version, raw_mac= m.groups()
            try:
                mac = norm_mac(raw_mac.decode('ascii'))
            except ValueError, e:
                logger.warning('Could not normalize MAC address "%s": %s', raw_mac, e)
            else:
                return {u'vendor': u'Grandstream',
                        u'model': raw_model.decode('ascii'),
                        u'version': raw_version.decode('ascii'),
                        u'mac': mac}
        return None


class GrandstreamPlugin(common['BaseGrandstreamPlugin']):
    IS_PLUGIN = True

    _MODELS = MODELS

    http_dev_info_extractor = BaseGrandstreamHTTPDeviceInfoExtractorGXP2000()

    pg_associator = common['BaseGrandstreamPgAssociator'](MODELS, VERSION)

    def _dev_specific_filename(self, device):
        # Return the device specific filename (not pathname) of device
        fmted_mac = format_mac(device[u'mac'], separator='', uppercase=False)
        return 'cfg' + fmted_mac

    def configure(self, device, raw_config):
        logger.info('Calling GXP2000 configure')
        self._check_config(raw_config)
        self._check_device(device)
        self._check_lines_password(raw_config)
        self._add_timezone(raw_config)
        self._add_locale(raw_config)
        self._add_fkeys(raw_config)
        filename = self._dev_specific_filename(device)
        tpl = self._tpl_helper.get_dev_template('GXP2000', device)

        path = os.path.join(self._tftpboot_dir, filename)
        logger.info('Destination template = %s',path)
        self._tpl_helper.dump(tpl, raw_config, path, self._ENCODING)
        # Convert to binary
        #fmted_mac = format_mac(device[u'mac'], separator='', uppercase=False)
        #encodecmd = '/home/lindsay/GS_CFG_GEN/bin/encode.sh ' + fmted_mac + ' ' + path + ' ' + path
        #os.system(encodecmd)

    def _format_line(self, code, value):
        return u'    %s = %s' % (code, value)


        



