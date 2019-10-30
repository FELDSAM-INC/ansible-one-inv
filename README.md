# ansible-one-inv

Dynamic Ansible inventory via OpenNebula API.

This script use VM Labels to create *groups*. It can take VM Name, Custom User Template Var or IP as *hostname*.

## How to use

### First of all, navigate to your ansible project directory and clone this repository

```
git clone https://github.com/FELDSAM-INC/ansible-one-inv.git
```

### Install dependencies and configure

```bash
cd ansible-one-inv
npm install
cp config.sample.js config.js
nano config.js # configure
cd -
```

### Test

```
./ansible-one-inv/one-inv --list
```

### Configure ansible inventory

```bash
nano ansible.cfg

...
inventory = ./ansible-one-inv/one-inv
...
```

Now you can use dynamic inventory in your playbooks. Hosts will be grouped by OpenNebula Labels to Ansible Host Groups.

### Custom SSH ports

I added support for define custom ssh port in vm user template. Just add variable `SSH_PORT` and ansible use it.

## Ansible

See

- http://docs.ansible.com/ansible/intro_dynamic_inventory.html
- http://docs.ansible.com/ansible/dev_guide/developing_inventory.html
