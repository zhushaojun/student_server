#!/bin/sh

python manage.py flush --no-input
python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py shell -c "
from django.contrib.auth.models import User;
User.objects.create_superuser('admin', 'admin@example.com', 'adminpass');
User.objects.create_superuser('user1', 'user1@example.com', 'userpass');
User.objects.create_superuser('user2', 'user2@example.com', 'userpass');
"
#python manage.py collectstatic --no-input --clear
python -m scripts.fake
exec "$@"