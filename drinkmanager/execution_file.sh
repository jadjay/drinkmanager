#!/bin/bash

export DJANGO_SECRETKEY="\"$(date | sha1sum | sed 's/ .*//')\""
cd drinkmanager
cat drinkmanager/default_settings.py | envsubst > drinkmanager/settings.py

env
echo "DSUE : $DJANGO_SUPERUSER_EMAIL"
#cat drinkmanager/settings.py

echo "########### MIGRATION "
python manage.py makemigrations
python manage.py migrate
echo "########### MIGRATION "

echo "python manage.py createsuperuser --noinput --email ${DJANGO_SUPERUSER_EMAIL} --username $DJANGO_SUPERUSER_USERNAME"
python manage.py createsuperuser --noinput --email $DJANGO_SUPERUSER_EMAIL --username $DJANGO_SUPERUSER_USERNAME

python manage.py runserver 0.0.0.0:8001

