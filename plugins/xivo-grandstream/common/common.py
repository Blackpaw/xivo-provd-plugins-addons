# -*- coding: utf-8 -*-

# Copyright (C) 2010-2013 Avencall
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

logger = logging.getLogger('plugin.xivo-grandstream')


class BaseGrandstreamHTTPDeviceInfoExtractor(object):

    def extract(self, request, request_type):
        return defer.succeed(self._do_extract(request))

    def _do_extract(self, request):
        ua = request.getHeader('User-Agent')
        if ua:
            return self._extract_from_ua(ua)
        return None

    def _extract_from_ua(self, ua):
        # HTTP User-Agent:
        # Grandstream Model HW GXP1405 SW 1.0.4.23 DevId 000b8240d55c
        m = ua.split()
        if m:
            raw_model = m[3]
            raw_version = m[5]
            raw_mac = m[7]
            try:
                mac = norm_mac(raw_mac.decode('ascii'))
            except ValueError, e:
                logger.warning('Could not normalize MAC address: %s', e)
            else:
                return {u'vendor': u'Grandstream',
                        u'model': raw_model.decode('ascii'),
                        u'version': raw_version.decode('ascii'),
                        u'mac': mac}
        return None


class BaseGrandstreamPgAssociator(BasePgAssociator):
    def __init__(self, models, version):
        BasePgAssociator.__init__(self)
        self._models = models
        self._version = version

    def _do_associate(self, vendor, model, version):
        if vendor == u'Grandstream':
            if model in self._models:
                if version == self._version:
                    return FULL_SUPPORT
                return COMPLETE_SUPPORT
            return UNKNOWN_SUPPORT
        return IMPROBABLE_SUPPORT


class BaseGrandstreamPlugin(StandardPlugin):
    _ENCODING = 'UTF-8'

    def __init__(self, app, plugin_dir, gen_cfg, spec_cfg):
        StandardPlugin.__init__(self, app, plugin_dir, gen_cfg, spec_cfg)
        # update to use the non-standard tftpboot directory
        self._base_tftpboot_dir = self._tftpboot_dir
        self._tftpboot_dir = os.path.join(self._tftpboot_dir, 'Grandstream')

        self._tpl_helper = TemplatePluginHelper(plugin_dir)

        downloaders = FetchfwPluginHelper.new_downloaders(gen_cfg.get('proxies'))
        fetchfw_helper = FetchfwPluginHelper(plugin_dir, downloaders)
        # update to use the non-standard tftpboot directory
        fetchfw_helper.root_dir = self._tftpboot_dir

        self.services = fetchfw_helper.services()
        self.http_service = HTTPNoListingFileService(self._base_tftpboot_dir)

    http_dev_info_extractor = BaseGrandstreamHTTPDeviceInfoExtractor()

    def _dev_specific_filename(self, device):
        # Return the device specific filename (not pathname) of device
        fmted_mac = format_mac(device[u'mac'], separator='', uppercase=False)
        return 'cfg' + fmted_mac + '.xml'

    def _check_config(self, raw_config):
        if u'http_port' not in raw_config:
            raise RawConfigError('only support configuration via HTTP')

    def _check_device(self, device):
        if u'mac' not in device:
            raise Exception('MAC address needed for device configuration')

    def configure(self, device, raw_config):
        self._check_config(raw_config)
        self._check_device(device)
        filename = self._dev_specific_filename(device)
        tpl = self._tpl_helper.get_dev_template(filename, device)

        path = os.path.join(self._tftpboot_dir, filename)
        self._tpl_helper.dump(tpl, raw_config, path, self._ENCODING)

    def deconfigure(self, device):
        self._remove_configuration_file(device)

    def _remove_configuration_file(self, device):
        path = os.path.join(self._tftpboot_dir, self._dev_specific_filename(device))
        try:
            os.remove(path)
        except OSError as e:
            logger.info('error while removing configuration file: %s', e)

    def synchronize(self, device, raw_config):
        try:
            ip = device[u'ip'].encode('ascii')
        except KeyError:
            return defer.fail(Exception('IP address needed for device synchronization'))
        else:
            sync_service = synchronize.get_sync_service()
            if sync_service is None or sync_service.TYPE != 'AsteriskAMI':
                return defer.fail(Exception('Incompatible sync service: %s' % sync_service))
            else:
                return threads.deferToThread(sync_service.sip_notify, ip, 'check-sync')
