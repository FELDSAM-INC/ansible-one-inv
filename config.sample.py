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

# OpenNebula XML-RPC API connection details
ONE = {
    'address': 'https://opennebula:2633/RPC2',
    'username': 'user',
    'password': 'pass'
}

# Whether to use VM name or IP (first one found) as hostname
USE_VM_NAME = False

# VM USER_TEMPLATE var to use as hostname
# Fallback:
# 1. check USE_VM_NAME and if True return use VM name
# 2. use VM IP (first one found)
HOSTNAME_USER_TEMPLATE_VAR = ''

# Skip VMs by labels
SKIP_LABELS = [
    'SomeLabel'
]
