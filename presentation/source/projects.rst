Budowniczy
***********************
.. image:: pro.png
   :scale: 30 %
   :alt: alternate text
   :align: right

Marian czasem się ludzie w różnych projektach, czasem coś na konferencje, a czasem pisz coś dla siebie.
Dlatego ma list repozytoriów, na których pracuje.



Rola: Projects
=================
.. code-block:: yaml

   roles/
      projects/
        tasks/
            main.yml

Tasks
---------
.. literalinclude:: ../../playbooks/roles/projects/tasks/main.yml

Output
--------
.. code-block:: sh

   $ ansible-playbook playbooks/projects.yml

   PLAY [pull projects] ***************************************************************************************************************************************************************************************

   TASK [Gathering Facts] *************************************************************************************************************************************************************************************
   ok: [localhost]

   TASK [projects : Ensures /home/kepok/projects dir exists] **************************************************************************************************************************************************
   ok: [localhost]

   TASK [projects : pull projects] ****************************************************************************************************************************************************************************
   changed: [localhost] => (item=https://github.com/pawelkopka/workplace)
   changed: [localhost] => (item=https://github.com/pawelkopka/SimpleMonitoring)

   PLAY RECAP *************************************************************************************************************************************************************************************************
   localhost                  : ok=3    changed=1    unreachable=0    failed=0

.. note::

   Git pozwala na zarządzanie repozytoriami. `git`_

.. _git: https://docs.ansible.com/ansible/latest/modules/git_module.html