# drinkmanager

## Installation
```bash
$ git clone ...
$ mv 
```

## Docker

```shell
mkdir drinkmanager
cd drinkmanager
sed 's/^\s\+//' > Dockerfile <<EOF
    FROM python:3
    MAINTAINER javond@adista.fr
    ENV PYTHONUNBUFFERED 1
    RUN mkdir /code
    WORKDIR /code
    RUN apt-get update
    RUN apt-get install gettext-base
    RUN pip3 install -r requirements.txt
    ADD . /code/
EOF
sed 's/^\s\+//' > requirements.txt <<EOF
    Django
    django-registration
    django-qrcode
    jsonfield
    Pillow
EOF
git clone https://github.com/jadjay/drinkmanager.git
sed 's/^\s{4}//' > docker-compose.yml <<EOF
    web:
      build: .
      command: ./execution_file.sh
      volumes:
        - .:/code
      ports:
        - "8001:8001"
EOF
sed 's/^\s\+//' > execution_file.sh <<EOF
      #!/bin/bash
      
      ### VARIABLES A EDITER
      export DJANGO_SUPERUSER_PASSWORD="''"
      export DJANGO_SUPERUSER_USERNAME="''"
      export DJANGO_SUPERUSER_EMAIL="''"
      export DJANGO_SECRETKEY="\"SECRETKEYTOGENERATE\""
      export DJANGO_DEBUG=True
      export DJANGO_EMAIL_HOST="''"
      export DJANGO_EMAIL_PORT=589
      export DJANGO_EMAIL_HOST_USER="''"
      export DJANGO_EMAIL_HOST_PASSWORD="''"
      export DJANGO_EMAIL_USE_TLS=True

      cd drinkmanager/drinkmanager/

      cat drinkmanager/default_settings.py | envsubst > drinkmanager/settings.py
      cat drinkmanager/settings.py

      python manage.py makemigrations
      python manage.py migrate

      python manage.py createsuperuser --noinput

      python manage.py runserver 0.0.0.0:8001
      
EOF
chmod a+x execution_file.sh
```

⚠️ Modifiez le fichier execution_file.sh ⚠️


Vous obtenez :
```shell
└> ls -l
total 0
-rw-r--r-- 1 jerome jerome  99 sept. 29 13:21 docker-compose.yml
-rw-r--r-- 1 jerome jerome 174 sept. 29 13:17 Dockerfile
drwxr-xr-x 1 jerome jerome 512 sept. 29 13:21 drinkmanager
-rw-r--r-- 1 jerome jerome  88 sept. 29 13:21 execution_file.sh
-rw-r--r-- 1 jerome jerome  58 sept. 29 13:19 requirements.txt
```

Il ne reste plus qu'à lancer :
```shell
docker-compose up
```

