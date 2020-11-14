#!/bin/bash

# Apply database migrations
# echo "Apply database migrations"
# python manage.py migrate --fake-initial
# python manage.py makemigrations
# python manage.py migrate

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:7000
