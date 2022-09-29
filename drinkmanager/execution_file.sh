#!/bin/bash

#### VARIABLES A EDITER
#export DJANGO_SUPERUSER_PASSWORD="azerty/42"
#export DJANGO_SUPERUSER_USERNAME="jadjay"
#export DJANGO_SUPERUSER_EMAIL="jadjay@rachetjay.fr"
#export DJANGO_DEBUG=True
#export DJANGO_EMAIL_HOST="''"
#export DJANGO_EMAIL_PORT=589
#export DJANGO_EMAIL_HOST_USER="''"
#export DJANGO_EMAIL_HOST_PASSWORD="''"
#export DJANGO_EMAIL_USE_TLS=True


export DJANGO_SECRETKEY="\"$(date | sha1sum | sed 's/ .*//')\""
cd drinkmanager
cat drinkmanager/default_settings.py | envsubst > drinkmanager/settings.py

#cat drinkmanager/settings.py

echo "########### MIGRATION "
python manage.py makemigrations
python manage.py migrate
echo "########### MIGRATION "

python manage.py createsuperuser --noinput --email $DJANGO_SUPERUSER_EMAIL

python manage.py runserver 0.0.0.0:8001

