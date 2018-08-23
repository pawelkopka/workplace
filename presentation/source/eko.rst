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


