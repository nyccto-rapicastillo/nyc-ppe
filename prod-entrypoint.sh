#!/bin/bash
set -e

if [ "$MIGRATE" ]; then
  python manage.py migrate
fi
gunicorn -b 0.0.0.0:8000 covid_backend.wsgi
