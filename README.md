# drinkmanager

## Installation à la mano

```bash
$ sudo apt install pipenv git 
$ git clone https://github.com/jadjay/drinkmanager.git
$ cd drinkmanager/drinkmanager/
$ pipenv sync
$ pipenv shell
```

On génère la configuration de developpement (cf drinkmanager/template_values.yaml)

```shell
$ cat > /tmp/dm_dev.yaml <<EOF

secure_key: Ahveuy1MahlahqueithohbeePhazieXa
# utilisez la commande `pwgen 32` par exemple 
debug: True
#allowed_hosts:
databases:
    name: db.dm_dev.sqlite3
    engine: django.db.backends.sqlite3

email:
  host: "smtp.cheztoi.fr"
  port: 587
  user: 'LUsurier'
  password: 'Soyez ma muse'
  tls: True

EOF
$ j2 template_settings.py.j2 /tmp/dm_dev.yaml > drinkmanager/settings_dev.py

```

On lance les commandes suivantes :

```shell
$ DJANGO_SETTINGS_MODULE=drinkmanager.settings_dev ./manage.py runserver
```
> Troubleshoot : Il peut arriver qu'un message d'erreur vous demande de faire les migrations au préalable

```shell
$ DJANGO_SETTINGS_MODULE=drinkmanager.settings_dev ./manage.py migrate
$ DJANGO_SETTINGS_MODULE=drinkmanager.settings_dev ./manage.py runserver
```

Pour vous familiariser avec la commande manage :
```shell
$ DJANGO_SETTINGS_MODULE=drinkmanager.settings_dev ./manage.py help
$ DJANGO_SETTINGS_MODULE=drinkmanager.settings_dev ./manage.py help runserver
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
    ADD . /code
    
    RUN apt update
    RUN apt install pipenv git apt-utils gettext-base
    RUN pipenv sync
    
EOF
git clone https://github.com/jadjay/drinkmanager.git
cd drinkmanager/drinkmanager/
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

      #cat drinkmanager/settings.py

      pipenv exec manage.py makemigrations
      pipenv exec manage.py migrate

      pipenv exec manage.py createsuperuser --noinput

      pipenv exec manage.py runserver 0.0.0.0:8001
      
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
sudo rm -rf drinkmanager
```
