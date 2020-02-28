#!/bin/sh

python manage.py flush --no-input
python manage.py makemigrations --no-input
python manage.py migrate --no-input

#python manage.py collectstatic --no-input --clear
python -m scripts.fake
exec "$@"