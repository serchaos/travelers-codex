Traveler's Codex
===========

A site to collate item data for Destiny. 


Initial Dev Env Setup
===========

#### Virtualenv
Get virtualenv, create an environment to work in, and activate your terminal.
```
sudo apt-get install python-virtualenv
virtualenv codex-env --no-site-packages
cd codex-env/
codex-env$ source bin/activate
```
NOTE - you need to run this command every time you have a new terminal you want to work with the project:
```
cd codex-env/
source bin/activate
```

#### Dependencies

Install System Dependencies

This part is manual - the rest of the python dependencies will be installed automatically using pip in the next step.
```
sudo apt-get install python-dev build-essential libpq-dev libevent-dev libmemcached-dev postgresql-client node-less
```

Python Dependencies

Currently we only use one set of requirements. We should split this into a dev and prod list once we have production running.
```
pip install -r reqs.txt
```

#### Database
We are using PostgreSQL for this project.

Note: Example error: *createdb: could not connect to database template1: FATAL:  role "YOUR_USER_NAME" does not exist*
```
sudo su
su postgres
createuser --interactive
```

Create and setup the DB to run locally (run from the django directory that contains manage.py).
```
createdb -E utf-8 -e travelerscodex
```
