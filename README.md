# drinkmanager

## Installation
```bash
$ git clone ...
$ mv 
```

## Docker

### Installation, tests

Copiez ce code et collez le dans un terminal d'un serveur Docker :

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
    RUN apt-get install gettext-base apt-utils
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

⚠️ Modifiez le fichier ```execution_file.sh``` ⚠️

Vous obtenez :
```shell
└> ls -l
total 0
-rw-r--r-- 1 jerome jerome  197 sept. 21 13:37 docker-compose.yml
-rw-r--r-- 1 jerome jerome  127 sept. 21 13:37 Dockerfile
drwxr-xr-x 1 jerome jerome 4096 sept. 21 13:37 drinkmanager
-rw-r--r-- 1 jerome jerome  761 sept. 21 13:37 execution_file.sh
-rw-r--r-- 1 jerome jerome   58 sept. 21 13:37 requirements.txt
```

Il ne reste plus qu'à lancer :
```shell
docker-compose up
```

### Suppression

Tapez ceci pour tout supprimer

```shell
docker-compose down
docker rm drinkmanager_web_1 ; docker image rm drinkmanager_web ; docker image rm python:3 
cd ../
rm -rf drinkmanager
```


