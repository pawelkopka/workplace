Jak działa Ansible?
********************

Tworzymy inventory
--------------------

.. literalinclude:: inv_test.ini

Pierwszy Ping
----------------

.. code-block:: sh

   $ ansible test -m ping

   34.245.217.152 | FAILED! => {
    "changed": false,
    "module_stderr": "Shared connection to 34.245.217.152 closed.\r\n",
    "module_stdout": "/bin/sh: 1: /usr/bin/python: not found\r\n",
    "msg": "MODULE FAILURE",
    "rc": 127
   }

.. note::

   Moduł ping służy do sprawdzania, czy zdalny host jest osiągalny `ping`_

.. _ping: https://docs.ansible.com/ansible/latest/modules/ping_module.html

Instalowanie Pythona bez Pythona
----------------------------------

.. code-block:: sh

    $ ansible test -m raw -a 'sudo apt -y update && sudo apt install -y python-minimal'
    34.245.217.152 | SUCCESS | rc=0 >>
    Hit:1 http://eu-west-1.ec2.archive.ubuntu.com/ubuntu xenial InRelease
    Get:2 http://eu-west-1.ec2.archive.ubuntu.com/ubuntu xenial-updates InRelease [109 kB]
    Get:3 http://eu-west-1.ec2.archive.ubuntu.com/ubuntu xenial-backports InRelease [107 kB]
    Get:4 http://security.ubuntu.com/ubuntu xenial-security InRelease [107 kB]
    ....
    Setting up libpython-stdlib:amd64 (2.7.12-1~16.04) ...
    Setting up python (2.7.12-1~16.04) ...
    Shared connection to 34.245.217.152 closed.


.. note::

   Moduł raw nie wymaga Python. Wykonuje polecanie bezpośrednio w shellu `raw`_

.. _raw: https://docs.ansible.com/ansible/2.6/modules/raw_module.html


Drugi Ping
----------------

.. code-block:: sh

   $ ansible  test -m ping
    34.245.217.152 | SUCCESS => {
        "changed": false,
        "ping": "pong"
    }


Jak dokładnie działa ansible
------------------------------

.. code-block:: sh

   $ ansible -i inv_test.ini all -m command -a 'pwd ; sleep 30'


Tymczasem na zdalnej maszynie
-----------------------------------

.. code-block:: sh

    root@ip-172-31-9-154:/tmp# ls
    ansible_r9RBDI

    root@ip-172-31-9-154:/tmp# cd ansible_r9RBDI/

    root@ip-172-31-9-154:/tmp/ansible_r9RBDI# ls
    ansible_modlib.zip  ansible_module_command.py

    root@ip-172-31-9-154:/tmp/ansible_r9RBDI# cat ansible_module_command.py
    #!/usr/bin/python
    # -*- coding: utf-8 -*-

    # Copyright: (c) 2012, Michael DeHaan <michael.dehaan@gmail.com>, and others
    # Copyright: (c) 2016, Toshio Kuratomi <tkuratomi@ansible.com>
    #
    # GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

    from __future__ import absolute_import, division, print_function
    __metaclass__ = type

    ANSIBLE_METADATA = {'metadata_version': '1.1',
                        'status': ['stableinterface'],
                        'supported_by': 'core'}

    DOCUMENTATION = '''
    ---
    module: command
    short_description: Executes a command on a remote node
    version_added: historical
    ...