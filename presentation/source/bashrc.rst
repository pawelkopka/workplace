Leń
***********************
.. image:: fire.png
   :scale: 50 %
   :alt: alternate text
   :align: right

Z Mariana trochę jest leń więc często dodaje aliasy od basha. Dlatego g to git, co bardzo często irytuje innych. Jednak Marian jest pod to.



Rola: Bashrc
=================
.. code-block:: yaml

   roles/
      bashrc/
        tasks/
            main.yml
        files/
            main.yml

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
   Za pomocą register możemy przechwycić stdout i używać w When dla kolejnego zadania. `Shell`_

.. _Shell: https://docs.ansible.com/ansible/2.5/modules/shell_module.html