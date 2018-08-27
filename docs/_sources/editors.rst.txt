Romantyk
***********************

Marian jest trochę poetą, dlatego przydałby mu się jakiś edytor. Jak że też jest trochę cebulą dlatego używa pycharm comnunity.
Nie jest też najmłodszy więc vim też mu nie jest obcy.

.. image:: old.png
   :scale: 40 %
   :alt: alternate text
   :align: right

.. image:: Intelligence.png
   :scale: 100 %
   :alt: alternate text
   :align: right




Rola: Editors
=============
.. code-block:: yaml

   roles/
      bashrc/
        tasks/
            main.yml
        defaults/
            main.yml

Defaults
---------
.. literalinclude:: ../../playbooks/roles/editors/defaults/main.yml

Tasks
---------
.. literalinclude:: ../../playbooks/roles/editors/tasks/main.yml

Output
--------
.. code-block:: sh

   $ ansible-playbook playbooks/editors.yml

   PLAY [install pycharm] *************************************************************************************************************************************************************************************

   TASK [Gathering Facts] *************************************************************************************************************************************************************************************
   ok: [localhost]

   TASK [editors : create (download) directory] ***************************************************************************************************************************************************************
   ok: [localhost]

   TASK [editors : download] **********************************************************************************************************************************************************************************
   ok: [localhost]

   TASK [editors : install] ***********************************************************************************************************************************************************************************
   ok: [localhost]

   TASK [editors : add alias pycharm] *************************************************************************************************************************************************************************
   ok: [localhost]

   TASK [editors : install vim] *******************************************************************************************************************************************************************************
   ok: [localhost]

   PLAY RECAP *************************************************************************************************************************************************************************************************
   localhost                  : ok=6    changed=0    unreachable=0    failed=0

.. note::

   lineinfile pozwala na dodawanie linii do dowolnego pliku, na przykład bashrc `lineinfile`_

.. _lineinfile: https://docs.ansible.com/ansible/latest/modules/apt_module.html