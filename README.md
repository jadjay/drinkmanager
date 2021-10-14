# drinkmanager

## Docker

### Installation, tests

[Installer docker](https://docs.docker.com/get-docker/)
[Installer git](https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git)

Copiez ce code et collez le dans un terminal d'un serveur Docker :

```shell
mkdir drinkmanager
cd drinkmanager
git clone https://github.com/jadjay/drinkmanager.git
cd drinkmanager/drinkmanager/
sed 's/^\s\+//' > Dockerfile <<EOF
    FROM python:3
    MAINTAINER javond@adista.fr
    
    ENV PYTHONUNBUFFERED 1
    
    RUN mkdir /code
    WORKDIR /code
    ADD . /code
    

    RUN apt-get update
    RUN apt-get install -y python3-pip python3-urllib3 gettext-base apt-utils

    RUN python -m pip install --upgrade pip
    RUN pip install -r requirements.txt

EOF
sed 's/^\s{4}//' > docker-compose.yml <<EOF
    web:
      build: .
      command: ./execution_file.sh
      volumes:
        - .:/code
      ports:
        - "8001:8001"
EOF
sed 's/^\s{4}//' > requirements.txt <<EOF
    Django
    django-extensions
    django-hvad
    django-qrcode
    django-registration
    j2cli
    Jinja2
    jsonfield
    MarkupSafe
    Pillow
    pip
    PyYAML
    requests
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


      cat drinkmanager/default_settings.py | envsubst > drinkmanager/settings.py

      #cat drinkmanager/settings.py

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

Pour reconstruire l'image
```shell
docker-compose build
```

### Suppression

Tapez ceci pour tout supprimer

```shell
docker-compose down --rmi all
cd ../../..
sudo rm -rf drinkmanager
```

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

## Utilisation

1. Connectez vous, avec le compte admin
2. Allez dans Admin
2. Cliquez sur le "ajouté" de DRINK/Drink
3. Créez une boisson avec son code EAN13 (celui du code barre de l'article)
  * Vous pouvez le trouver facilement sur [OpenFoodFacts](https://fr.openfoodfacts.org/)
4. Enregistrez et créez un nouveau
5. Une fois terminé, cliquez sur DRINK/Drinks
6. Vous avez la liste de vos code EAN13, selectionnez tout
7. Dans action prenez "Get info from openfoodfacts", et cliquez sur "Envoyer"
8. A présent cliquez "Ajouter" dans DRINK/Stocks
9. Date du jour + Quantité + Drink, enregistrez et créez bien un stock pour chaque boisson
10. Retournez sur le site web

Votre drinkmanager est prêt, il ne vous reste plus qu'à aller sur la page d'impression et imprimer avec votre navigateur.
