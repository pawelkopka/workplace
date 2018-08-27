Robo-leń
**************************
.. image:: robo.png
   :scale: 120 %
   :alt: alternate text
   :align: right

Marian lubi automatyzacje. Dlatego wkłada wiele ról w jeden playbook.


Playbook
---------
   .. literalinclude:: ../../playbooks/deploy.yml


Output
--------
.. code-block:: sh

    $ time ansible-playbook playbooks/deploy.yml --ask-vault-pass

   .....

   PLAY RECAP *************************************************************************************************************************************************************************************************
   34.250.28.34               : ok=48   changed=30   unreachable=0    failed=0

   real    4m23.447s
   user    0m26.480s
   sys     0m6.276s


