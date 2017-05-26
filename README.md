# ansible-one-inv

Dynamic Ansible inventory via OpenNebula API.

This script use VM Labels to create *groups*. It can take VM Name, Custom User Template Var or IP as *hostname*.

## Build

```bash
npm install
```

## Configure

See [config.sample.js](https://github.com/feldsam-inc/ansible-one-inv/blob/master/config.sample.js).

## Run

```bash
./one-inv --list
./one-inv --host <hostname>
```

## Ansible

See

- http://docs.ansible.com/ansible/intro_dynamic_inventory.html
- http://docs.ansible.com/ansible/dev_guide/developing_inventory.html