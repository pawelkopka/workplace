Terminator
***********************
.. image:: Robotics_Expert.png
   :scale: 60 %
   :alt: alternate text
   :align: right

Marian lubi state filmy, uważa, że już nikt nie robi porządnych film. A aktualna młodzież…
Nie wie też czemu jest takie zainteresowanie AI, chyba każdy wie, czym jest (będzie) skynet…
W obawie przed skynetem korzystał z terminator, ale ostatnio przerzucił się na tmux+tmuxinator.


Rola: Terminal
=================
.. code-block:: yaml

   roles/
      terminal/
        tasks/
            main.yml
        files/
            tmux.config


File
---------
.. literalinclude:: ../../playbooks/roles/terminal/files/tmux.config

Tasks
---------
.. literalinclude:: ../../playbooks/roles/terminal/tasks/main.yml

Output
--------
.. code-block:: sh

   $ ansible-playbook playbooks/terminal.yml

   PLAY [install and config terminal] *************************************************************************************************************************************************************************

   TASK [Gathering Facts] *************************************************************************************************************************************************************************************
   ok: [localhost]

   TASK [terminal : apt terminal packates] ********************************************************************************************************************************************************************
   changed: [localhost] => (item=[u'tmux', u'tmuxinator'])

   TASK [terminal : add tmux config] **************************************************************************************************************************************************************************
   changed: [localhost]

   TASK [terminal : Create symbolic link] *********************************************************************************************************************************************************************
   ok: [localhost]

   PLAY RECAP *************************************************************************************************************************************************************************************************
   localhost                  : ok=4    changed=2    unreachable=0    failed=0

.. note::

   File pozwala na kopiowanie plików w dowolne miejsce, między innymi konfigów. `file`_

.. _file: https://docs.ansible.com/ansible/2.5/modules/file_module.html