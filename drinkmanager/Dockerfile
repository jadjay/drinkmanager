FROM python:2.7
MAINTAINER javond@adista.fr

ENV PYTHONUNBUFFERED 1
#ARG ARG_DJANGO_DATABASE_DIR
#ENV DJANGO_DATABASE_DIR=$ARG_DJANGO_DATABASE_DIR

RUN apt-get update
RUN apt-get install -y python-pip python-urllib3 gettext-base apt-utils

RUN mkdir /database
RUN useradd -m -d /code -s /bin/bash drink
RUN chown drink /database

USER drink
ENV PATH=/code/.local/bin:$PATH
WORKDIR /code
ADD ./requirements.txt /tmp
RUN python -m pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt


