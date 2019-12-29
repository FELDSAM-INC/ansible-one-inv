# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------- #
# Copyright 2020, FeldHost™ (feldhost.net)                                   #
#                                                                            #
# Licensed under the Apache License, Version 2.0 (the "License"); you may    #
# not use this file except in compliance with the License. You may obtain    #
# a copy of the License at                                                   #
#                                                                            #
# http://www.apache.org/licenses/LICENSE-2.0                                 #
#                                                                            #
# Unless required by applicable law or agreed to in writing, software        #
# distributed under the License is distributed on an "AS IS" BASIS,          #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.   #
# See the License for the specific language governing permissions and        #
# limitations under the License.                                             #
# -------------------------------------------------------------------------- #

import config


def get_hostname(vm):
    if not config.USE_VM_NAME and config.HOSTNAME_USER_TEMPLATE_VAR != '' and vm.USER_TEMPLATE.get(config.HOSTNAME_USER_TEMPLATE_VAR):
        return vm.USER_TEMPLATE.get(config.HOSTNAME_USER_TEMPLATE_VAR)

    if not config.USE_VM_NAME:
        return get_vm_ip(vm)

    return vm.NAME


def get_vm_ip(vm):
    nic = vm.TEMPLATE.get('NIC')

    if isinstance(nic, dict):
        nic = [nic]

    for net in nic:
        return net['IP']

    return False


def get_ssh_port(vm):
    if vm.USER_TEMPLATE.get('SSH_PORT'):
        return vm.USER_TEMPLATE.get('SSH_PORT')

    return False
