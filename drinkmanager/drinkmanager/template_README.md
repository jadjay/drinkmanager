# Création des environnements d'executions

1. Editer le fichier [template_values.yaml](template_values.yaml)
```yaml

#secure_key: 
#debug: True
#allowed_hosts:
databases:
    name: db.xxENVIRONNEMENTxx.sqlite3
    # remplacez xxENVIRONNEMENTxx par dev, prod, preprod etc...
    engine: django.db.backends.sqlite3

email:
  #host:
  #port:
  #user:
  #password:
  #tls:
```
> Les variables commentées sont facultatives

2. Lancez la commande suivante 

```shell
user@home drinkmanager/ $ j2 template_settings.py.j2 template_values.yaml > drinkmanager/settings_xxENVIRONNEMENTxx.py
```
> remplacez xxENVIRONNEMENTxx par dev, prod, preprod etc...

Vous disposez d'un fichier de configuration spécifique à votre environnement (dev,preprod etc...).
Il ne vous reste plus qu'à lancer le serveur en utilisant la variable d'environnement **DJANGO_SETTINGS_MODULE**

```shell
user@home drinkmanager/ $ DJANGO_SETTINGS_MODULE=drinkmanager.settings_xxENVIRONNEMENTxx ./manage.py runserver
```

