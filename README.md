# sh
Django app
pastebin service (cocktail of features of: telegra.ph, pastebin.com, temp.sh)

Checklist:

* apt install postgresql libssl-dev libpq-dev python3.8-dev python3.8-venv gcc

* python3.8 -m venv venv
* source ./venv/bin/activate
* pip install pip -U
* pip install -r requirements.txt
* vim MainProj/MainProj/settings.py

* ip address add 192.168.0.1/24 dev ens3 (or vim /etc/network/interfaces)
* vim /etc/postgresql/12/main/postgresql.conf <-- listen_addresses = '192.168.0.1'
* vim /etc/postgresql/12/main/pg_hba.conf <-- host all all 10.8.0.4/24 md5 + host all all 192.168.0.1/24 md5
* systemctl restart postgresql
* ?passwd postgres?
* su - postgres
* psql:
\password postgres (or ALTER USER postgres PASSWORD 'pass';)
CREATE USER user WITH PASSWORD 'password';
CREATE DATABASE db OWNER user;  
ALTER ROLE user SET client_encoding TO 'utf8';   
ALTER ROLE user SET default_transaction_isolation TO 'read committed';   
ALTER ROLE user SET timezone TO 'UTC';  

* ./MainProj/manage.py migrate
* ./MainProj/manage.py createsuperuser
* ./MainProj/manage.py collectstatic

* vim gunicorn.conf.py
* vim /etc/systemd/system/sh_gunicorn.service
* systemctl enable --now sh_gunicorn.service
