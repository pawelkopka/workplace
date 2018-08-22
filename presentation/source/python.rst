Napiszmy historię
***********************

Playbooki powinny być jaki historia, pełna dobrze odegranych rul.

Bohater
========



Marian
-------

.. image:: edu.png
   :scale: 20 %
   :alt: alternate text
   :align: right

.. image:: hipis.png
   :scale: 50 %
   :alt: alternate text
   :align: right

Marian jest hipisem dlatego nie przepada za statycznym typowaniem, ale jest dorosły i odpowiedzialny.
Dlatego Python będzie świetnym dla niego.


Rola: Python
=============

Defaults
---------
.. literalinclude:: ../../playbooks/roles/python/defaults/main.yml

Tasks
---------
.. literalinclude:: ../../playbooks/roles/python/tasks/main.yml

Output
--------
.. code-block:: sh

    $ ansible-playbook playbooks/python.yml

    PLAY [install and config python] ***************************************************************************************************************************************************************************

    TASK [Gathering Facts] *************************************************************************************************************************************************************************************
    ok: [localhost]

    TASK [python : Add latest Python] **************************************************************************************************************************************************************************
    skipping: [localhost]

    TASK [python : install Python with dev] ********************************************************************************************************************************************************************
    changed: [localhost] => (item=[u'python3.6', u'python-dev', u'python3.6-dev', u'python3.6-venv'])

    TASK [python : install Pip] ********************************************************************************************************************************************************************************
    changed: [localhost] => (item=[u'python-pip', u'python3-pip'])

    TASK [python : install Venv for python3] *******************************************************************************************************************************************************************
    ok: [localhost]

    TASK [python : install Venv for python2] *******************************************************************************************************************************************************************
    ok: [localhost]

    PLAY RECAP *************************************************************************************************************************************************************************************************
    localhost                  : ok=5    changed=2    unreachable=0    failed=0

.. note::

   Apt jest jak każdy widzi `apt`_

.. _apt: https://docs.ansible.com/ansible/latest/modules/apt_module.html