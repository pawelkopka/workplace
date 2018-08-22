Terminator
***********************

Marian lubi state filmy, uważa że już nikt nie robi porządnych film. A aktualna młodziesz....
Nie też czemu jest takie  zainteresowanie AI, chyba każdy wie czy jest(będzie) skynet...
W obawie przed skynetem kożystał z terminator, ale ostatnio przeżucił się na tmux+tmuxinator.

.. image:: Robotics_Expert.png
   :scale: 40 %
   :alt: alternate text
   :align: right






Rola: Terminal
=================

Template
---------
.. literalinclude:: ../../playbooks/roles/terminal/templates/tmux.config.j2

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

   template pozwala na wypełnienie naszej konfuguracji zmiennymi `template`_

.. _template: https://docs.ansible.com/ansible/latest/modules/apt_module.html