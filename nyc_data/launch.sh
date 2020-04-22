#!/bin/bash
set -e
echo ">>>>> Running LAUNCH"
if [ "$MIGRATE" ]; then
  echo ">>>>> MIGRATING"
  python manage.py migrate
fi

python manage.py runserver 8000