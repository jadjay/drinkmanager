#!/bin/bash

### VARIABLES A EDITER
export DJANGO_SUPERUSER_PASSWORD="MONPASSWORDADMIN"
export DJANGO_SUPERUSER_USERNAME="MONUSERADMIN"
export DJANGO_SUPERUSER_EMAIL="MONMAIL@ADMINISTRAT.EU"
export DJANGO_SECRETKEY="\"SECRETKEYTOGENERATE\""
export DJANGO_DEBUG=True
export DJANGO_EMAIL_HOST="''"
export DJANGO_EMAIL_PORT=589
export DJANGO_EMAIL_HOST_USER="''"
export DJANGO_EMAIL_HOST_PASSWORD="''"
export DJANGO_EMAIL_USE_TLS=True


cat drinkmanager/default_settings.py | envsubst > drinkmanager/settings.py

#cat drinkmanager/settings.py

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser --noinput

python manage.py runserver 0.0.0.0:8001

