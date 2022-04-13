# OpenNebula Ansible Dynamic Inventory

# This inventory plugin is part of ansible community collection now

https://docs.ansible.com/ansible/latest/collections/community/general/opennebula_inventory.html

## Description

This script use VM Labels to create *groups*. It can take VM Name, Custom User Template Var or IP as *hostname*.

See

- http://docs.ansible.com/ansible/intro_dynamic_inventory.html
- http://docs.ansible.com/ansible/dev_guide/developing_inventory.html

## Development

To contribute bug patches or new features, you can use the github Pull Request model. It is assumed that code and documentation are contributed under the Apache License 2.0.

More info:

* [How to Contribute](http://opennebula.org/addons/contribute/)
* Support: [OpenNebula user forum](https://forum.opennebula.org/c/support)
* Development: [OpenNebula developers forum](https://forum.opennebula.org/c/development)
* Issues Tracking: GitHub issues (https://github.com/FELDSAM-INC/ansible-one-inv/issues)

## Authors

* Leader: Kristian Feldsam (feldsam@feldhost.net)

## Support

[FeldHost™ as OpenNebula Systems Service Partner](https://www.feldhost.net/products/opennebula) offers design, implementation, operation and management of a cloud solution based on OpenNebula.

## Compatibility

This add-on is developed and tested with:
- OpenNebula 5.8+

## Requirements

Python module `pyone`

## How to use

First of all, navigate to your ansible project directory and clone this repository.

```
git clone https://github.com/FELDSAM-INC/ansible-one-inv.git
```

Install dependencies and configure.

```bash
cd ansible-one-inv
pip install pyone
cp config.sample.py config.py
nano config.py # configure
cd -
```

Sample config:
```
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
```

Test

```
./ansible-one-inv/one-inv --list
```

Configure ansible inventory

```bash
nano ansible.cfg

...
inventory = ./ansible-one-inv/one-inv
...
```

Now you can use dynamic inventory in your playbooks. Hosts will be grouped by OpenNebula Labels to Ansible Host Groups.

## Notes

### Host groups

This script defines host groups by labels assigned to VMs in OpenNebula.  
There is one special group `All`, which contains all VMs.  
One VM can be in more groups if have more labels.

### Custom SSH ports

There is support to define custom ssh port in VM USER_TEMPLATE.  
Just add variable `SSH_PORT` and Ansible use it.

