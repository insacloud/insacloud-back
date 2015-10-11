# insacloud-back
This is THE BACK

## Get started

### Set up dev environment

You have to install
- vagrant
- virtualbox

Run ``vagrant up``

When it's done you can try this url http://localhost:8080/admin (credentials : ``admin`` => ``insacloud``)

### Develop

Get started with :
- Django : https://docs.djangoproject.com/en/1.8/intro
- Virtualenv : https://virtualenv.pypa.io/en/latest/
- Ansible : https://docs.ansible.com/

Django root folder : ``/insacloud``  
Django app folder : ``/insacloud/services``

To run django commands you need to have virtualenv enabled :
- ``cd /home/vagrant/insacloud``
- ``source bin/activate``
- When you have finish : ``deactivate``

**Resart server** : (to update changes)
- ``sudo supervisorctl restart insacloud``

**Restart serrver + misc operations (make migrations ...)** :
- ``cd /vagrant/ansible``
- ``ansible-playbook -i inventories/dev site.yml``

## TODO

- Implement data feed system for developpment
- Test vagrant with linux (files permissions)