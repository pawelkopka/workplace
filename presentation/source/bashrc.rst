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


.. note::

   Shell pozwala wykonywanie dowolnej komendy w shellu, na przykład grep itp.
   Za pomocą register możemy przechwycliś stdout i używć w When dla kolejnego zadania. `Shell`_

.. _Shell: https://docs.ansible.com/ansible/2.5/modules/shell_module.html