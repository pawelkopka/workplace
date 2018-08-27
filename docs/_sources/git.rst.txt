Team spirit
***********************
.. image:: wspolpraca.png
   :scale: 30 %
   :alt: alternate text
   :align: right

Marian lubi pracę zespołową i czuje team spirit. Dlatego korzysta z git i nie dzieli się kodem przy użyciu pendrive,
ale że lubi kolorki w terminalu dlatego ma używa git-prompt.



Rola: Git
=================
.. code-block:: yaml

   roles/
      git/
        tasks/
            main.yml
        files/
            git-prompt-colors.sh
        templates/
            gitconfig.j2

Templates
---------
.. literalinclude:: ../../playbooks/roles/git/templates/gitconfig.j2

Files
---------
.. literalinclude:: ../../playbooks/roles/git/files/git-prompt-colors.sh

Tasks
---------
.. literalinclude:: ../../playbooks/roles/git/tasks/main.yml

Output
--------
.. code-block:: sh

   $ ansible-playbook playbooks/git.yml

   PLAY [install and configure git] *********************************************************************************************************************

   TASK [Gathering Facts] *******************************************************************************************************************************
   ok: [localhost]

   TASK [git : apt git] *********************************************************************************************************************************
   ok: [localhost]

   TASK [git : install bash-git-prompt] *****************************************************************************************************************
   ok: [localhost]

   TASK [git : copy git-prompt config] ******************************************************************************************************************
   changed: [localhost]

   TASK [git : add alias pycharm] ***********************************************************************************************************************
   changed: [localhost] => (item=GIT_PROMPT_ONLY_IN_REPO=1)
   changed: [localhost] => (item=source /home/kepok/.bash-git-prompt/gitprompt.sh)
   changed: [localhost] => (item=GIT_PROMPT_THEME_FILE=/home/kepok/.git-prompt-colors.sh)
   changed: [localhost] => (item=GIT_PROMPT_THEME=Custom)

   PLAY RECAP *******************************************************************************************************************************************
   localhost                  : ok=5    changed=2    unreachable=0    failed=0

.. note::

   Template pozwala generowanie plików, configów na podstawie zmienny. `template`_

.. _template: https://docs.ansible.com/ansible/latest/modules/template_module.html