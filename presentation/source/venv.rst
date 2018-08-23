Ekolog
***********************
.. image:: tox.png
   :scale: 100 %
   :alt: alternate text
   :align: right

Marian nie lubi toksycznego środowiska, dlatego dla każdego projektu tworzy wirtualne środowisko.
Żeby mieć przyjane i czyste zależności, w końcu "u Niego działa".


Rola: Venv
=================


Tasks
---------
.. literalinclude:: ../../playbooks/roles/venv/tasks/main.yml


.. literalinclude:: ../../playbooks/roles/venv/tasks/check_and_install.yml

Output
--------
.. code-block:: bash

   $ ansible-playbook playbooks/venv.yml

   PLAY [create projects venv] **************************************************************************************************************************

   TASK [Gathering Facts] *******************************************************************************************************************************
   ok: [localhost]

   TASK [venv : check and install req] ******************************************************************************************************************
   included: /home/kepok/projekty/workplace/playbooks/roles/venv/tasks/check_and_install.yml for localhost
   included: /home/kepok/projekty/workplace/playbooks/roles/venv/tasks/check_and_install.yml for localhost

   TASK [venv : set project dir] ************************************************************************************************************************
   ok: [localhost]

   TASK [venv : name check if req exists in /home/kepok/projects/workplace] *****************************************************************************
   ok: [localhost]

   TASK [venv : create virtualenv] **********************************************************************************************************************
   skipping: [localhost]

   TASK [venv : install /home/kepok/projects/workplace/requirements.txt] ********************************************************************************
   skipping: [localhost]

   TASK [venv : set project dir] ************************************************************************************************************************
   ok: [localhost]

   TASK [venv : name check if req exists in /home/kepok/projects/SimpleMonitoring] **********************************************************************
   ok: [localhost]

   TASK [venv : create virtualenv] **********************************************************************************************************************
   changed: [localhost]

   TASK [venv : install /home/kepok/projects/SimpleMonitoring/requirements.txt] *************************************************************************
   changed: [localhost]

   PLAY RECAP *******************************************************************************************************************************************
   localhost                  : ok=9    changed=2    unreachable=0    failed=0


.. note::

   include pozwala na użycie taksów lub playbooków wewnątrz innego tasku `include`_

.. _include: https://docs.ansible.com/ansible/2.5/modules/include_module.html