Do czego służy Ansible?
***********************

Głównie do orkiestracji dużych deplymentów, ale też do małych.


Przykład
==========

Mały deployment
----------------
2 maszyny(web i loadbalancer)

Inventory
.. literalinclude:: inv_do1.ini

Playbook dla web

.. code-block:: yaml

   - hosts: web
     tasks:
        - name: install flask with pip
          pip: name=flask
        - name: pull po
          git:
            repo: 'https://github.com/pawelkopka/my_web'
            dest: /var/www
            version: release-0.0
        - name: start flask
          shell: "flask run"
            environment:
              FLASK_APP: /var/www/flaskapp.py

Playbook dla lo

.. code-block:: yaml

   - hosts: lo
     tasks:
      - name: ensure nginx is at the latest version
        apt:
            name: nginx
            state: latest
      - name: copy the nginx config file and restart nginx
        template:
            src: config.cfg.j2
            dest: /etc/nginx/sites-available/static_site.cfg
      - name: start nginx
        service:
            name: nginx
            state: started


Większy deployment
-------------------

10 maszyny(9 web i 1 loadbalancer)

Inventory
.. literalinclude:: inv_do2.ini