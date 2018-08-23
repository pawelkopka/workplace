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
.. code-block:: sh

.. note::

   include pozwala na użycie taksów lub playbooków wewnątrz innego tasku `include`_

.. _include: https://docs.ansible.com/ansible/2.5/modules/include_module.html