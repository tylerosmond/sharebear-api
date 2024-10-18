#!/bin/bash

rm db.sqlite3
rm -rf ./sharebearapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations sharebearapi
python3 manage.py migrate sharebearapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

