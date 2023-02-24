# drinkmanager

## Docker

### Installation, tests

- [Installer docker](https://docs.docker.com/get-docker/)
- [Installer git](https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git)

Copiez ce code et collez le dans un terminal d'un serveur Docker :

```shell
git clone https://github.com/jadjay/drinkmanager.git
cd drinkmanager
```

⚠️  Modifiez le fichier ```execution_file.sh``` ⚠️

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
ou 
```shell
docker-compose run --build
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


# TODO

- gérer un USER dans le docker

Dockerfile: 
```Dockerfile

FROM python:3
MAINTAINER truc@bidule.fr

ENV PYTHONUNBUFFERED 1

RUN useradd -m -d /code -u 1000 -g 1000 jeannot_lapin
WORKDIR /code
ADD . /code

USER jeannot_lapin
```

docker-compose.yml: 
```yaml
    web:
      build: .
      command: ./execution_file.sh
      user: "1000:1000"
      volumes:
        - .:/code
      ports:
        - "8001:8001"

```

# TODO

* [ ] Ajouter la liste des consommations dans le mail
* [ ] Gérer un utilisateur hors root dans le Dockerfile et docker-compose
* [ ] Docker-compose + gitlab ci-cd 
  * https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

