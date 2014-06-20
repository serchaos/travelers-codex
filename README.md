Traveler's Codex
===========

A place to find information on any item in Destiny: how to get it, what it does, and more.


Initial Setup
===========

Clone the repo, create a virtualenv and source in.

#### Install requirements and set up database
```
pip install -r requirements.txt
manage.py syncdb
manage.py loaddata rarities.json
manage.py loaddata materials.json
manage.py loaddata currencies.json
```

#### Run a local server
```
manage.py runserver
```
then navigate to localhost:8000 in browser