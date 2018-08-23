Terminologia
*************

Inventory
==========
Plik z opisem hostów oraz grup.

Formaty:
- INI

.. literalinclude:: inv_example.ini
   :language: ini

- YAML

.. literalinclude:: inv_example.yml
   :language: YAML

- PY (Dynamic inventory)

.. literalinclude:: inv_aws.py

Moduł
======

Kody wykonywany na zdalnych maszynach.
Na przykład:

- ping
- apt
- template


Task
=====
Pojedyncze zadania wykonywane na zdalnej maszynie



.. code-block:: yaml

   - name: install python3-sphinx
     apt:
       name: python3-sphinx
       state: present


Playbook
=========
Orkiestracja zadań, konfiguracji oraz deploymentu.

.. code-block:: yaml

   - hosts: all
     tasks:
      - name: ensure nginx is at the latest version
        apt:
         name: nginx
         state: latest
      - name: start nginx
        service:
           name: nginx
           state: started

.. note::

   They are called playbooks partially because it’s a sports analogy, and it’s supposed to be fun using them. They aren’t workbooks :)`doc`_

.. _doc: https://docs.ansible.com/ansible/latest/reference_appendices/glossary.html#term-library


Role
======
Jednostka z zadaniami, konfiguracją, zmiennymi itp.

.. code-block:: yaml

   roles/
      common/
        tasks/
        handlers/
        files/
        templates/
        vars/
        defaults/
        meta/


