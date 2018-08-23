Leń
***********************
.. image:: fire.png
   :scale: 30 %
   :alt: alternate text
   :align: right

Marian to trochę leń więc często dodaje aliasy od basha. Dlatego g to git, co bardzo często irytuje innych.
Ale Marian jest pod to.



Rola: Bashrc
=================

Files
---------
.. literalinclude:: ../../playbooks/roles/bashrc/files/aliases.sh

Tasks
---------
.. literalinclude:: ../../playbooks/roles/bashrc/tasks/main.yml

Output
--------
.. code-block:: sh

   $ ansible-playbook playbooks/bashrc.yml

   PLAY [create config place] ***************************************************************************************************************************

   TASK [Gathering Facts] *******************************************************************************************************************************
   ok: [localhost]

   TASK [bashrc : create config directory] **************************************************************************************************************
   ok: [localhost]

   TASK [bashrc : create aliases file] ******************************************************************************************************************
   changed: [localhost]

   TASK [bashrc : check aliases in bashrc user] *********************************************************************************************************
   changed: [localhost]

   TASK [bashrc : add aliases to bashrc user] ***********************************************************************************************************
   skipping: [localhost]

   TASK [bashrc : check aliases in bashrc root] *********************************************************************************************************
   changed: [localhost]

   TASK [bashrc : add aliases to bashrc root] ***********************************************************************************************************
   skipping: [localhost]

   PLAY RECAP *******************************************************************************************************************************************
   localhost                  : ok=5    changed=3    unreachable=0    failed=0

.. note::

   Shell pozwala wykonywanie dowolnej komendy w shellu, na przykład grep itp.
   Za pomocą register możemy przechwycliś stdout i używć w When dla kolejnego zadania. `Shell`_

.. _Shell: https://docs.ansible.com/ansible/2.5/modules/shell_module.html