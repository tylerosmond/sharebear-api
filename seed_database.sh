#!/bin/bash

rm db.sqlite3
rm -rf ./sharebearapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations sharebearapi
python3 manage.py migrate sharebearapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata categories
python3 manage.py loaddata conditions
python3 manage.py loaddata ages
python3 manage.py loaddata sizes
python3 manage.py loaddata weights
python3 manage.py loaddata products
