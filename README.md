# insacloud-back
---
This is THE BACK

## API

restful
- http://localhost:8080/api/  

custom  
- ``/api/events/{{id}}/generate_mosaic``: generate mosaic for an event (not should be called: testing)
- ``/api/mosaics/get_image``: get mosaic or tile (return **url**)
  - ``event``: event id (**int, required**)
  - ``level``: 0 for all mosaic, > 0 for tiles (**int, required**)
  - ``row``: tile at row (int, only if level > 0) 
  - ``column``: tile at column (int, only if level > 0)
  
0 <= row, column < 4^(level) (ex for level = 2, 0 <= row, colum < 4^2 = 16)

filters
- ``/api/events/``
  - ``latitude``
  - ``longitude``
  - ``radius`` (km)

mosaics are auto-generated every time GENERATE_MOSAIC_STEP images has been added

## Useful stuff
---
### urls
http://localhost:8080/admin/  
http://localhost:8080/api/  

## Get started
---
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

**Resart server :**
- ``sudo supervisorctl restart insacloud``

**Redeploy sproject :** (to excute django migrations ...)
- ``deploy_local``

## TODO
---
- Implement data feed system for developpment