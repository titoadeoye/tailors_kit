#!/bin/bash

# apply database migrations
echo "Applying migrations..."
python manage.py migrate --noinput

# create a superuser if it doesn't exist
echo "Creating superuser :)..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
import os
username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f'Superuser "{username}" created.')
else:
    print(f'Superuser "{username}" already exists.')
EOF

# start the server
echo "Starting server..."
python manage.py runserver 0.0.0.0:8000