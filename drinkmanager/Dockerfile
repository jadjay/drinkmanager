FROM python:3
MAINTAINER javond@adista.fr

ENV PYTHONUNBUFFERED 1
#ARG ARG_DJANGO_DATABASE_DIR
#ENV DJANGO_DATABASE_DIR=$ARG_DJANGO_DATABASE_DIR

RUN apt-get update
RUN apt-get install -y python3-pip python3-urllib3 gettext-base apt-utils
#python3 python3-pip pipenv git
#RUN pipenv --three sync

#RUN mkdir /code
#RUN mkdir /${DJANGO_DATABASE_DIR}
RUN mkdir /database
RUN useradd -m -d /code -s /bin/bash drink
RUN chown drink /database

USER drink
ENV PATH=/code/.local/bin:$PATH
WORKDIR /code
ADD ./requirements.txt /tmp
RUN python -m pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt


