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
    FROM python:3.8
    MAINTAINER javond@adista.fr
    ENV PYTHONUNBUFFERED 1
    RUN mkdir /code
    WORKDIR /code
    ADD requirements.txt /code/
    RUN pip install -r requirements.txt
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
sed 's/^\s\+//' > docker-compose.yml <<EOF
    web:
      build: .
      command: ./execution_file.sh
      volumes:
        - .:/code
      ports:
        - "8001:8001"
EOF
sed 's/^\s\+//' > requirements.txt <<EOF
 > execution_file.sh <<EOF
      #!/bin/bash
      cd drinkmanager/drinkmanager/
      python manage.py runserver 0.0.0.0:8001
EOF
 sed 's/^\s\+//' > execution_file.sh <<EOF
      #!/bin/bash

      cd drinkmanager/drinkmanager/
      python manage.py runserver 0.0.0.0:8001
EOF

chmod a+x execution_file.sh
```
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

