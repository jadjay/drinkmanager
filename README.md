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
sed 's/    //' > Dockerfile <<EOF
    FROM python:2.7
    MAINTAINER javond@adista.fr
    ENV PYTHONUNBUFFERED 1
    RUN mkdir /code
    WORKDIR /code
    ADD requirements.txt /code/
    RUN pip install -r requirements.txt
    ADD . /code/
EOF
sed 's/    //' > requirements.txt <<EOF
    Django
    django-registration
    django-qrcode
    jsonfield
    Pillow
EOF
git clone git@github.com:jadjay/drinkmanager.git
sed 's/    //' > docker-compose.yml <<EOF
    web:
      build: .
      command: ./execution_file.sh
      volumes:
        - .:/code
      ports:
        - "8001:8001"
EOF
sed 's/    //' > execution_file.sh <<EOF
      #!/bin/bash
      cd drinkmanager/drinkmanager/
      python manage.py runserver 0.0.0.0:8001
EOF
docker-compose up
```

