#!/bin/bash
set -e

python manage.py migrate
python manage.py collectstatic
python manage.py runserver 8000
