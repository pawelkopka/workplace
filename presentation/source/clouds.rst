Marzyciel
***********************
.. image:: fire.png
   :scale: 30 %
   :alt: alternate text
   :align: right

Marian jest marzyciel i ciągle lata obłokach. Żeby, tego dokonać potrzeby jest mu klient do aws i azure.


Rola: Clouds
=================

Templates
---------

.. literalinclude:: ../../playbooks/roles/clouds/templates/aws_cli_config.j2

.. literalinclude:: ../../playbooks/roles/clouds/templates/aws_cli_credentials.j2

defaults
---------

.. literalinclude:: ../../playbooks/roles/clouds/defaults/main.yml

Tasks
---------

.. literalinclude:: ../../playbooks/roles/clouds/tasks/main.yml

.. literalinclude:: ../../playbooks/roles/clouds/tasks/aws.yml

.. literalinclude:: ../../playbooks/roles/clouds/tasks/azure.yml

Output
--------

.. code-block:: sh
   $ ansible-vault create playbooks/roles/clouds/defaults/main.yml
   New Vault password:
   Confirm New Vault password:


   $ ansible-vault view playbooks/roles/clouds/defaults/main.yml
   Vault password:
   aws_output_format: 'table'
   aws_region: 'eu-west-1'
   aws_access_key_id: 'access_key_id'
   aws_secret_access_key: 'secret_access_key'

   $ ansible-playbook  -i inv.yml playbooks/clouds.yml --ask-vault-pass
   Vault password:

   PLAY [install and configure clouds] ******************************************************************************************************************

   TASK [Gathering Facts] *******************************************************************************************************************************
   ok: [localhost]

   TASK [clouds : install aws cli] **********************************************************************************************************************
   ok: [localhost]

   TASK [clouds : Copy AWS config] **********************************************************************************************************************
   ok: [localhost]

   TASK [clouds : Copy AWS CLI credentials] *************************************************************************************************************
   ok: [localhost]

   TASK [clouds : download azure cli] *******************************************************************************************************************
   ok: [localhost]

   PLAY RECAP *******************************************************************************************************************************************
   localhost                  : ok=5    changed=0    unreachable=0    failed=0


.. note::

   Vault pozwala na szyfrowanie plików ze zmiennymi. `vault`_

.. _vault: https://docs.ansible.com/ansible/2.4/vault.html