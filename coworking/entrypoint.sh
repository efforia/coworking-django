#!/bin/sh
apt update && apt install mysql-client
pip install -r requirements.txt
python manage.py collectstatic --noinput 
mysql -u root -p -h database "create database if not exists fabrica"
# Verify if the database exists on Postgres
#if !(psql -U postgres -h db -lqt | cut -d \| -f 1 | grep -qw fabrica); then
#	psql -U postgres -h db -c "create database fabrica;" 
#fi
#python manage.py makemigrations --settings="coworking.production"
python manage.py migrate --settings="coworking.production" 
gunicorn coworking.wsgi -b 0.0.0.0:8000
